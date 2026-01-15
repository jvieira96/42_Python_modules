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
        player_achiev[player['name']] = player['achievements_number']
    print(f"Player scores: {player_scores}")
    print(f"Score Categories: {score_cat}")
    print(f"Achievements counts: {player_achiev}")


def set_comprehension(player_data):
    print("\n=== Set Comprehension Examples ===")
    unique_achiev = set()
    unique_region = set()
    unique_names = set()
    for player in player_data:
        unique_names.add(player['name'])
        unique_region.add(player['region'])
        unique_achiev.update(player['achievements'])
    print(f"Unique players: {unique_names}")
    print(f"Unique achievements: {unique_achiev}")
    print(f"Unique regions: {unique_region}")


def main():
    print("=== Game Analytics Dashboard ===\n")
    player_data = [
        {"name": "alice", "score": 2300, "achievements_number": 5, "active": True, "region": "north", "achievements" : ["first_kill", "level_10", "boss_slayer", "max_level", "most_damage"]},
        {"name": "bob", "score": 1800, "achievements_number": 3, "active": True, "region": "central", "achievements" : ["heavy_hitter", "level_10", "low_health"]},
        {"name": "charlie", "score": 2150, "achievements_number": 7, "active": True, "region": "east", "achievements" : ["first_kill", "level_10", "boss_slayer", "first_kill", "level_10", "rampage", "legendary_loot"]},
        {"name": "diana", "score": 2050, "achievements_number": 4, "active": False, "region": "north", "achievements" : ["first_kill", "boss_slayer", "first_kill", "team_carry"]}
    ]
    list_comprehension(player_data)
    dict_comprehension(player_data)
    set_comprehension(player_data)

    print("\n=== Combined Analysis ===")
    total_players = 0
    unique_achiev = set()
    total_score = 0
    top_performer = {"name": None, "score": 0, "achievements": 0}
    for player in player_data:
        total_players += 1
        unique_achiev.update(player['achievements'])
        total_score += player['score']
        if player['score'] > top_performer['score']:
            top_performer['name'] = player['name']
            top_performer['score'] = player['score']
            top_performer['achievements'] = player['achievements_number']
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_achiev)}")
    print(f"Average score: {total_score / total_players}")
    print(f"Top performer: {top_performer['name']} ({top_performer['score']} points, {top_performer['achievements']} achievements)")

if __name__ == "__main__":
    main()
