"""Fixtures for end-to-end agent evals.

These evals run a real LLM agent, equipped only with the ``markdown_document``
tool, against natural-language editing instructions. They exist to catch a class
of regression the unit tests cannot: whether the model can translate plain
instructions into correct tool calls given the tool's description and schema.

They are non-deterministic and cost money, so they are excluded from the default
`pytest` run (see the ``-m "not agent_eval"`` default in ``pyproject.toml``) and
are intended to be triggered manually.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

# The evals need the ``[openhands]`` extra. Skip cleanly if it is not installed.
pytest.importorskip("openhands.sdk", reason="agent evals require the [openhands] extra")

from openhands.sdk import LLM, Agent, Conversation, Tool  # noqa: E402
from pydantic import SecretStr  # noqa: E402

# Importing the module registers the ``markdown_document`` tool as a side effect.
import oh_markdown_tool.tool  # noqa: E402,F401
from oh_markdown_tool.tool import MarkdownDocumentTool  # noqa: E402

# Pinned model — do NOT let this float. Matches the PR-review bot configuration so
# eval results are comparable across runs and only change when we change it here.
EVAL_MODEL = "litellm_proxy/claude-sonnet-4-5-20250929"
# Base URL is overridable (e.g. to run locally against a different proxy) but the
# model itself stays pinned.
EVAL_BASE_URL = os.environ.get("EVAL_LLM_BASE_URL", "https://llm-proxy.app.all-hands.dev")


@pytest.fixture(scope="session")
def llm_api_key() -> str:
    key = os.environ.get("LLM_API_KEY")
    if not key:
        pytest.skip("LLM_API_KEY not set; skipping agent evals")
    return key


@pytest.fixture
def agent(llm_api_key: str) -> Agent:
    """An agent equipped ONLY with the markdown tool.

    No default file editor or terminal is included, so the agent must exercise
    the ``markdown_document`` tool to satisfy an instruction — which is exactly
    what we want to evaluate.
    """
    # Prompt caching is left ON so the eval mirrors production (Cloud + PR-review
    # bot both run cache-eligible Anthropic models with caching enabled). This is
    # deliberate: an empty tool observation combined with caching used to crash the
    # run, and we want the evals to catch that class of regression rather than hide
    # it behind caching_prompt=False.
    llm = LLM(
        usage_id="agent-eval",
        model=EVAL_MODEL,
        base_url=EVAL_BASE_URL,
        api_key=SecretStr(llm_api_key),
        temperature=0.0,
    )
    return Agent(llm=llm, tools=[Tool(name=MarkdownDocumentTool.name)])


@pytest.fixture
def run_instruction(agent: Agent):
    """Return a helper that writes ``doc`` into a workspace, sends ``instruction``
    to the agent, runs to completion, and returns the resulting file content.
    """

    def _run(tmp_path: Path, filename: str, doc: str, instruction: str) -> str:
        file_path = tmp_path / filename
        file_path.write_text(doc)
        conversation = Conversation(agent=agent, workspace=str(tmp_path))
        conversation.send_message(instruction)
        conversation.run()
        return file_path.read_text()

    return _run
