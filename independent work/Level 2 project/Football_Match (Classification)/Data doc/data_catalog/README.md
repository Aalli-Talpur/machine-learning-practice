# Football Match Classification — Data Catalogue

This folder documents the structure and initial profiling of the seven project tables in `database.sqlite`.

| Table | Purpose | Rows | Columns |
|---|---|---:|---:|
| Country | Country reference data | 11 | 2 |
| League | League reference data | 11 | 3 |
| Player | Basic player information | 11,060 | 7 |
| Player_Attributes | Historical player attributes and ratings | 183,978 | 42 |
| Team | Basic team information | 299 | 5 |
| Team_Attributes | Historical team attributes | 1,458 | 25 |
| Match | Match-level information, events and betting odds | 25,979 | 115 |

## Catalogue scope

Each table file records its purpose, grain, keys, relationships, columns, data types, and initial profiling observations.

This catalogue describes the data **before cleaning or feature engineering**. It does not decide which fields will be retained, removed, transformed, or used as the ML target.

## Data model

`Match` is the central match-level table. It connects to country, league, teams and players through identifiers. `Player_Attributes` and `Team_Attributes` contain historical records associated with players and teams.

## Profiling status

Initial profiling has been completed for all seven tables. Deeper relationship checks, data-quality investigation, leakage checks, and target definition will follow.

## Reference material

Supporting football-data field definitions are kept separately in the project's reference documentation and should be used alongside this catalogue when interpreting abbreviations.
