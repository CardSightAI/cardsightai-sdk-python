# CardSight AI Python SDK

![PyPI Version](https://img.shields.io/pypi/v/cardsightai)
![Python Version](https://img.shields.io/pypi/pyversions/cardsightai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Type Hints](https://img.shields.io/badge/Type_Hints-Complete-blue.svg)](https://docs.python.org/3/library/typing.html)

**Official Python SDK for [CardSight AI](https://cardsight.ai) REST API**

The most comprehensive trading card identification and collection management platform.
**6M+ Cards** • **Baseball, Football, Basketball** • **AI-Powered Recognition** • **Free Tier Available**

**Quick Links:** [Getting Started](https://github.com/CardSightAI/cardsightai-sdk-python#getting-started) • [Installation](https://github.com/CardSightAI/cardsightai-sdk-python#installation) • [Examples](https://github.com/CardSightAI/cardsightai-sdk-python#usage-examples) • [API Documentation](https://cardsight.ai/documentation/api-reference) • [Support](https://cardsight.ai/support)

---

## Features

- **Full Type Safety** - Complete type hints with auto-generated types from OpenAPI
- **Multi-Card Detection** - Identify multiple cards in a single image with confidence scores
- **Async & Sync Support** - Use asyncio or traditional synchronous code
- **Smart Error Handling** - Custom exception hierarchy with detailed error information
- **Minimal Dependencies** - Only essential packages (httpx, attrs, python-dotenv)
- **6M+ Cards** - Baseball, Football, and Basketball. Hockey and TCG (Pokemon, Magic: The Gathering, Yu-Gi-Oh!, One Piece) coming soon
- **100% API Coverage** - All CardSight AI endpoints fully implemented
- **Auto-Generated** - Always up-to-date with the latest API changes

## Key Capabilities

| Feature | Description | Primary Methods |
|---------|-------------|-----------------|
| **Card Identification** | Identify multiple cards from images using AI | `identify.identify()` |
| **Card Detection** | Detect cards in images | `detect.detect()` |
| **Global Search** | Fuzzy search across cards, sets, releases, parallels | `catalog.search_catalog(q="...")` |
| **Catalog Search** | Search 6M+ trading cards database | `catalog.get_cards()`, `catalog.get_sets()` |
| **Random Catalog** | Pack opening simulations with parallel odds | `catalog.get_random_cards()`, `catalog.get_random_sets()` |
| **Collections** | Manage owned card collections with analytics | `collections.create_collection()`, `collections.add_collection_cards()` |
| **Collectors** | Manage collector profiles | `collectors.create_collector()`, `collectors.update_collector()` |
| **Lists** | Track wanted cards (wishlists) | `lists.create_list()`, `lists.add_cards_to_list()` |
| **Binders** | Organize collection subsets | `collections.create_binder()` |
| **Grading** | PSA, BGS, SGC grade information | `grades.get_grading_companies()` |
| **AI Search** | Natural language queries | `ai.process_ai_query()` |
| **Autocomplete** | Search suggestions for all entities | `autocomplete.autocomplete_cards()` |

## Requirements

- Python 3.10+ (uses modern type hints and async features)
- API Key from [cardsight.ai](https://cardsight.ai) (free tier available)

## Installation

```bash
# pip
pip install cardsightai

# poetry
poetry add cardsightai

# pipenv
pipenv install cardsightai
```

## Getting Started

### Get Your Free API Key

Get started in minutes with a **free API key** from [cardsight.ai](https://cardsight.ai) - no credit card required!

### Quick Start (< 5 minutes)

```python
from cardsightai import CardSightAI

# 1. Initialize the client (auto-detects CARDSIGHTAI_API_KEY env var)
client = CardSightAI(api_key='your_api_key_here')

# 2. Identify a card from an image
result = client.identify.identify('path/to/card.jpg')

# 3. Access the identification results
if result and hasattr(result, 'detections'):
    # The API can detect multiple cards in a single image
    detection = result.detections[0] if result.detections else None
    if detection and detection.card:
        print(f"Card: {detection.card.name}")
        print(f"Confidence: {detection.confidence}")  # "High", "Medium", or "Low"
        print(f"Total cards detected: {len(result.detections)}")
```

**Async Version:**

```python
import asyncio
from cardsightai import AsyncCardSightAI

async def main():
    async with AsyncCardSightAI() as client:
        result = await client.identify.identify('path/to/card.jpg')
        if result and hasattr(result, 'detections'):
            detection = result.detections[0] if result.detections else None
            if detection:
                print(f"Card: {detection.card.name}")

asyncio.run(main())
```

That's it! The SDK handles all API communication, type safety, and error handling automatically.

## Usage Examples

### Card Identification

The identification endpoint uses AI to detect trading cards in images. It can identify multiple cards in a single image and returns confidence levels for each detection.

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Identify from file path
result = client.identify.identify('card_image.jpg')

# Or from bytes
with open('card_image.jpg', 'rb') as f:
    result = client.identify.identify(f.read())

# Process results
for detection in result.detections:
    print(f"Card: {detection.card.name}")
    print(f"Set: {detection.card.set_name}")
    print(f"Confidence: {detection.confidence}")
    print(f"Year: {detection.card.year}")
    print("---")
```

#### Grading Detection

When a card is inside a graded slab, the API automatically detects the grading company:

```python
result = client.identify.identify('graded_card.jpg')
for detection in result.detections:
    if hasattr(detection, 'grading') and detection.grading:
        print(f"Graded by: {detection.grading.company.name}")
        print(f"Grading confidence: {detection.grading.confidence}")
```

#### Response Structure

Each detection includes:
- `confidence`: "High", "Medium", or "Low"
- `card`: Full card details including name, set, year, attributes, pricing
- `grading`: (optional) Grading company and confidence when card is in a slab
- `set`: Set information
- `release`: Release information
- `manufacturer`: Manufacturer details

### Working with Identification Results

Use the included utility function to get the best match. Note that `get_highest_confidence_detection` works with dict-style data — convert response objects as needed:

```python
from cardsightai import CardSightAI
from cardsightai.extras import get_highest_confidence_detection

client = CardSightAI()
result = client.identify.identify('card.jpg')

# get_highest_confidence_detection works with dicts/lists of dicts
# If your result is an attrs response object, access detections directly:
if result and hasattr(result, 'detections') and result.detections:
    best = result.detections[0]  # Already sorted by confidence from the API
    print(f"Best match: {best.card.name} ({best.confidence})")
```

### Catalog Operations

Search and browse the comprehensive card catalog:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Get catalog statistics
stats = client.catalog.get_statistics()
print(f"Total cards: {stats.cards.total:,}")
print(f"Total sets: {stats.sets.total:,}")
print(f"Total releases: {stats.releases.total:,}")

# List segments (Sports, Entertainment, Gaming)
segments = client.catalog.get_segments()
for segment in segments.segments:
    print(f"Segment: {segment.name}")

# List manufacturers
manufacturers = client.catalog.get_manufacturers()
for manufacturer in manufacturers.manufacturers[:10]:
    print(f"Manufacturer: {manufacturer.name}")

# Search releases with pagination
releases = client.catalog.get_releases(
    take=20,
    skip=0,
    sort='year',
    order='desc'
)

# Get specific card details
card = client.catalog.get_card(id='card-uuid-here')
print(f"Card: {card.name}")
print(f"Raw price: ${card.prices.raw}")
print(f"PSA 10 price: ${card.prices.psa_10}")
```

### Global Search

Search across cards, sets, releases, and parallels with fuzzy matching:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Basic search
results = client.catalog.search_catalog(q="Mike Trout", take=10)
for result in results.results:
    print(f"{result.type_}: {result.name} (relevance: {result.relevance})")

# Filter by type
from cardsightai.generated.card_sight_ai_api_client.models import SearchCatalogType
results = client.catalog.search_catalog(q="Topps Chrome", type_=SearchCatalogType.SET)

# Filter by year range
results = client.catalog.search_catalog(q="rookie", min_year="2020", max_year="2024")
```

### Random Catalog (Pack Opening & Discovery)

Simulate pack opening with weighted odds:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Get random cards (like opening a pack)
random_cards = client.catalog.get_random_cards(take=10)
for card in random_cards.cards:
    print(f"Pulled: {card.name} - ${card.prices.raw}")

# Get random release
random_release = client.catalog.get_random_releases()
print(f"Release: {random_release.name} ({random_release.year})")

# Get random set
random_set = client.catalog.get_random_sets()
print(f"Set: {random_set.name}")
```

### Collection Management

Manage your card collections with full CRUD operations:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Create a collection
collection = client.collections.create_collection(name="My Baseball Cards")

# Add cards to collection
client.collections.add_collection_cards(
    collection_id=collection.id,
    card_id='card-uuid',
    quantity=1,
    condition='Near Mint',
    purchase_price=50.00,
    purchase_date='2024-01-15'
)

# Get collection analytics
analytics = client.collections.get_collection_analytics(collection_id=collection.id)
print(f"Total value: ${analytics.total_value}")
print(f"Total cards: {analytics.total_cards}")

# List all cards in collection
cards = client.collections.get_collection_cards(collection_id=collection.id)
```

### Binders (Collection Organization)

Organize collections into binders:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Create a binder within a collection
binder = client.collections.create_binder(
    collection_id='collection-uuid',
    name='Rookie Cards',
    description='All my rookie cards'
)

# Add cards to binder
client.collections.add_card_to_binder(
    collection_id='collection-uuid',
    binder_id=binder.id,
    card_id='card-uuid'
)
```

### Lists (Want Lists / Wishlists)

Track cards you want to acquire:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Create a want list
want_list = client.lists.create_list(name="Cards I Want")

# Add cards to the list
client.lists.add_cards_to_list(
    list_id=want_list.id,
    card_id='card-uuid',
    max_price=100.00
)

# View your want list
cards = client.lists.get_list_cards(list_id=want_list.id)
```

### Grading Information

Access grading company data:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# List grading companies
companies = client.grades.get_grading_companies()
for company in companies:
    print(f"Company: {company.name}")

# Get grade types for a company
types = client.grades.get_grading_types(company_id='psa-uuid')

# Get specific grades
grades = client.grades.get_grades(
    company_id='psa-uuid',
    type_id='numeric-uuid'
)
```

### AI-Powered Search

Use natural language to search the catalog:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Natural language query
results = client.ai.process_ai_query("Find me Mickey Mantle rookie cards")
for result in results:
    print(f"Found: {result.card.name}")
```

### Autocomplete

Get search suggestions for improved UX:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Autocomplete for cards
suggestions = client.autocomplete.autocomplete_cards(query="Mike Trout")

# Autocomplete for manufacturers
manufacturers = client.autocomplete.autocomplete_manufacturers(query="Top")

# Autocomplete for sets
sets = client.autocomplete.autocomplete_sets(query="Chrome")
```

### Image Retrieval

Get card images from the catalog:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Get card image
image = client.images.get_card_image(card_id='card-uuid')
```

### Feedback System

Submit feedback to improve the platform:

```python
from cardsightai import CardSightAI

client = CardSightAI()

# Submit feedback on a card identification
client.feedback.submit_identify_feedback(
    identification_id='id-uuid',
    feedback='Incorrect card identified',
    correct_card_id='actual-card-uuid'
)

# Submit general feedback
client.feedback.submit_general_feedback(
    feedback='Great API!',
    category='positive'
)
```

## Async/Await Support

The SDK provides full async support with `AsyncCardSightAI`:

```python
import asyncio
from cardsightai import AsyncCardSightAI

async def main():
    async with AsyncCardSightAI() as client:
        # All methods are async
        stats = await client.catalog.get_statistics()
        print(f"Total cards: {stats.cards.total:,}")

        segments = await client.catalog.get_segments()
        for segment in segments.segments:
            print(f"Segment: {segment.name}")

        # Concurrent requests
        results = await asyncio.gather(
            client.catalog.get_cards(take=10),
            client.catalog.get_sets(take=10),
            client.catalog.get_releases(take=10)
        )

asyncio.run(main())
```

## Type Hints Support

The SDK includes complete type hints for excellent IDE support:

```python
from cardsightai import CardSightAI
from cardsightai.generated.card_sight_ai_api_client.models import (
    GetV1CatalogCardsResponse200,
    GetV1CatalogStatisticsResponse200
)

client = CardSightAI()

# Full type inference
stats: GetV1CatalogStatisticsResponse200 = client.catalog.get_statistics()
cards: GetV1CatalogCardsResponse200 = client.catalog.get_cards()
```

## Error Handling

The SDK defines custom exception classes for structured error handling:

```python
from cardsightai import CardSightAI
from cardsightai.exceptions import (
    CardSightAIError,
    AuthenticationError,
    RateLimitError,
    APIError
)

client = CardSightAI()

try:
    result = client.identify.identify('card.jpg')
except AuthenticationError as e:
    print(f"Invalid API key: {e.message}")
except RateLimitError as e:
    print(f"Rate limit exceeded. Retry after {e.retry_after} seconds")
except APIError as e:
    print(f"API error ({e.status_code}): {e.message}")
    print(f"Request ID: {e.request_id}")
except CardSightAIError as e:
    print(f"General error: {e.message}")
```

> **Note:** The current SDK passes through response objects from the generated client layer.
> HTTP errors are returned as typed error response objects rather than raised as exceptions.
> The exception classes above are available for use in your own error-handling logic or for
> future SDK versions that may raise them automatically.

## Configuration

Customize client behavior:

```python
from cardsightai import CardSightAI

client = CardSightAI(
    api_key='your_api_key',              # Or use CARDSIGHTAI_API_KEY env var
    base_url='https://api.cardsight.ai',  # Default
    timeout=30.0,                         # Request timeout in seconds
)
```

## Environment Variables

The SDK supports environment variables for configuration:

```bash
# Required
export CARDSIGHTAI_API_KEY='your_api_key_here'

# Optional overrides
export CARDSIGHTAI_BASE_URL='https://api.cardsight.ai'
export CARDSIGHTAI_TIMEOUT='30'
```

Then initialize without parameters:

```python
from cardsightai import CardSightAI

# Automatically uses CARDSIGHTAI_API_KEY
client = CardSightAI()
```

## API Endpoint Coverage

The SDK provides complete coverage of all CardSight AI endpoints:

| Category | Endpoints | Status |
|----------|-----------|--------|
| Card Identification | `POST /v1/identify/card`, `POST /v1/identify/card/{segment}` | ✅ |
| Card Detection | `POST /v1/detect/card` | ✅ |
| Global Search | `GET /v1/catalog/search` - fuzzy search across all entities | ✅ |
| Catalog | Statistics, Segments, Manufacturers, Releases, Sets, Cards | ✅ |
| Random Catalog | Random cards, sets, releases | ✅ |
| Collections | Full CRUD, analytics, cards | ✅ |
| Binders | Create, update, delete, cards | ✅ |
| Lists | Create, update, delete, cards | ✅ |
| Collectors | Create, update, delete | ✅ |
| Grading | Companies, types, grades | ✅ |
| AI Search | Natural language queries | ✅ |
| Autocomplete | Cards, sets, releases, manufacturers, segments | ✅ |
| Images | Card image retrieval | ✅ |
| Feedback | Identification, general, entity feedback | ✅ |
| Subscription | Subscription management | ✅ |
| Health | API health check | ✅ |

## Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/CardSightAI/cardsightai-sdk-python.git
cd cardsightai-sdk-python

# Install dependencies
poetry install

# Run tests
poetry run pytest

# Build package
poetry build
```

### Regenerating from OpenAPI

The SDK auto-generates from the OpenAPI specification:

```bash
# Regenerate client code
make regenerate

# Or manually
poetry run python scripts/generate_client.py
```

### Testing

```bash
# Run all tests
make test

# Run specific tests
poetry run pytest tests/unit/

# Run with coverage
poetry run pytest --cov=cardsightai --cov-report=html
```

### Code Quality

```bash
# Lint code
make lint

# Format code
make format

# Type check
poetry run mypy cardsightai/
```

## Python Version Support

The SDK supports Python 3.10 and later. We test against:

- Python 3.10
- Python 3.11
- Python 3.12

## Dependencies

The SDK has minimal runtime dependencies:

- `httpx` - Modern HTTP client with async support
- `attrs` - Python classes without boilerplate
- `python-dateutil` - Date/time utilities
- `python-dotenv` - Environment variable management
- `typing-extensions` - Backported type hints

## Support

- **Documentation**: [api.cardsight.ai/documentation](https://api.cardsight.ai/documentation)
- **Issues**: [GitHub Issues](https://github.com/CardSightAI/cardsightai-sdk-python/issues)
- **Email**: support@cardsight.ai
- **Discord**: [Join our community](https://discord.gg/cardsightai)

## License

This SDK is released under the [MIT License](LICENSE).

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history and changes.

---

*Made with love by CardSight AI, Inc.*
