# SofaScorePlayerCardAnalysis

This is my first personal python project that I think is 'big' enough to upload. I've been learning python for some time now - mostly web scraping, pandas and so on. 

This project is a Web Scraper / Analyser for Football (Soccer) matches from SofaScore. In my free time i like to systematically bet on player cards. I started folowing some tips on twitter but got realy excited about doing my own 'model', so here it is.

WHAT THE MODEL DOES:

1. getgames.py scrapes SofaScore for all games thar are played {today} and scrapes only games from the Premier League, Champions League, La Liga and Serie A (just my preference). You need a valid date in the file check_game_date.txt which the model reads for the last read date.
2. It retuns a csv file with all the game data and referee CPG (Card per game) stat.
3. Then the model loops through the games and checks if the lineups have been confirmed yet (usually one hour before kick off).
4. If the lineups are confirmed it makes an xslx file per match of important player stats for card betting (fouls per game, tackles per game, cards per game,...)
5. The next step is in GameAnalysis.py. The model reads the match xlsx file and on some basic stats finds the biggest mean outliners in the match and returns the top 9 players.

After that i bet 2% of my account balance per match. Mostly I build 2-3 mixed player bets and some double double longshots. I base my decision on the xslx analysis and the xlsx lineup.

I've got this model running on crontab every 15 minutes.
