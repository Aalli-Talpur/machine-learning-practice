# League

## Purpose
Reference table containing the leagues represented in the dataset.

## Grain
One row represents one league.

## Structure
- Rows: 11
- Columns: 3
- Duplicate rows: 0
- Missing values: 0

## Keys
- `id`: primary key
- `country_id`: foreign key to `Country.id`
- `name`: league name

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | League identifier |
| `country_id` | INTEGER | Country identifier |
| `name` | TEXT | League name |

## Relationships
`country_id` links each league to `Country.id`.

## Initial profiling
All three columns contain 11 unique values. No missing values or duplicate rows were observed.
