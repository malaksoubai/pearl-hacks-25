import random
from industry_categories import names, all_industries, all_skills

user = {
    "industry_of_interest": ["AI Development", "Cybersecurity", "Biotechnology"],
    "skills_of_interest": ["Python", "R", "Machine Learning", "AI"],
}

#create a class to generate users

#replace with og data
# names = ["Jamie", "Trisha", "Gina", "Sai Ananya", "Malak", "Nivedhita", "Allana", "Juno", "Gayathri", "Maxine", "Mary", "Nicki"]
# industries = ["AI Development", "Software Development", "Cybersecurity, Biotechnology, Electrical Engineering, Computer Engineering, Medical Doctor, Nursing"]
# experience_years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20]
# skills_and_topics = ["Java", "CSS", "C", "Python", "R", "Machine Learning", "AI", "Data Science", "Network Security", "Web Development, Front-end Development", "Back-end Development"]
# skills_and_topics_nums = [1, 2, 3, 4]

class Mentor:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.skills = []

        skills_num = 7
        for index in range(0, skills_num):
            self.skills.append(random.choice(all_skills))


mentors = [] #let's generate mentor objects babyyyyy
for i in range(30):
    mentor = Mentor(random.choice(names), random.choice(all_industries))
    mentors.append(mentor)

# mentors = [
#     {"name": "Alice", "industry": "Software Development", "skills": ["Python", "AI", "Data Science", "R"]},
#     {"name": "Bonny", "industry": "Cybersecurity", "skills": ["Network Security", "AI", "DevOps", "C"]},
#     {"name": "Charlie", "industry": "Software Development", "skills": ["Python", "AI", "Web Development", "CSS"]}
# ]
