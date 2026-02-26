.PHONY: help install regenerate test lint format clean build publish publish-test

help:  ## Show this help
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies
	poetry install --with dev,docs

regenerate:  ## Regenerate SDK from OpenAPI specification
	@echo "Regenerating SDK from OpenAPI spec..."
	poetry run python scripts/generate_client.py

test:  ## Run tests
	poetry run pytest tests/ -v --cov=cardsightai --cov-report=term-missing

test-integration:  ## Run integration tests (requires API key)
	poetry run pytest tests/integration/ -v

lint:  ## Run linting and type checking
	poetry run ruff check cardsightai/
	poetry run ruff format --check cardsightai/
	poetry run mypy cardsightai/ --ignore-missing-imports

format:  ## Format code
	poetry run ruff check --fix cardsightai/
	poetry run ruff format cardsightai/

clean:  ## Clean build artifacts
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:  ## Build distribution packages
	poetry build

publish-test:  ## Publish to Test PyPI
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi

publish:  ## Publish to PyPI
	poetry publish

dev:  ## Run development server with example
	poetry run python examples/basic_usage.py

docs:  ## Build documentation
	poetry run mkdocs build

docs-serve:  ## Serve documentation locally
	poetry run mkdocs serve

check:  ## Run all checks (lint, test)
	$(MAKE) lint
	$(MAKE) test

setup-pre-commit:  ## Setup pre-commit hooks
	poetry run pre-commit install
	poetry run pre-commit autoupdate

run-pre-commit:  ## Run pre-commit on all files
	poetry run pre-commit run --all-files