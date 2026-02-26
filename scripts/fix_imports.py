#!/usr/bin/env python3
"""
Script to fix generated API imports in client.py by mapping incorrect import names
to correct module names based on the actual generated files.
"""

import re
import os
from pathlib import Path

# Mapping of incorrect imports to correct module names
# Format: {incorrect_name: (api_category, correct_module_name)}
IMPORT_FIXES = {
    # Card Identification
    "post_v1_identify_card": ("card_identification", "identify_card"),

    # Catalog
    "get_v1_catalog_segments": ("catalog", "get_segments"),
    "get_v1_catalog_manufacturers": ("catalog", "get_manufacturers"),
    "get_v1_catalog_releases": ("catalog", "get_releases"),
    "get_v1_catalog_releases_id": ("catalog", "get_release"),
    "get_v1_catalog_releases_random": ("catalog", "get_random_releases"),
    "get_v1_catalog_releases_id_cards": ("catalog", "get_release_cards"),
    "get_v1_catalog_sets": ("catalog", "get_sets"),
    "get_v1_catalog_sets_id": ("catalog", "get_set"),
    "get_v1_catalog_sets_random": ("catalog", "get_random_sets"),
    "get_v1_catalog_sets_id_cards": ("catalog", "get_set_cards"),
    "get_v1_catalog_cards": ("catalog", "get_cards"),
    "get_v1_catalog_cards_id": ("catalog", "get_card"),
    "get_v1_catalog_cards_random": ("catalog", "get_random_cards"),
    "get_v1_catalog_attributes": ("catalog", "get_attributes"),
    "get_v1_catalog_attributes_id": ("catalog", "get_attribute_by_id"),
    "get_v1_catalog_parallels": ("catalog", "get_parallels"),

    # Collection Management
    "post_v1_collection": ("collection_management", "create_collection"),
    "get_v1_collection": ("collection_management", "get_collections"),
    "get_v1_collection_id": ("collection_management", "get_collection"),
    "put_v1_collection_id": ("collection_management", "update_collection"),
    "delete_v1_collection_id": ("collection_management", "delete_collection"),
    "get_v1_collection_id_analytics": ("collection_management", "get_collection_analytics"),
    "get_v1_collection_id_breakdown": ("collection_management", "get_collection_breakdown"),
    "get_v1_collection_id_set_progress": ("collection_management", "get_collection_set_progress"),
    "get_v1_collection_id_set_set_id_progress": ("collection_management", "get_set_progress"),
    "get_v1_collection_id_set_set_id_parallel_parallel_id_progress": ("collection_management", "get_parallel_set_progress"),

    # Collection Cards
    "post_v1_collection_id_cards": ("collection_management", "add_collection_cards"),
    "get_v1_collection_id_cards": ("collection_management", "get_collection_cards"),
    "get_v1_collection_id_cards_card_id": ("collection_management", "get_collection_card"),
    "put_v1_collection_id_cards_card_id": ("collection_management", "update_collection_card"),
    "delete_v1_collection_id_cards_card_id": ("collection_management", "delete_collection_card"),
    "get_v1_collection_id_cards_card_id_image": ("collection_card_images", "get_collection_card_image"),
    "get_v1_collection_id_cards_card_id_image_thumbnail": ("collection_card_images", "get_collection_card_image_thumbnail"),
    "post_v1_collection_id_cards_card_id_image": ("collection_card_images", "upload_collection_card_image"),

    # Binders
    "post_v1_collection_id_binders": ("collection_management", "create_binder"),
    "get_v1_collection_id_binders": ("collection_management", "get_binders"),
    "get_v1_collection_id_binders_binder_id": ("collection_management", "get_binder"),
    "put_v1_collection_id_binders_binder_id": ("collection_management", "update_binder"),
    "delete_v1_collection_id_binders_binder_id": ("collection_management", "delete_binder"),

    # Binder Cards
    "post_v1_collection_id_binders_binder_id_cards": ("collection_management", "add_card_to_binder"),
    "get_v1_collection_id_binders_binder_id_cards": ("collection_management", "get_binder_cards"),
    "delete_v1_collection_id_binders_binder_id_cards_card_id": ("collection_management", "remove_card_from_binder"),

    # Grades
    "get_v1_grades_companies": ("grades", "get_grading_companies"),
    "get_v1_grades_companies_company_id_types": ("grades", "get_grading_types"),
    "get_v1_grades_companies_company_id_types_type_id": ("grades", "get_grades"),

    # AI
    "post_v1_ai_query": ("ai", "process_ai_query"),

    # Images
    "get_v1_images_cards_card_id": ("images", "get_card_image"),
    "get_v1_images_cards_card_id_thumbnail": ("images", "get_card_image_thumbnail"),

    # Lists
    "post_v1_lists": ("lists", "create_list"),
    "get_v1_lists": ("lists", "get_lists"),
    "get_v1_lists_id": ("lists", "get_list"),
    "put_v1_lists_id": ("lists", "update_list"),
    "delete_v1_lists_id": ("lists", "delete_list"),
    "post_v1_lists_id_cards": ("lists", "add_cards_to_list"),
    "get_v1_lists_id_cards": ("lists", "get_list_cards"),
    "delete_v1_lists_id_cards_card_id": ("lists", "remove_card_from_list"),

    # Collectors
    "post_v1_collectors": ("collectors", "create_collector"),
    "get_v1_collectors": ("collectors", "get_collectors"),
    "get_v1_collectors_id": ("collectors", "get_collector"),
    "put_v1_collectors_id": ("collectors", "update_collector"),
    "delete_v1_collectors_id": ("collectors", "delete_collector"),

    # Feedback
    "get_v1_feedback_id": ("feedback", "get_feedback"),
    "post_v1_feedback_general": ("feedback", "submit_general_feedback"),
    "post_v1_feedback_identify_id": ("feedback", "submit_identify_feedback"),
    "post_v1_feedback_card_id": ("feedback", "submit_card_feedback"),
    "post_v1_feedback_manufacturer_id": ("feedback", "submit_manufacturer_feedback"),
    "post_v1_feedback_release_id": ("feedback", "submit_release_feedback"),
    "post_v1_feedback_segment_id": ("feedback", "submit_segment_feedback"),
    "post_v1_feedback_set_id": ("feedback", "submit_set_feedback"),

    # Autocomplete
    "get_v1_autocomplete_cards": ("autocomplete", "autocomplete_cards"),
    "get_v1_autocomplete_manufacturers": ("autocomplete", "autocomplete_manufacturers"),
    "get_v1_autocomplete_releases": ("autocomplete", "autocomplete_releases"),
    "get_v1_autocomplete_segments": ("autocomplete", "autocomplete_segments"),
    "get_v1_autocomplete_sets": ("autocomplete", "autocomplete_sets"),
    "get_v1_autocomplete_years": ("autocomplete", "autocomplete_years"),

    # Subscription
    "get_v1_subscription": ("subscription", "get_subscription"),
}


