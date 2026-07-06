"""Basic end-to-end agent evals.

Starting deliberately small: two simple, single-command instructions. Each runs
once (rep=1) against a tiny document to bound token spend. Assertions check the
end-state of the file, not the exact tool-call transcript, since the agent's
path is non-deterministic.
"""

import pytest

pytestmark = pytest.mark.agent_eval


def test_agent_renumbers_sections(run_instruction, tmp_path):
    """The agent should renumber out-of-order sections to 1, 2, 3..."""
    doc = "# Spec\n\n## 5. Introduction\n\nIntro.\n\n## 10. Methods\n\nMethods.\n"
    result = run_instruction(
        tmp_path,
        "spec.md",
        doc,
        "In spec.md, renumber the sections so they start at 1 and increment by 1.",
    )
    assert "## 1. Introduction" in result
    assert "## 2. Methods" in result


def test_agent_creates_toc(run_instruction, tmp_path):
    """The agent should generate a table of contents for the document."""
    doc = "# Spec\n\n## 1. Introduction\n\nIntro.\n\n## 2. Methods\n\nMethods.\n"
    result = run_instruction(
        tmp_path,
        "spec.md",
        doc,
        "Add a table of contents to spec.md.",
    )
    assert "Table of Contents" in result
    assert "- 1. Introduction" in result
    assert "- 2. Methods" in result


def test_agent_renumbers_and_adds_toc(run_instruction, tmp_path):
    """Combined instruction (renumber + TOC) on an out-of-order document.

    This mirrors the real-world task that previously crashed the run: the first
    tool observation was empty, which — with prompt caching on — raised an
    IndexError before the edit could complete.
    """
    doc = (
        "# Project Documentation\n\n"
        "## 5. Introduction\n\nThis is the introduction section.\n\n"
        "### 5.2 Background\n\nSome background information.\n\n"
        "## 10. Methods\n\nThis is the methods section.\n\n"
        "### 10.1 Approach\n\nOur approach.\n\n"
        "## 3. Results\n\nThe results section.\n"
    )
    result = run_instruction(
        tmp_path,
        "sample.md",
        doc,
        "sample.md has inconsistent section numbering. Renumber the sections "
        "sequentially starting from 1, and add a table of contents after the title.",
    )
    assert "## 1. Introduction" in result
    assert "## 2. Methods" in result
    assert "## 3. Results" in result
    assert "Table of Contents" in result
