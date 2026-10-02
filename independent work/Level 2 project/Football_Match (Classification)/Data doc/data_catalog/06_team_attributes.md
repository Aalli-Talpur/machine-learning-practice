# Team_Attributes

## Purpose
Historical team-level attributes describing playing style and team characteristics.

## Grain
One row represents a recorded set of team attributes at a particular date.

## Structure
- Rows: 1,458
- Columns: 25
- Duplicate rows: 0
- Missing data: concentrated in `buildUpPlayDribbling`

## Keys / identifiers
- `id`: primary key
- `team_api_id`: team identifier
- `team_fifa_api_id`: FIFA identifier
- `date`: attribute-record date

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Internal record identifier |
| `team_fifa_api_id` | INTEGER | FIFA team identifier |
| `team_api_id` | INTEGER | Team API identifier |
| `date` | TEXT | Attribute-record date |
| `buildUpPlaySpeed`–`defenceDefenderLineClass` | INTEGER/TEXT | Team playing-style and tactical attributes |

## Relationships
Links to `Team` through team identifiers.

## Initial profiling
No duplicate rows were observed. `buildUpPlayDribbling` has approximately 66% missing values; the other profiled columns were complete. The `id` column is unique while team identifiers repeat across historical records.
