"""Markdown document tool for structural editing and formatting."""

__version__ = "0.1.0"

from .numbering import NumberingIssue, RenumberResult, SectionNumberer, ValidationResult
from .parser import MarkdownParser, ParseResult, Section
from .toc import (
    TocAction,
    TocManager,
    TocRemoveResult,
    TocUpdateResult,
    TocValidationResult,
)
from .tool import MarkdownAction, MarkdownDocumentTool, MarkdownExecutor, MarkdownObservation

__all__ = [
    "__version__",
    "MarkdownParser",
    "ParseResult",
    "Section",
    "SectionNumberer",
    "NumberingIssue",
    "RenumberResult",
    "ValidationResult",
    "MarkdownDocumentTool",
    "MarkdownAction",
    "MarkdownObservation",
    "MarkdownExecutor",
    "TocAction",
    "TocManager",
    "TocUpdateResult",
    "TocRemoveResult",
    "TocValidationResult",
]
