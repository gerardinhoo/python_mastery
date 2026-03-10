"""
Premier League Results Script
Displays club standings for the 2025–2026 season.
"""

premier_league = [
    {"club": "Aston Villa", "rank": "fourth"},
    {"club": "Arsenal", "rank": "first"},
    {"club": "Man City", "rank": "second"},
    {"club": "Man U", "rank": "third"}
]

rank_messages = {
    "first": "is Champions of the Premier League Season 2025-2026.",
    "second": "is Vice Champions of the Premier League Season 2025-2026.",
    "third": "finished on the podium of the Premier League Season 2025-2026.",
    "fourth": "finished fourth of the Premier League Season 2025-2026 but qualifies for the UCL."
}

for club in premier_league:
    message = rank_messages.get(club["rank"], "participated in the league.")
    print(f"{club['club']} {message}")