# Scraping Issues

### src/scraping/automated_scraper.py
- NFL
    - There were a handful of games with no available betting data (~10 per team)
    - These games weren't included in the saved files
    - These games were scattered around, but usually occuring in the earlier seasons (pre 2010) for each team
    - Could be due to insufficient data
- NHL
    - There were some games with no available betting data or no available home/away moneyline betting data (~60 per team)
    - These games weren't included in the saved files
    - These games were scattered around, but almost all of them were concentrated in the earlier pre-2010 seasons
    - Could be due to insufficient moneyline data, and preference of the 1x2 line for NHL as opposed to home/away moneylines
