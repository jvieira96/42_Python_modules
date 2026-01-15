#!/usr/bin/env python3

import sys

def score_analytics():
    string_scores = sys.argv
    scores_count = len(string_scores) - 1
    scores = []

    print("=== Player Score Analytics ===")
    if not scores_count:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for i in range (1, len(string_scores)):
                scores.append(int(string_scores[i]))
            print(f"Scores processed: {scores}")
            print(f"Total players: {scores_count}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / scores_count}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    score_analytics()
