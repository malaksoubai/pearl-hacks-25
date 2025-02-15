import random

user = {
    "industry": "AI Development",
    "experience": 3,
    "skills": ["Python", "R", "Machine Learning", "AI"],
    #"topics of interest": ["Front-end development", "Back-end development"],
}
#create a class to generate users

#replace with og data
names = ["Jamie", "Trisha", "Gina", "Sai Ananya", "Malak", "Nivedhita", "Allana", "Juno", "Gayathri", "Maxine", "Mary", "Nicki"]
industries = ["AI Development", "Software Development", "Cybersecurity, Biotechnology, Electrical Engineering, Computer Engineering, Medical Doctor, Nursing"]
experience_years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20]
skills_and_topics = ["Java", "CSS", "C", "Python", "R", "Machine Learning", "AI", "Data Science", "Network Security", "Web Development, Front-end Development", "Back-end Development"]
skills_and_topics_nums = [1, 2, 3, 4]

class Mentor:
    def __init__(self, name, industry, experience):
        self.name = name
        self.industry = industry
        self.experience = experience
        self.skills = []
        self.topics = []

        skills_num = random.choice(skills_and_topics_nums)
        for index in range(0, skills_num):
            self.skills.append(random.choice(skills_and_topics))

        topics_num = random.choice(skills_and_topics_nums)
        for index in range(0, topics_num):
            self.topics.append(random.choice(skills_and_topics))

mentors = []
for i in range(3):
    mentor = Mentor(random.choice(names), random.choice(industries), random.choice(experience_years))
    mentors.append(mentor)

# mentors = [
#     {"name": "Alice", "industry": "Software Development", "experience": 7, "skills": "Python, AI, Data Science", "availability": "Evenings"},
#     {"name": "Bob", "industry": "Cybersecurity", "experience": 10, "skills": "Network Security, AI", "availability": "Mornings"},
#     {"name": "Charlie", "industry": "Software Development", "experience": 3, "skills": "Python, Web Development", "availability": "Evenings"}
# ]
