"""
Basic usage example for the CardSight AI SDK

This example demonstrates:
- Setting up the client with API key
- Checking API health status
- Getting catalog statistics
- Listing segments and manufacturers
- Searching for cards
- Both synchronous and asynchronous client usage
"""

import asyncio
import os

from cardsightai import AsyncCardSightAI, CardSightAI


def sync_example():
    """Synchronous example of using the CardSight AI SDK"""
    print("=== Synchronous Example ===\n")

    # Initialize the client (API key from environment variable)
    client = CardSightAI()

    try:
        # 1. Check API health
        print("1. Checking API health...")
        health = client.health.get_health()
        print(f"   ✓ API Status: {health.status}")
        print(f"   ✓ Timestamp: {health.timestamp}\n")

        # 2. Get catalog statistics
        print("2. Fetching catalog statistics...")
        stats = client.catalog.get_statistics()
        print(f"   ✓ Total Cards: {stats.cards.total:,}")
        print(f"   ✓ Total Sets: {stats.sets.total:,}")
        print(f"   ✓ Total Releases: {stats.releases.total:,}")
        print(f"   ✓ Total Manufacturers: {stats.manufacturers.total}\n")

        # 3. List segments (sports categories)
        print("3. Fetching segments...")
        segments_response = client.catalog.get_segments()
        segments = getattr(segments_response, 'segments', [])
        print(f"   ✓ Found {len(segments)} segments:")
        for segment in segments[:5]:  # Show first 5
            segment_name = getattr(segment, 'name', 'Unknown')
            print(f"     • {segment_name}")
        print()

        # 4. List manufacturers
        print("4. Fetching manufacturers...")
        mfg_response = client.catalog.get_manufacturers()
        manufacturers = getattr(mfg_response, 'manufacturers', [])
        print(f"   ✓ Found {len(manufacturers)} manufacturers:")
        for mfg in manufacturers[:5]:  # Show first 5
            mfg_name = getattr(mfg, 'name', 'Unknown')
            print(f"     • {mfg_name}")
        print()

        # 5. Get a random card
        print("5. Getting a random card...")
        random_cards = client.catalog.get_random_cards()
        cards = getattr(random_cards, 'cards', [])
        if cards:
            card = cards[0]
            print("   ✓ Random Card:")
            print(f"     • Name: {getattr(card, 'name', 'Unknown')}")
            print(f"     • Set: {getattr(card, 'set_name', 'Unknown')}")
            print(f"     • Release: {getattr(card, 'release_name', 'Unknown')} ({getattr(card, 'release_year', 'Unknown')})")
            print(f"     • Number: {getattr(card, 'number', 'N/A')}")
        print()

        print("✅ All synchronous operations completed successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")


async def async_example():
    """Asynchronous example of using the CardSight AI SDK"""
    print("=== Asynchronous Example ===\n")

    # Initialize the async client using context manager
    async with AsyncCardSightAI() as client:
        try:
            # 1. Check API health
            print("1. Checking API health...")
            health = await client.health.get_health()
            print(f"   ✓ API Status: {health.status}")
            print(f"   ✓ Timestamp: {health.timestamp}\n")

            # 2. Get catalog statistics
            print("2. Fetching catalog statistics...")
            stats = await client.catalog.get_statistics()
            print(f"   ✓ Total Cards: {stats.cards.total:,}")
            print(f"   ✓ Total Sets: {stats.sets.total:,}")
            print(f"   ✓ Total Releases: {stats.releases.total:,}")
            print(f"   ✓ Total Manufacturers: {stats.manufacturers.total}\n")

            # 3. List segments (sports categories)
            print("3. Fetching segments...")
            segments_response = await client.catalog.get_segments()
            segments = getattr(segments_response, 'segments', [])
            print(f"   ✓ Found {len(segments)} segments:")
            for segment in segments[:5]:  # Show first 5
                segment_name = getattr(segment, 'name', 'Unknown')
                print(f"     • {segment_name}")
            print()

            # 4. List manufacturers
            print("4. Fetching manufacturers...")
            mfg_response = await client.catalog.get_manufacturers()
            manufacturers = getattr(mfg_response, 'manufacturers', [])
            print(f"   ✓ Found {len(manufacturers)} manufacturers:")
            for mfg in manufacturers[:5]:  # Show first 5
                mfg_name = getattr(mfg, 'name', 'Unknown')
                print(f"     • {mfg_name}")
            print()

            # 5. Get a random card
            print("5. Getting a random card...")
            random_cards = await client.catalog.get_random_cards()
            cards = getattr(random_cards, 'cards', [])
            if cards:
                card = cards[0]
                print("   ✓ Random Card:")
                print(f"     • Name: {getattr(card, 'name', 'Unknown')}")
                print(f"     • Set: {getattr(card, 'set_name', 'Unknown')}")
                print(f"     • Release: {getattr(card, 'release_name', 'Unknown')} ({getattr(card, 'release_year', 'Unknown')})")
                print(f"     • Number: {getattr(card, 'number', 'N/A')}")
            print()

            print("✅ All asynchronous operations completed successfully!")

        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    """Run both sync and async examples"""
    # Check if API key is set
    if not os.getenv("CARDSIGHTAI_API_KEY"):
        print("❌ Error: CARDSIGHTAI_API_KEY environment variable not set")
        print("   Please set it with: export CARDSIGHTAI_API_KEY='your_api_key_here'")
        print()
        print("   Don't have an API key? Get one at:")
        print("   https://cardsight.ai/signup")
        return

    print("CardSight AI SDK - Basic Usage Examples")
    print("=" * 50)
    print()

    # Run synchronous example
    sync_example()

    print("\n" + "=" * 50 + "\n")

    # Run asynchronous example
    asyncio.run(async_example())

    print("\n" + "=" * 50)
    print("\n🎉 All examples completed!")
    print("\nNext steps:")
    print("  • Read the docs: https://github.com/CardSightAI/cardsightai-sdk-python")
    print("  • API reference: https://api.cardsight.ai/documentation")


if __name__ == "__main__":
    main()
