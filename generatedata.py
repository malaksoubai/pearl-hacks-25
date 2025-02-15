from user_mentor_data import user as user_data
from user_mentor_data import mentors
from industry_categories import industry_categories

weights = { #all weights should add to 1
    "industry": 0.4,
    "experience": 0.2,
    "skills": 0.3,
    "topics": 0.3,
}

user = user_data

def industry_score(user_industry, mentor_industry):
    score = 0
    if user_industry == mentor_industry:
         score += 1
    else:
         for industry in industry_categories:
             temp_indus_cats = industry_categories.get(industry)
             if user_industry in temp_indus_cats and mentor_industry in temp_indus_cats:
                score += 0.5
                break
    return score

# def experience_score():
#     pass
#
def skills_score(user_skills, mentor_skills):
    score = 0
    for skill in user_skills:
        if skill in mentor_skills:
            score += 1
    return score
#
# def interestedtopics_score(user_topics, mentor_topics):
#     score = 0
#     for topic in user_topics:
#         if topic in mentor_topics:
#             score += 1
#     return score

# def get_individual_scores():
#     pass

features_pylist = []
match_scores = []
match_scores_w_names = {}
final_match_labels = []
def calculate_scores():
    score = 0
    industry_similarity = 0
    experience_similarity = 0
    skills_similarity = 0
    topics_similarity = 0

    for mentor in mentors:
        industry_similarity = industry_score(user.get("industry"), mentor.get("industry"))*weights.get("industry")
        experience_similarity = 0*weights.get("experience")
        skills_similarity = skills_score(user.get("skills"), mentor.get("skills"))*weights.get("skills")
        # topics_similarity = interestedtopics_score(user.get("topics"), mentor.get("topics"))*weights.get("skills")
        score = industry_similarity + experience_similarity + skills_similarity
        match_scores_w_names[mentor.get("name")] = score

        features_pylist.append([industry_similarity, experience_similarity, skills_similarity])
        match_scores.append(score)

        if score > 0.5:
            final_match_labels.append(1)
        else:
            final_match_labels.append(0)

        score = 0

calculate_scores()
print(features_pylist)
print(match_scores)
print(final_match_labels)
print(match_scores_w_names)

