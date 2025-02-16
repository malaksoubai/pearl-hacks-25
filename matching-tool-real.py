"""Testing the scikit-learn api for matching"""
from user_mentor_data import user, mentors
from industry_categories import names, all_industries, all_skills
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# This function checks if user's preferred industries matches the mentor's industry
def get_industry(mentor_industry) -> float:
    user_interests: list[str] = user["industry_of_interest"] 
    for i in user_interests:
        if i == mentor_industry:
            return 1
    return 0


# This fct generates a vector of skills, based off all my skills. 
# Shortcoming Note: user's len(pref-skills) == mentor's len(skillset)
def get_skills_vector(skills) -> list[float]:
    vector: list[float] = []
    for skill in all_skills:
        if skill in skills:
            vector.append(1)
        else:
            vector.append(0)
    return vector


# make the user's skills into a vector
user_skills_of_interest = np.array(get_skills_vector(user["skills_of_interest"]))

# Compute similarity with all users, and extract top 5
similarity_scores = []
for mentor in mentors:
    mentor_skills = np.array(get_skills_vector(mentor.skills))
    skills_similarity = cosine_similarity([user_skills_of_interest], [mentor_skills])[0][0]
    industry_similarity = get_industry(mentor.industry)
    averaged_similarity = (skills_similarity + industry_similarity) / 2
    similarity_scores.append((mentor.name, averaged_similarity))

top_matches = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:5]

print("Top 5 compatible users:")
for name, score in top_matches:
    percent = score*100
    print(f"{name}: {int(round(percent, 0))}%")

