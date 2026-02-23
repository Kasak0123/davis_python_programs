def movie_rating_system(ratings):
    # Step 1: Remove invalid ratings
    valid_ratings = [r for r in ratings if 1 <= r <= 5]
    
    if not valid_ratings:
        return "No valid ratings available."
    
    # Step 2: Find average rating
    average = sum(valid_ratings) / len(valid_ratings)
    
    # Step 3: Count 5-star ratings
    five_star_count = valid_ratings.count(5)
    
    # Step 4: Sort ratings in ascending order
    sorted_ratings = sorted(valid_ratings)
    
    # Step 5: Display results
    print("Original Ratings:", ratings)
    print("Valid Ratings:", valid_ratings)
    print("Average Rating:", round(average, 2))
    print("Number of 5-Star Ratings:", five_star_count)
    print("Sorted Ratings (Ascending):", sorted_ratings)


# Example usage
ratings_list = [5, 4, 3, 6, 2, 5, 0, 1, 5]
movie_rating_system(ratings_list)