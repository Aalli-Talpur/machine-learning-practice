# Player

## Purpose
Reference table containing basic player information.

## Grain
One row represents one player.

## Structure
- Rows: 11,060
- Columns: 7
- Duplicate rows: 0
- Missing values: 0

## Keys
- `id`: primary key
- `player_api_id`: unique player API identifier
- `player_fifa_api_id`: FIFA identifier

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Internal player identifier |
| `player_api_id` | INTEGER | Player API identifier |
| `player_name` | TEXT | Player name |
| `player_fifa_api_id` | INTEGER | FIFA API identifier |
| `birthday` | TEXT | Player date of birth |
| `height` | REAL | Player height |
| `weight` | INTEGER | Player weight |

## Relationships
Player identifiers are referenced by player-related fields in `Match` and by `Player_Attributes`.

## Initial profiling
No missing values or duplicate rows were observed. Identifier fields were unique in the initial profile. `player_name` was not completely unique.
