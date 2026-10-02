# Player_Attributes

## Purpose
Historical player-level attributes, ratings and skill measurements.

## Grain
One row represents a recorded set of player attributes at a particular date.

## Structure
- Rows: 183,978
- Columns: 42
- Duplicate rows: 0
- Missing data: present across multiple attribute fields

## Keys / identifiers
- `id`: primary key
- `player_api_id`: player identifier
- `player_fifa_api_id`: FIFA identifier
- `date`: attribute-record date

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Internal record identifier |
| `player_fifa_api_id` | INTEGER | FIFA player identifier |
| `player_api_id` | INTEGER | Player API identifier |
| `date` | TEXT | Attribute record date |
| `overall_rating` | INTEGER | Overall player rating |
| `potential` | INTEGER | Player potential |
| `preferred_foot` | TEXT | Preferred foot |
| `attacking_work_rate` | TEXT | Attacking work-rate classification |
| `defensive_work_rate` | TEXT | Defensive work-rate classification |
| `crossing`–`gk_reflexes` | INTEGER/REAL | Player skill and goalkeeper attributes |

## Relationships
Links to `Player` through player identifiers.

## Initial profiling
No duplicate rows were observed. Multiple attribute columns contain missing values. Missingness requires further investigation before deciding on treatment.
