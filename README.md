# OpenHands Markdown Document Tool

[![CI](https://github.com/jpshackelford/oh-markdown-tool/actions/workflows/ci.yml/badge.svg)](https://github.com/jpshackelford/oh-markdown-tool/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/oh-markdown-tool.svg)](https://badge.fury.io/py/oh-markdown-tool)
[![Python versions](https://img.shields.io/pypi/pyversions/oh-markdown-tool.svg)](https://pypi.org/project/oh-markdown-tool/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive tool for structural editing and formatting of markdown documents, designed for use with [OpenHands](https://github.com/All-Hands-AI/OpenHands) AI agents.

## Features

This tool provides AI agents with powerful markdown document manipulation capabilities:

### Document Structure
- **Overview** - Display hierarchical document structure with sections, line numbers, and nesting
- **Validate** - Check section numbering consistency and table of contents accuracy
- **Renumber** - Automatically fix section numbering sequentially

### Table of Contents
- **Generate/Update TOC** - Create or refresh table of contents with configurable depth
- **Remove TOC** - Clean removal of table of contents section

### Section Operations
- **Move** - Relocate sections (with children) to new positions
- **Insert** - Add new sections at specific locations
- **Delete** - Remove sections and their subsections
- **Promote** - Increase heading level (### → ##)
- **Demote** - Decrease heading level (## → ###)

### Formatting
- **Rewrap** - Normalize paragraph line lengths with smart wrapping
- **Lint** - Detect markdown formatting issues
- **Fix** - Auto-fix common markdown problems
- **Cleanup** - Comprehensive cleanup (rewrap + fix + renumber + update TOC)

## Installation

The core library (markdown parsing, numbering, TOC, formatting) has no dependency on
the OpenHands SDK:

```bash
pip install oh-markdown-tool          # or: uv pip install oh-markdown-tool
```

To use it as an OpenHands agent tool, install the `openhands` extra. It pulls in
`openhands-sdk`, which requires **Python 3.12+**:

```bash
pip install "oh-markdown-tool[openhands]"
```

## Usage as an OpenHands agent tool

The tool lives in `oh_markdown_tool.tool`; importing that module registers it under the
name `markdown_document`.

```python
from openhands.sdk import Agent
from oh_markdown_tool.tool import MarkdownDocumentTool

# Create an agent with the markdown tool
agent = Agent(
    tools=[MarkdownDocumentTool],
    # ... other configuration
)

# The agent can now use commands like:
# - "Show me the overview of doc/design.md"
# - "Renumber the sections in README.md"
# - "Update the table of contents in design.md"
# - "Move section 4.3 to after section 2"
```

On a **remote agent-server**, reference the tool by its module qualname so the server
imports and registers it on conversation creation:

```python
"tools": [{"name": "markdown_document"}],
"tool_module_qualnames": {"markdown_document": "oh_markdown_tool.tool"},
```

## Standalone usage (no agent)

`MarkdownExecutor` runs the operations directly. It lives in `oh_markdown_tool.tool` and
therefore needs the `[openhands]` extra (the action/observation types build on the SDK):

```python
from pathlib import Path
from oh_markdown_tool.tool import MarkdownAction, MarkdownExecutor

# Initialize executor with workspace directory
executor = MarkdownExecutor(workspace_dir=Path("."))

# Get document overview
action = MarkdownAction(command="overview", file="design.md")
result = executor.execute(action)
print(result.content)

# Renumber sections
action = MarkdownAction(command="renumber", file="design.md")
result = executor.execute(action)
print(f"Renumbered {result.sections_renumbered} sections")

# Update table of contents
action = MarkdownAction(command="toc_update", file="design.md", depth=3)
result = executor.execute(action)
print(f"TOC updated with {result.toc_entries} entries")
```

For SDK-free, lower-level access, import the core classes directly (no `[openhands]`
extra needed):

```python
from oh_markdown_tool import MarkdownParser, SectionNumberer, TocManager
```

## Document Conventions

### Section Numbering
- Document title uses `#` (h1) and is unnumbered
- Top-level sections use `##` (h2): `## 1. Introduction`
- Subsections are numbered hierarchically: `### 1.1 Purpose`, `#### 1.1.1 Detail`

### Table of Contents
- TOC section uses `## Table Of Contents` (unnumbered, case-insensitive)
- Appears after document title, before first numbered section
- Depth is configurable (default: 3 levels)

### Section References
Sections can be referenced by:
- **Number**: `"3.2"` (current numbering in document)
- **Title**: `"Implementation Plan"` (exact title match)

## Available Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `overview` | Show document structure | `file` |
| `validate` | Check structure consistency | `file` |
| `renumber` | Fix section numbering | `file` |
| `toc_update` | Generate/update TOC | `file`, `depth` (default: 3) |
| `toc_remove` | Remove TOC | `file` |
| `move` | Move a section | `file`, `section`, `position`, `target` |
| `insert` | Insert new section | `file`, `heading`, `level`, `position`, `target` |
| `delete` | Delete section | `file`, `section` |
| `promote` | Increase heading level | `file`, `section` |
| `demote` | Decrease heading level | `file`, `section` |
| `rewrap` | Rewrap paragraphs | `file`, `width` (default: 80) |
| `lint` | Check for issues | `file` |
| `fix` | Auto-fix issues | `file` |
| `cleanup` | Full cleanup | `file`, `width`, `depth` |

## Architecture

The tool is composed of several specialized components:

```
oh_markdown_tool/
├── parser.py          # Parse markdown into section tree
├── numbering.py       # Validate and renumber sections
├── toc.py            # Table of contents management
├── operations.py     # Section operations (move, insert, delete, etc.)
├── formatter.py      # Formatting, linting, and fixing
└── tool.py           # OpenHands SDK tool integration
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/jpshackelford/oh-markdown-tool.git
cd oh-markdown-tool

# Install with dev dependencies
pip install -e ".[dev]"

# Or with uv
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=oh_markdown_tool --cov-report=html
```

### Code Quality

```bash
# Format and lint
ruff check .
ruff format .
```

## Dependencies

Core:
- `openhands-sdk>=1.19.0` - OpenHands SDK integration
- `pydantic>=2.0.0` - Data validation
- `mdformat>=0.7` - Paragraph rewrapping
- `pymarkdownlnt>=0.9` - Linting and auto-fixing
- `rich>=13.0.0` - Terminal formatting

## License

MIT License - see LICENSE file for details

## Credits

Originally developed as part of the [lxa](https://github.com/jpshackelford/lxa) project.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/) and [Release Please](https://github.com/googleapis/release-please) for automated releases. Please use the following commit message format:

```bash
feat: add new feature       # New features (minor version bump)
fix: correct bug            # Bug fixes (patch version bump)
docs: update documentation  # Documentation changes
refactor: improve code      # Code refactoring
test: add tests            # Test changes
chore: update dependencies  # Maintenance tasks
```

Breaking changes should include `!` or `BREAKING CHANGE:` in the footer:
```bash
feat!: redesign API
```

See [PUBLISHING.md](PUBLISHING.md) for details on the release process.

### Automated Code Review

This repository uses [OpenHands](https://github.com/All-Hands-AI/OpenHands) for automated PR reviews. When you open a PR:
- ✅ Automated review with direct, honest feedback 🔥
- ✅ Code quality critique
- ✅ Best practices enforcement

Reviews are **roasted** style - expect critical, no-nonsense feedback. See [.github/OPENHANDS_REVIEW.md](.github/OPENHANDS_REVIEW.md) for details.

### Development Guidelines

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.