def fix_imports(client_file_path: str):
    """Fix all imports in client.py"""
    with open(client_file_path, 'r') as f:
        content = f.read()

    original_content = content
    fixes_applied = 0

    for old_import, (api_category, new_module) in IMPORT_FIXES.items():
        # Pattern to match the import line
        pattern = rf'from \.generated\.card_sight_ai_edge_api_client\.api\.{api_category} import {old_import}'
        replacement = f'from .generated.card_sight_ai_edge_api_client.api.{api_category} import {new_module}'

        if pattern in content:
            content = content.replace(pattern, replacement)
            fixes_applied += 1
            print(f"✓ Fixed: {old_import} → {new_module}")

        # Also fix the usage of the import (e.g., post_v1_identify_card.asyncio → identify_card.asyncio)
        usage_pattern = rf'\b{old_import}\.(asyncio|sync)'
        content = re.sub(usage_pattern, rf'{new_module}.\1', content)

    if content != original_content:
        with open(client_file_path, 'w') as f:
            f.write(content)
        print(f"\n✅ Applied {fixes_applied} import fixes to {client_file_path}")
    else:
        print("No changes needed")


if __name__ == "__main__":
    client_path = Path(__file__).parent.parent / "cardsightai" / "client.py"
    fix_imports(str(client_path))
