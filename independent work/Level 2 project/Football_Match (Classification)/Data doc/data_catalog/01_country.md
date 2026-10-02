# Country

## Purpose
Reference table containing the countries represented in the dataset.

## Grain
One row represents one country.

## Structure
- Rows: 11
- Columns: 2
- Duplicate rows: 0
- Missing values: 0

## Keys
- `id`: primary key
- `name`: country name

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Country identifier |
| `name` | TEXT | Country name |

## Relationships
Referenced by `League.country_id` and `Match.country_id`.

## Initial profiling
Both columns contain 11 unique values. No missing values or duplicate rows were observed.
