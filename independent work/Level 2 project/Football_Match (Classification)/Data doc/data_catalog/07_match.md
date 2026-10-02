# Match

## Purpose
Central match-level table containing match identifiers, teams, results, player references, match-event information and betting odds.

## Grain
One row represents one football match.

## Structure
- Rows: 25,979
- Columns: 115
- Duplicate rows: 0
- Core identifiers: no missing values observed

## Keys / identifiers
- `id`: primary key
- `match_api_id`: unique match identifier
- `country_id`: country reference
- `league_id`: league reference
- `home_team_api_id`: home team reference
- `away_team_api_id`: away team reference
- home/away player identifiers: player references

## Main groups of fields

### Match information
`country_id`, `league_id`, `season`, `stage`, `date`, `match_api_id`, home/away team identifiers and home/away goals.

### Player line-up information
Home/away player X and Y positions and home/away player identifiers.

### Match-event/statistics information
`goal`, `shoton`, `shotoff`, `foulcommit`, `card`, `cross`, `corner`, and `possession`.

### Betting odds
Bookmaker-specific home/draw/away odds, including fields such as `B365H`, `B365D`, `B365A`, `PSH`, `PSD`, `PSA`, `WHH`, `WHD`, `WHA`, `VCH`, `VCD`, `VCA`, `GBH`, `GBD`, `GBA`, `BSH`, `BSD`, and `BSA`.

## Relationships
Links to `Country`, `League`, `Team`, and `Player` through their respective identifiers.

## Initial profiling
`match_api_id` was unique and core relationship fields were complete in the inspected profile. Detailed match-statistics fields showed approximately 45% missing values. Several betting-odds fields also showed substantial missingness.

The table has no explicit classification target. A target may need to be derived from available match-result information; this is a modelling decision and is not made in this catalogue.

## Status
Central table for deeper relationship analysis, leakage checks, target definition and feature selection. No fields are being removed at this stage.
