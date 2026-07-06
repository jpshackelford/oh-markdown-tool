"""Markdown document tool for structural editing and formatting."""

__version__ = "0.2.2"

from .numbering import NumberingIssue, RenumberResult, SectionNumberer, ValidationResult
from .parser import MarkdownParser, ParseResult, Section
from .toc import (
    TocAction,
    TocManager,
    TocRemoveResult,
    TocUpdateResult,
    TocValidationResult,
)

# The OpenHands tool integration lives in ``oh_markdown_tool.tool`` and is imported
# separately (see ``pip install "oh-markdown-tool[openhands]"``). It is intentionally
# NOT imported here so the core library has no dependency on ``openhands-sdk`` and
# importing this package triggers no tool-registration side effects.

__all__ = [
    "__version__",
    "MarkdownParser",
    "ParseResult",
    "Section",
    "SectionNumberer",
    "NumberingIssue",
    "RenumberResult",
    "ValidationResult",
    "TocAction",
    "TocManager",
    "TocUpdateResult",
    "TocRemoveResult",
    "TocValidationResult",
]
