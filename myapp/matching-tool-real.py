"""Testing the scikit-learn api for matching"""
from user_mentor_data import user, mentors
from industry_categories import names, all_industries, all_skills
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# import sys
# import json

# # Read the data from stdin (Node.js sends it as a string)
# input_data = sys.argv[1]  # If you passed data as an argument
# user_data = json.loads(input_data)

# industry_of_interest = user_data['industry_of_interest']
# skills_of_interest = user_data['skills_of_interest']


with open(file=f"mentorinfo.txt", mode="w") as new_letter:
    new_letter.write("Your top 5 mentor matches are:" + "\n")

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
    similarity_scores.append((mentor, averaged_similarity))

top_matches = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:5]

# print("Your top 5 mentor matches are:")
for mentor, score in top_matches:
    percent = score*100
    # print(f"{mentor.name}: {int(round(percent, 0))}%")
    # print("   industry: " + mentor.industry)
    # print("   skills: " + ", ".join(mentor.skills))
    # print("   contacts: " + mentor.email)
    new_txt_text = "   industry: " + mentor.industry + "\n" + "   skills: " + ", ".join(mentor.skills) + "\n" + "   contacts: " + mentor.email + "\n"
    with open(file=f"mentorinfo.txt", mode="a") as new_letter:
        new_letter.write(f"{mentor.name}: {int(round(percent, 0))}%" + "\n")
        new_letter.write(new_txt_text)
    
# output_data = {'matches': top_matches}  # or any suitable structure
# print(json.dumps(output_data))  





# Our qstretch goal: pronouns / optional Ai generated email

