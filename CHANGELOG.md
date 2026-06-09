# Changelog

## [1.2.0] - 2026-06-08

### Added
- **Pricing** endpoints: `client.pricing.get_card_pricing(card_id=...)` for completed-sales data (raw + graded) and `client.pricing.get_bulk_pricing(body=...)` for up to 100 cards in one request
- **Marketplace** endpoint: `client.marketplace.get_card_marketplace(card_id=...)` for active listings grouped by grading company and grade
- **Population** endpoints: `client.population.get_card_population(card_id=...)`, `get_set_population(set_id=...)`, and `get_release_population(release_id=...)` for graded census reports
- **Release Calendar** endpoint: `client.release_calendar.get_release_calendar(...)` for upcoming and recent product releases
- **Catalog Fields** endpoints: `client.catalog.get_fields(...)` and `client.catalog.get_field_by_id(id=...)` for browsing flexible metadata fields (HP, Rarity, Artist, Mana Cost, etc.) with usage counts
- **Set identifiability** pre-flight checks: `client.card_identification.list_identifiable_sets(...)` and `client.card_identification.check_set_identifiable(set_id=...)`
- `client.detect` alias for the card-detection module (`client.detect.detect_card(...)`), matching the Node SDK
- New response models including `PricingResponse`, `BulkPricingResponse`, `MarketplaceResponse`, `CardPopulationResponse`, `SetPopulationResponse`, `ReleasePopulationResponse`, `PaginatedReleaseCalendarResponse`, `PaginatedFieldsResponse`, `DetailedFieldResponse`, `IdentifiableSetsResponse`, and `SetIdentifiableResponse`

### Changed
- Enriched card identification responses: detections now expose `fields` (flexible metadata), `numbered_to` (print run for numbered base cards), `suggestions` (alternative reprint candidates), and richer slab grading (`grade`, qualifier, and autograph grade)
- Refactored collection analytics and breakdown response models to match the updated API schema

### Removed
- `client.health.get_detailed_health()` — the `GET /v1/health/detailed` endpoint was removed from the API

## [1.1.0] - 2026-03-09

### Added
- Global catalog search endpoint (`client.catalog.search_catalog(q="...")`) for fuzzy search across cards, sets, releases, and parallels
- Grading company detection in card identification responses (`detection.grading`) with company name and confidence level
- New models: `CatalogSearchResponse`, `SearchResult`, `SearchResultType`, `SearchCatalogType`, `SlabCompany`, `SlabGradingDetail`, `SlabGradingDetailConfidence`

## [1.0.0] - 2025-02-26

### Added
- Initial public release
- Full API coverage for all CardSight AI endpoints
- Sync and async client support
- Card identification with file upload helpers
- Card detection endpoint support
- Segment-specific identification
- Lazy-loaded API module proxies
- Complete type hints (PEP 561)
