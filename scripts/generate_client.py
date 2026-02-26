#!/usr/bin/env python3
"""
Regenerate the CardSight AI SDK from the latest OpenAPI specification.

This script:
1. Fetches the latest OpenAPI spec from the API
2. Regenerates the client code
3. Applies any post-generation modifications
4. Validates the generated code
"""

import subprocess
import sys
import shutil
from pathlib import Path


def check_dependencies():
    """Check if required dependencies are installed."""
    # Check for openapi-python-client
    result = subprocess.run(
        ["poetry", "run", "openapi-python-client", "--version"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("Error: openapi-python-client not found. Installing...")
        subprocess.run(["poetry", "add", "--group", "dev", "openapi-python-client"])


def generate_client():
    """Generate the client from OpenAPI specification."""
    print("Fetching OpenAPI specification from https://api.cardsight.ai/documentation/json")
    print("Generating client code...")

    # Remove old generated code
    generated_path = Path("cardsightai/generated")
    if generated_path.exists():
        print(f"Removing old generated code at {generated_path}")
        shutil.rmtree(generated_path)

    # Run openapi-python-client
    result = subprocess.run(
        [
            "poetry", "run", "openapi-python-client", "generate",
            "--url", "https://api.cardsight.ai/documentation/json",
            "--output-path", "./cardsightai/generated",
            "--config", "config.yml",
            "--overwrite"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error generating client:\n{result.stderr}")
        return False

    print("Client generated successfully!")
    if result.stdout:
        print(f"Generation output:\n{result.stdout}")

    return True


def post_process():
    """Apply post-generation modifications."""
    print("\nApplying post-generation modifications...")

    # Run the post-processing script if it exists
    post_process_script = Path("scripts/post_generate.py")
    if post_process_script.exists():
        result = subprocess.run(
            ["poetry", "run", "python", str(post_process_script)],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Warning: Post-processing failed:\n{result.stderr}")
        else:
            print("Post-processing completed successfully!")
    else:
        print("No post-processing script found, skipping...")


def validate_generated_code():
    """Validate the generated code with linting and type checking."""
    print("\nValidating generated code...")

    # Run ruff for linting
    print("Running ruff...")
    result = subprocess.run(
        ["poetry", "run", "ruff", "check", "cardsightai/generated/", "--fix"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Ruff found issues (auto-fixed where possible):\n{result.stdout}")

    # Format with ruff
    print("Formatting code...")
    subprocess.run(
        ["poetry", "run", "ruff", "format", "cardsightai/generated/"],
        capture_output=True
    )

    print("Validation completed!")


def update_version():
    """Update version information if needed."""
    # This could be expanded to automatically bump version numbers
    print("\nVersion information:")
    version_file = Path("cardsightai/version.py")
    if version_file.exists():
        with open(version_file, "r") as f:
            content = f.read()
            if "__version__" in content:
                version_line = [line for line in content.split("\n") if "__version__" in line][0]
                print(f"Current SDK {version_line}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("CardSight AI SDK Regeneration Script")
    print("=" * 60)

    # Check dependencies
    check_dependencies()

    # Generate client
    if not generate_client():
        print("\nGeneration failed!")
        sys.exit(1)

    # Post-process
    post_process()

    # Validate
    validate_generated_code()

    # Update version info
    update_version()

    print("\n" + "=" * 60)
    print("SDK regeneration completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review the changes: git diff cardsightai/generated/")
    print("2. Run tests: make test")
    print("3. Update version if needed: edit cardsightai/version.py")
    print("4. Commit changes if everything looks good")


if __name__ == "__main__":
    main()