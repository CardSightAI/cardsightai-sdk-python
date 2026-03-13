# Changelog

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
