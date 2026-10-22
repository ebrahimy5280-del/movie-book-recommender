import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N_ITEMS = 20
STEPS = 50
RUNS = 100
GENRES = ["Action", "Sci-Fi", "Drama", "Fantasy", "Comedy"]

def simulate(agent_type, seed):
    rng = np.random.default_rng(seed)
    item_genres = rng.choice(GENRES, size=N_ITEMS)
    user_favorites = {"Sci-Fi", "Drama"}
    user_profile_model = {genre: 0 for genre in GENRES}
    
    score = 0
    last_feedback = None
    
    for step in range(STEPS):
        if agent_type == "random":
            recommended_item = rng.integers(0, N_ITEMS)
            
        elif agent_type == "reflex":
            if last_feedback and last_feedback["liked"]:
                matching_items = [idx for idx, g in enumerate(item_genres) if g == last_feedback["genre"]]
                recommended_item = rng.choice(matching_items) if matching_items else rng.integers(0, N_ITEMS)
            else:
                recommended_item = rng.integers(0, N_ITEMS)
                
        elif agent_type == "model":
            best_genre = max(user_profile_model, key=user_profile_model.get)
            matching_items = [idx for idx, g in enumerate(item_genres) if g == best_genre]
            
            if matching_items and user_profile_model[best_genre] > 0:
                recommended_item = rng.choice(matching_items)
            else:
                recommended_item = rng.integers(0, N_ITEMS)
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        recommended_genre = item_genres[recommended_item]
        user_liked = (recommended_genre in user_favorites)
        
        if user_liked:
            score += 1.0
            if agent_type == "model":
                user_profile_model[recommended_genre] += 1
        else:
            score -= 0.2
            if agent_type == "model":
                user_profile_model[recommended_genre] = max(0, user_profile_model[recommended_genre] - 0.5)
                
        last_feedback = {"genre": recommended_genre, "liked": user_liked}
        
    return score

if __name__ == "__main__":
    rows = []
    agent_types = ["random", "reflex", "model"]
    
    for agent in agent_types:
        for seed in range
