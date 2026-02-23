def sports_points_table(points):
    # Step 1: Replace negative points with 0
    valid_points = [p if p >= 0 else 0 for p in points]
    
    # Step 2: Sort leaderboard (descending)
    sorted_points = sorted(valid_points, reverse=True)
    
    # Step 3: Find winner and runner-up
    winner = sorted_points[0] if sorted_points else None
    runner_up = sorted_points[1] if len(sorted_points) > 1 else None
    
    # Step 4: Display results
    print("Original Points:", points)
    print("Valid Points (no negatives):", valid_points)
    print("Sorted Leaderboard:", sorted_points)
    print("Winner Points:", winner)
    print("Runner-Up Points:", runner_up)


# Example usage
team_points = [25, -5, 40, 32, 18,-10]
sports_points_table(team_points)