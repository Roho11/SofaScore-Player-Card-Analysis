Football Match Analyzer for Player Card Betting

Welcome to my first personal Python project that I'm excited to share. As someone who's been diving into Python, particularly web scraping and data analysis with libraries like pandas, I've created a tool that caters to my interest in systematic player card betting in football (soccer) matches. This project is made just for fun and for learning purposes.

Project Overview

This project serves as a Web Scraper and Analyzer tailored for football matches sourced from SofaScore. During my free time, I've developed a penchant for making calculated bets on player cards. While I initially followed betting tips on platforms like Twitter, I found the idea of creating my own model both intriguing and empowering. And thus, this project came into being.

What the Model Does

Data Collection: The getgames.py script scrapes SofaScore for matches scheduled on the current day. It focuses on fetching games from notable leagues such as the Premier League, Champions League, La Liga, and Serie A (aligned with my preferences). The script requires a valid date specified in check_game_date.txt, which the model uses to determine the last accessed date. The output is a comprehensive CSV file containing game data and referee Card per Game (CPG) statistics.
Game Analysis: The model subsequently traverses through the collected games and verifies if the lineups have been confirmed. Confirmation typically occurs an hour before kickoff. Once lineup confirmation is obtained, the model generates individual XLSX files for each match. These files contain essential player statistics pertinent to card betting, including fouls per game, tackles per game, and cards per game.
In-depth Analysis: The GameAnalysis.py script steps in to analyze the match-specific XLSX files. Leveraging fundamental statistics, it identifies significant mean outliers within the match and presents the top 9 players accordingly.
Betting Strategy: Armed with insights, I wager 2% of my account balance on each match. My betting strategy usually involves crafting mixed player bets and engaging in some ambitious double-double longshots. These decisions are guided by the analysis from the XLSX files and the lineup data.
Automation and Frequency

To ensure that my model is as up-to-date as possible, I've scheduled it to run on a 15-minute interval using crontab. This ensures that I have access to the latest game information and statistics for informed betting decisions.

Feel free to explore the scripts, adapt the model to your preferences, or provide feedback. While my model has served my personal interests, remember that betting entails risks, and responsible gambling is essential.

Developed by [Your Name]
