"""Testing the scikit-learn api for matching"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Example list of all possible hobbies
all_hobbies = ["reading", "traveling", "movies", "music", "photography"]
all_hobbies = sorted(all_hobbies)

# Example users
user_1 = {
    "hobbies": ["reading", "traveling", "movies"]
}

all_users = [
    {
        "name": "User 2",
        "hobbies": ["reading", "traveling", "movies"]
    },
    {
        "name": "User 3",
        "hobbies": ["reading", "movies", "photography"]
    },
    {
        "name": "User 4",
        "hobbies": ["traveling", "music"]
    }
]

# Function to generate hobby vectors
def get_hobby_vector(hobbies):
    #hobbies = sorted(hobbies)
    vector: list[float] = []
    for hobby in all_hobbies:
        if hobby in hobbies:
            vector.append(1)
        else:
            vector.append(0)
    return vector

# Convert User 1's hobbies into a feature vector
user_1_features = np.array(get_hobby_vector(user_1["hobbies"]))

# Compute similarity with all users
similarity_scores = []
for user in all_users:
    user_features = np.array(get_hobby_vector(user["hobbies"]))
    similarity = cosine_similarity([user_1_features], [user_features])[0][0]
    similarity_scores.append((user["name"], similarity))

# Sort users by similarity (highest first) and get top 2
top_matches = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:2]

# Output the top 2 matches
print("Top 2 compatible users:")
for name, score in top_matches:
    print(f"{name}: {score:.2f}")




