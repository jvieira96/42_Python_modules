#!/usr/bin/env python3


def list_comprehension(player_data):
    print("=== List Comprehension Examples ===")
    high_scores = []
    scores_double = []
    active_players = []
    for player in player_data:
        if player['score'] > 2000:
            high_scores.append(player['name'])
        scores_double.append(player['score'] * 2)
        if player['active']:
            active_players.append(player['name'])
        
    print(f"High scores (>2000): {high_scores}")
    print(f"Scores doubled: {scores_double}")
    print(f"Active players: {active_players}")


def dict_comprehension(player_data):
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {}
    player_achiev = {}
    score_cat = {"high": 0, "medium": 0, "low": 0}
    for player in player_data:
        player_scores[player['name']] = player['score']
        if player['score'] > 2100:
            score_cat['high'] += 1
        elif player['score'] > 2000:
            score_cat['medium'] += 1
        else:
            score_cat["low"] += 1
        player_achiev[player['name']] = player['achievements']
    print(f"Player scores: {player_scores}")
    print(f"Score Categories: {score_cat}")
    print(f"Achievements counts: {player_achiev}")


def set_comprehension(player_data, raw_achievements):
    print("\n=== Set Comprehension Examples ===")
    unique_achiev = set()
    unique_region = set()
    unique_names = set()
    for achiev in raw_achievements:
        unique_achiev.add(achiev)
    for player in player_data:
        unique_names.add(player['name'])
        unique_region.add(player['region'])
    print(f"Unique players: {unique_names}")
    print(f"Unique achievements: {unique_achiev}")
    print(f"Unique regions: {unique_region}")
    

def main():
    print("=== Game Analytics Dashboard ===\n")
    player_data = [
        {"name": "alice", "score": 2300, "achievements": 5, "active": True, "region": "north"},
        {"name": "bob", "score": 1800, "achievements": 3, "active": True, "region": "central"},
        {"name": "charlie", "score": 2150, "achievements": 7, "active": True, "region": "east"},
        {"name": "diana", "score": 2050, "achievements": 4, "active": False, "region": "north"}
    ]
    raw_achievements = ["first_kill", "level_10", "boss_slayer", "first_kill", "level_10"]
    list_comprehension(player_data)
    dict_comprehension(player_data)
    set_comprehension(player_data, raw_achievements)

    print("=== Combined Analysis ===")
    total_players = 0
    unique_achiev = set()
    total_score = 0
    top_performer = {}
    for achiev in raw_achievements:
        unique_achiev = achiev
    for player in player_data:
        total_players += 1
        


if __name__ == "__main__":
    main()
