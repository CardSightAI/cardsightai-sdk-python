#!/usr/bin/env python3
"""
Post-generation script to apply custom modifications to the generated client.

This script is run after openapi-python-client generates the base client code.
It applies any custom modifications needed for the CardSight AI SDK.
"""

from pathlib import Path


def create_py_typed():
    """Ensure py.typed file exists for type checking support."""
    print("Ensuring py.typed file...")

    py_typed = Path("cardsightai/py.typed")
    if not py_typed.exists():
        py_typed.touch()
        print("Created py.typed file")
    else:
        print("py.typed file already exists")


def main():
    """Run all post-generation modifications."""
    print("\nStarting post-generation processing...")

    create_py_typed()

    # Placeholder hooks for future customizations:
    # - fix_import_paths(): Fix any import path issues in generated code
    # - add_custom_docstrings(): Enhance docstrings in generated code
    # - ensure_type_hints(): Verify type hints in generated functions
    # - update_client_defaults(): Modify default values in generated client

    print("\nPost-generation processing completed!")


if __name__ == "__main__":
    main()
