# Issues

### src/scraping/automated_scraper.py
- There were a handful of games with no available betting data (~10 per team); these games weren't included in the saved file
- These games were scattered around, but usually occuring in the earlier seasons (pre 2010) for each team
- Could be due to insufficient data or OddsPortal bugs

### src/scraping/espn_id_scraping/espn_mlb.py
- PIT STL 22-07-2019 (game does not exist on ESPN)
    - espn_id left as default (000000000)
    - game_type manually corrected to 2nd_half
- NYY DET 01-10-2011 (game date on ESPN was 30-09-2011)
    - Kept OddsPortal date
    - Corrected espn_id manually
    - Corrected game_type manually
- PHI TB 29-10-2008 (game date on ESPN was 27-10-2008)
    - Kept OddsPortal date
    - Corrected espn_id manually
    - Corrected game_type manually
- COL WSH 06-08-2008 (game date on ESPN was 07-08-2008)
    - There were two games between COL and WSH, one on 07-08-2008 and one on 06-08-2008
    - OddsPortal listed it correctly, but ESPN listed them both on 07-08-2020
    - Kept OddsPortal date
    - Corrected espn_id manually
    - Corrected game_type manually

### src/scraping/espn_id_scraping/espn_nba.py
- There are a total of 114 games from the 2019-2020 NBA season across all teams that are listed on OddsPortal, but not at ESPN
    - Kept their default null espn_id value (000000000)
    - Manually corrected game_type to be regular_season

### src/scraping/espn_id_scraping/espn_nfl.py
- WSH SF 31-12-2023 (ESPN had the date listed as TBD-Flex Game)
    - Kept OddsPortal date
    - Corrected espn_id manually
    - Corrected game_type manually

### src/scraping/espn_id_scraping/espn_nhl.py
- OddsPortal lists 12 regular season games that all happened at the end of July 2020 (28th-30th), but ESPN has no record of these games
    - Usually, the NHL regular season ends in April and the post season begins in April
    - In 2020, because of the pandemic, regular season games after March were cancelled and the postseason was delayed until August
    - OddsPortal lists 12 total regular season games that supposedly happened right before the delayed postseason, but ESPN does not list these
    - Kept default espn_id value (000000000)
    - Corrected game_type to be regular_season manually
- NJ TB 10-01-2010 (listed as January 10th on OddsPortal, but listed as January 8th on ESPN)
    - Kept OddsPortal date
    - Corrected espn_id manually
    - Corrected game_type manually

