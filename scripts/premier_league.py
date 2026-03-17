"""Premier League Results Script
Displays club standings for the 2025-2026 season.
"""

STANDINGS = [
    {"club": "Aston Villa", "rank": "fourth"},
    {"club": "Arsenal", "rank": "first"},
    {"club": "Man City", "rank": "second"},
    {"club": "Man U", "rank": "third"},
]

RANK_MESSAGES = {
    "first": "is Champions of the Premier League Season 2025-2026.",
    "second": "is Vice Champions of the Premier League Season 2025-2026.",
    "third": "finished on the podium of the Premier League Season 2025-2026.",
    "fourth": "finished fourth of the Premier League Season 2025-2026 but qualifies for the UCL.",
}


def display_standings() -> None:
    """Print the Premier League standings."""
    for club in STANDINGS:
        message = RANK_MESSAGES.get(club["rank"], "participated in the league.")
        print(f"{club['club']} {message}")


if __name__ == "__main__":
    display_standings()
