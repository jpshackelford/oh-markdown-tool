.PHONY: help install dev lint format test test-cov clean all check

# Default target
help:
	@echo "oh-markdown-tool - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install    Install in editable mode"
	@echo "  make dev        Install with development dependencies"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint       Run ruff linter"
	@echo "  make format     Format code with ruff"
	@echo "  make check      Run all checks (lint)"
	@echo ""
	@echo "Testing:"
	@echo "  make test       Run tests"
	@echo "  make test-cov   Run tests with coverage report"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean      Remove build artifacts and caches"
	@echo "  make all        Run all checks and tests"

# Install in editable mode
install:
	uv pip install -e .

# Install development dependencies
dev:
	uv pip install -e ".[dev]"

# Run linter (matches CI checks)
lint:
	uv run ruff check src tests
	uv run ruff format --check src tests

# Format code (auto-fix)
format:
	uv run ruff format src tests
	uv run ruff check --fix src tests

# Run all code quality checks
check: lint

# Run tests
test:
	uv run pytest tests -v

# Run tests with coverage
test-cov:
	uv run pytest tests -v \
		--cov=oh_markdown_tool \
		--cov-report=term-missing \
		--cov-report=html \
		--cov-fail-under=80

# Clean build artifacts
clean:
	rm -rf __pycache__ .pytest_cache .ruff_cache htmlcov .coverage coverage.xml
	rm -rf build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Run all checks and tests
all: check test
