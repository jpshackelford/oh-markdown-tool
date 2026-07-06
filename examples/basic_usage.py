"""Basic usage example for the oh-markdown-tool."""

from pathlib import Path

from oh_markdown_tool.tool import MarkdownAction, MarkdownExecutor


def main():
    """Demonstrate basic markdown tool operations."""
    # Create a sample markdown file
    sample_doc = """# My Document

## 5. Introduction

This is the introduction.

### 5.1 Purpose

The purpose section.

## 10. Methods

This is the methods section.

### 10.1 Approach

Our approach.

## 15. Results

The results section.
"""

    # Write sample document
    doc_path = Path("sample.md")
    doc_path.write_text(sample_doc)

    # Initialize executor with current directory
    executor = MarkdownExecutor(workspace_dir=Path())

    # 1. Get document overview
    print("=" * 60)
    print("OVERVIEW")
    print("=" * 60)
    action = MarkdownAction(command="overview", file="sample.md")
    result = executor.execute(action)
    print(result.content)
    print()

    # 2. Validate document structure
    print("=" * 60)
    print("VALIDATION")
    print("=" * 60)
    action = MarkdownAction(command="validate", file="sample.md")
    result = executor.execute(action)
    print(result.content)
    if result.numbering_issues:
        print(f"\nFound {len(result.numbering_issues)} numbering issues")
    print()

    # 3. Renumber sections
    print("=" * 60)
    print("RENUMBERING")
    print("=" * 60)
    action = MarkdownAction(command="renumber", file="sample.md")
    result = executor.execute(action)
    print(result.content)
    print(f"Renumbered {result.sections_renumbered} sections")
    print()

    # 4. Add table of contents
    print("=" * 60)
    print("ADD TABLE OF CONTENTS")
    print("=" * 60)
    action = MarkdownAction(command="toc_update", file="sample.md", depth=3)
    result = executor.execute(action)
    print(result.content)
    print(f"TOC {result.toc_action} with {result.toc_entries} entries")
    print()

    # 5. Show final document
    print("=" * 60)
    print("FINAL DOCUMENT")
    print("=" * 60)
    final_content = doc_path.read_text()
    print(final_content)

    # Cleanup
    doc_path.unlink()


if __name__ == "__main__":
    main()
