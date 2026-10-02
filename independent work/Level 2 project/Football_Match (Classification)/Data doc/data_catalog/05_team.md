# Team

## Purpose
Reference table containing basic team information.

## Grain
One row represents one team.

## Structure
- Rows: 299
- Columns: 5
- Duplicate rows: 0
- Missing values: 11 in `team_fifa_api_id`

## Keys
- `id`: primary key
- `team_api_id`: team API identifier
- `team_fifa_api_id`: FIFA team identifier

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Internal team identifier |
| `team_api_id` | INTEGER | Team API identifier |
| `team_fifa_api_id` | INTEGER | FIFA team identifier |
| `team_long_name` | TEXT | Full team name |
| `team_short_name` | TEXT | Short team name |

## Relationships
Team identifiers are referenced by `Match` and `Team_Attributes`.

## Initial profiling
No duplicate rows were observed. `team_fifa_api_id` contains 11 missing values. Identifier and name fields are not all unique.
