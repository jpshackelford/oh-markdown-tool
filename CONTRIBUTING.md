# Contributing to oh-markdown-tool

Thank you for your interest in contributing to oh-markdown-tool! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jpshackelford/oh-markdown-tool.git
   cd oh-markdown-tool
   ```

2. **Install dependencies**
   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install the package with dev dependencies
   make dev
   # or
   uv pip install -e ".[dev]"
   ```

3. **Run tests to verify setup**
   ```bash
   make test
   ```

## Development Workflow

### Making Changes

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes**
   - Write clean, well-documented code
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Run code quality checks**
   ```bash
   # Format code
   make format

   # Run linter
   make lint

   # Run tests
   make test

   # Run tests with coverage
   make test-cov

   # Or run all checks at once
   make all
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature"
   # or
   git commit -m "fix: resolve issue with X"
   ```

   We follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `test:` for test changes
   - `refactor:` for code refactoring
   - `chore:` for maintenance tasks

5. **Push and create a pull request**
   ```bash
   git push origin your-branch-name
   ```

   Then create a pull request on GitHub.

### Automated PR Review

This repository uses **OpenHands** for automated code reviews. When you open a PR:

- The bot will automatically review your changes
- You'll receive **roasted** 🔥 feedback - direct, critical, and honest
- Expect no-nonsense reviews on code quality, best practices, and potential issues
- Reviews typically complete within a few minutes

**Trigger a review manually:**
- Add the `review-this` label to your PR
- Request `openhands-agent` as a reviewer
- Mark a draft PR as "Ready for review"

See [.github/OPENHANDS_REVIEW.md](.github/OPENHANDS_REVIEW.md) for more details.

## Code Quality Standards

### Testing

- Write tests for all new functionality
- Maintain or improve code coverage (minimum 80%)
- Tests should be clear and well-documented
- Use descriptive test names that explain what is being tested

### Code Style

- We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- Line length: 100 characters
- Follow PEP 8 guidelines
- Use type hints where appropriate

### Documentation

- Update docstrings for modified functions/classes
- Update README.md if adding new features
- Add examples for new functionality
- Keep documentation clear and concise

## Project Structure

```
oh-markdown-tool/
├── src/oh_markdown_tool/  # Main package code
│   ├── __init__.py        # Package exports
│   ├── parser.py          # Markdown parsing
│   ├── numbering.py       # Section numbering
│   ├── toc.py            # Table of contents
│   ├── operations.py     # Section operations
│   ├── formatter.py      # Formatting & linting
│   └── tool.py           # OpenHands SDK integration
├── tests/                 # Test suite
│   ├── fixtures/         # Test fixtures
│   └── test_*.py         # Test files
├── examples/             # Usage examples
└── doc/                  # Additional documentation
```

## Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run specific test file
uv run pytest tests/test_parser.py -v

# Run specific test
uv run pytest tests/test_parser.py::TestMarkdownParser::test_parse_simple -v
```

## Common Tasks

### Adding a New Command

1. Add the command to `MarkdownAction.command` enum in `tool.py`
2. Implement the command handler in `MarkdownExecutor`
3. Add observation fields in `MarkdownObservation` if needed
4. Add visualization in `MarkdownObservation.visualize`
5. Write tests in `tests/test_tool.py`
6. Update documentation

### Adding a New Feature

1. Implement the feature in the appropriate module
2. Add tests with good coverage
3. Update the tool integration if needed
4. Add examples in `examples/`
5. Update README.md
6. Document in `doc/markdown-tool.md`

## Reporting Issues

When reporting issues, please include:

- A clear description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (Python version, OS, etc.)
- Minimal code example if applicable

## Questions?

Feel free to open an issue for questions or discussion about potential contributions.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
