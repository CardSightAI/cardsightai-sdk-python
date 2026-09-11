# Changelog

## [2.0.0] - 2026-09-11

### Breaking
- **`CardDetails.parallel` removed.** Card identification and detail responses no longer include a single `parallel` field (`ParallelSummary`). It is replaced by `parallel_suggestions`, a ranked list of `ParallelSuggestion` (best match first). Each entry carries `id`, `name`, `description`, `is_partial`, `numbered_to`, `cards`, and an optional `confidence` (`ParallelSuggestionConfidence`: `HIGH` | `MEDIUM` | `LOW`) — a missing `confidence` means the parallel was not assessed, not that it is low-confidence. **Migration:** replace `card.parallel` with `card.parallel_suggestions[0]` (guarding for an empty/unset list), and read `.confidence` per entry instead of assuming a single value.

### Added
- **Pricing timeseries** endpoint: `client.pricing.get_card_pricing_timeseries(card_id=..., interval=...)` (`GET /v1/pricing/{card_id}/timeseries`) — candlestick-style price rollups bucketed by `interval` (`daily` | `weekly` | `monthly`), with optional `periods`, `as_of_date`, `listing_type`, `parallel_id`, and `grade_id` filters. New response models: `TimeseriesResponse`, `TimeseriesQueryEcho`, `TimeseriesTypeTotals`, `TimeseriesGradeGroup`, `TimeseriesCompanyGroup`, `CandlePeriod`, `CandleStats`, `RawTimeseriesSection`.
- `CardSuggestion` entries now include full card fields (`segment_id`, `release_id`, `set_id`, `year`, `manufacturer`, `release_name`, `set_name`, `name`, `number`, `description`, `numbered_to`, `attributes`, `variation_of`, `fields`) — populated only when detection confidence is Medium or Low.
- `SearchResult` gained optional `segment_name`, `card_number`, and `match_kind` (`SearchResultMatchKind`: `exact` | `fuzzy`).
- `FeedbackResponse.status` (`FeedbackResponseStatus`) gained new values: `new`, `confirmed_bug`, `enhancement_backlog`, `enhancement_planned`, `released`, `not_an_issue`, `closed`. Older values (`duplicate`, `fixed`, `need_info`, `not_reviewed`, `under_review`, `wont_fix`) are deprecated but still present.
- Detections may include a `CARD_LANGUAGE` entry (ISO 639-1 code) in `card.fields`.

### Changed
- Title/catalog search `q` minimum length relaxed from 3 to 2 characters.
- `SearchResult.relevance` is now documented as an opaque, order-only value (not a comparable score).
- Parallel catalog endpoints (`get_parallel`, `get_parallels`) are no longer labelled "(free)" in their descriptions.
- Regenerated the client from the latest OpenAPI spec.

## [1.4.0] - 2026-07-15

### Added
- **Pricing history paging** — `pricing` accepts an optional `as_of_date` query param on `GET /v1/pricing/{card_id}`; results are capped at 500 rows with a non-fatal advisory surfaced in the response `messages` array.
- **Catalog `/N` slash search** — `SearchResult` now carries an optional `numbered_to` field; a standalone `/N` term in the search query hard-filters to items serial-numbered to N.
- **Server advisory messages** — `ServerMessage[]` `messages` arrays added to `PaginatedCardsResponse`, `CatalogSearchResponse`, and `PricingResponse`.

### Changed
- Regenerated the client from the latest OpenAPI spec.

## [1.3.0] - 2026-06-30

### Added
- **Pricing search** endpoint: `client.pricing.search_pricing_by_title(q="...")` — free-text fuzzy search over historical pricing by listing title (`GET /v1/pricing/search`), covering completed auction sales and Buy It Now asking prices, with optional `period`, `listing_type`, and `limit` filters
- **Marketplace search** endpoint: `client.marketplace.search_marketplace_by_title(q="...")` — free-text fuzzy search over active marketplace listings by title (`GET /v1/marketplace/search`), with optional `listing_type` and `limit` filters
- New response models: `PricingSearchResponse`, `PricingSearchRecord`, `MarketplaceSearchResponse`, `MarketplaceSearchRecord`, and shared `SearchMeta`, `SearchMatchedCard`, `CardSetContext`, and `SearchGrade`

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
