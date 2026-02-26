# Contributing to CardSight AI Python SDK

Thank you for your interest in contributing to the CardSight AI Python SDK! We welcome contributions from the community and are grateful for your support.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. We expect all contributors to:

- Be respectful and considerate in all interactions
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/cardsightai-sdk-python.git
   cd cardsightai-sdk-python
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/CardSightAI/cardsightai-sdk-python.git
   ```

## Development Setup

### Prerequisites

- Python 3.10 or higher
- Poetry (package manager)
- Git

### Installation

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install --with dev,docs
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. Set up pre-commit hooks (optional but recommended):
   ```bash
   make setup-pre-commit
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Reports**: Found a bug? Let us know!
- **Feature Requests**: Have an idea? We'd love to hear it!
- **Code Contributions**: Bug fixes, new features, or improvements
- **Documentation**: Improvements to README, code comments, or examples
- **Tests**: Additional test coverage or test improvements

### Bug Reports

When filing a bug report, please include:

- **Clear title and description**
- **Python version** (`python --version`)
- **SDK version** (`pip show cardsightai`)
- **Code sample** that reproduces the issue
- **Expected behavior** vs. actual behavior
- **Stack trace** if applicable

Use the GitHub issue template when creating a new issue.

### Feature Requests

For feature requests, please:

- Check if the feature already exists or is planned
- Clearly describe the use case and benefits
- Provide examples of how the feature would be used
- Consider whether it fits the SDK's scope and philosophy

## Development Workflow

### 1. Create a Branch

Create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Test additions or changes

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style
- Add or update tests as needed
- Update documentation if required

### 3. Test Your Changes

Run the test suite:

```bash
# Run all tests
make test

# Run specific test file
poetry run pytest tests/unit/test_client.py

# Run with coverage
poetry run pytest --cov=cardsightai --cov-report=html
```

### 4. Lint and Format

Ensure code quality:

```bash
# Run linting
make lint

# Auto-format code
make format

# Type check
poetry run mypy cardsightai/
```

### 5. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "feat: add support for new endpoint

- Implement new catalog.parallels endpoint
- Add tests for parallel conversions
- Update documentation with examples"
```

Commit message format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions or changes
- `refactor:` - Code refactoring
- `chore:` - Maintenance tasks

## Code Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints for all function signatures
- Maximum line length: 120 characters (configured in ruff)
- Use descriptive variable and function names

### Type Hints

All code should include type hints:

```python
from typing import Optional, List, Dict, Any

def process_cards(
    card_ids: List[str],
    options: Optional[Dict[str, Any]] = None
) -> List[Card]:
    """Process a list of cards."""
    ...
```

### Docstrings

Use Google-style docstrings:

```python
def identify_card(image_path: str, confidence_threshold: float = 0.8) -> Detection:
    """Identify a card from an image.

    Args:
        image_path: Path to the card image file
        confidence_threshold: Minimum confidence level (0.0-1.0)

    Returns:
        Detection object with card information and confidence

    Raises:
        ValueError: If image_path doesn't exist
        APIError: If the API request fails

    Example:
        >>> detection = identify_card('card.jpg')
        >>> print(detection.card.name)
        'Mike Trout Rookie'
    """
    ...
```

### Error Handling

- Use custom exceptions from `cardsightai.exceptions`
- Provide helpful error messages
- Log errors appropriately

### Import Organization

Organize imports in this order:

```python
# Standard library
import os
from typing import Optional

# Third-party
import httpx
from attrs import define

# Local imports
from cardsightai.exceptions import APIError
from cardsightai.models import Card
```

## Testing Guidelines

### Test Structure

- Unit tests: `tests/unit/`
- Integration tests: `tests/integration/`
- Fixtures: `tests/fixtures/`

### Writing Tests

```python
import pytest
from cardsightai import CardSightAI


def test_catalog_statistics():
    """Test catalog statistics endpoint."""
    client = CardSightAI(api_key='test_key')
    # Mock the HTTP response
    with respx.mock:
        respx.get("https://api.cardsight.ai/v1/catalog/statistics").mock(
            return_value=httpx.Response(200, json={'cards': {'total': 1000}})
        )

        stats = client.catalog.statistics()
        assert stats.cards.total == 1000


@pytest.mark.asyncio
async def test_async_catalog_statistics():
    """Test async catalog statistics endpoint."""
    async with AsyncCardSightAI(api_key='test_key') as client:
        stats = await client.catalog.statistics()
        assert stats.cards.total > 0
```

### Test Coverage

- Aim for >90% code coverage
- Test both success and failure cases
- Test edge cases and error conditions
- Use mocking for API calls in unit tests
- Integration tests should use real API (with proper keys)

## Documentation

### Code Comments

- Comment complex logic
- Don't comment obvious code
- Keep comments up-to-date

### README Updates

If your change affects usage:

- Update relevant sections in README.md
- Add examples if introducing new features
- Update the API coverage table if needed

### Changelog

Significant changes should be noted in CHANGELOG.md:

```markdown
## [Unreleased]

### Added
- New `catalog.parallels` endpoint support

### Fixed
- Fixed event loop handling in sync client

### Changed
- Updated httpx dependency to 0.28.1
```

## Submitting Changes

### Pull Request Process

1. **Update your fork**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what changed and why
   - Reference to related issues (e.g., "Fixes #123")
   - Screenshots if UI/output changes
   - Checklist of completed tasks

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added new tests for changes
- [ ] Updated documentation

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
```

### Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, a maintainer will merge your PR

## Release Process

(For maintainers)

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Creating a Release

1. Update version in `cardsightai/version.py`
2. Update `CHANGELOG.md`
3. Create a git tag:
   ```bash
   git tag -a v1.2.3 -m "Release version 1.2.3"
   git push origin v1.2.3
   ```
4. GitHub Actions will automatically publish to PyPI

## Need Help?

- **Questions**: Open a [GitHub Discussion](https://github.com/CardSightAI/cardsightai-sdk-python/discussions)
- **Issues**: Check existing [Issues](https://github.com/CardSightAI/cardsightai-sdk-python/issues)
- **Email**: support@cardsight.ai
- **Discord**: [Join our community](https://discord.gg/cardsightai)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to CardSight AI Python SDK! 🎉