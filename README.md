# Pearl Hacks 2025
## Inspiration
In today's technology industry, women are not equally represented, especially women of color. Factors such as hiring bias and lack of female role models often discourage women from the technology industry. As students ourselves, we have found one element in particular to be daunting: interviews. In this project, we created both a mock-interview tool and a ML mentorship matching tool, designed to simplify the process of preparing to join the technology workforce.

## What it does
Our website is home to a platform that allows users to either practice mock-interviewing with an AI-assisted voice-recognition and evaluation system, or fill out a survey to be matched with a mentor.

On the home page, we have an About Us page, with navigation links at the top. When the user navigates to "Mock Interviews", they have the option to generate a question, then subsequently record their response. Upon recording their response, they will choose to evaluate their response (or re-record). The page will render OpenAI feedback based on the generated question and recorded response, which is also transcribed. The generative-AI model will consider multiple aspects of the user's response, such as level of detail, formality, and adherence to the question.

Another feature of our Mock Interviews page is the facial-expressions tracking. This feature is not fully added to our current web platform, but it will be integrated soon! When the user presses the "interview" button, it will utilize the user's webcam using OpenCV to track their facial expressions and behavior. Then, the program will take timely screen captures of the user, which are then analyzed by generative AI software to evaluate the user's body language in the mock interview and return an evaluation.

Our user also has the option to view the Mentorship page. First, they have the option to fill out fields based on their interests. For this project, we have implemented the "industry" and "skills of interest" fields, and we plan to add more in the future. Upon selecting their respective fields, a results page is generated with the user's matching of the top five respective mentors with similar skills and interests.

## How we built it
We used Python primarily for backend scripts, such as in our computer vision and voice recognition programs. We used OpenAI for the generative AI calls, as well as Node.js and Express for our web application and framework. For the mentor matching program, we used scikit-learn and numpy within Python to create our matching algorithm. For the front-end, we used HTML and CSS. Lastly, we used JavaScript to handle the API calls and requests.

## Challenges we ran into
We had some difficulty setting up our environment as a team and determining which frameworks and dependencies to use, especially between Mac and Windows! We originally intended to create a dev-container for the majority of our project, but quickly realized that it was not necessary for our hackathon.

We had challenges at the tail-end of our project in integrating our computer vision application with Express. Despite this, we hope to fully integrate it soon!

## Accomplishments that we're proud of
Setting up both our computer vision model and voice transcription models was a huge success for our team! We also learned a lot from implementing our generative AI application, both to analyze the images in the interview recording as well as analyze text for the user's interview response.

## What's next for SheDevs
In the future, we hope to add user login and authentication capabilities, which distinct pages for both user and mentor sign up. We hope to add security measures to restrict to students with a university email address as well.
For future implementation, we hope to fully integrate our computer vision software onto the web application in conjunction with the voice recognition and analysis software.
