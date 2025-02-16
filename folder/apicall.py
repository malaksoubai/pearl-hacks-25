import ollama
import os


screenshots_folder = "screenshots"
#Add all files iin screenshots to list
screenshot_list = [os.path.join(screenshots_folder, f) for f in os.listdir(screenshots_folder) if os.path.isfile(os.path.join(screenshots_folder, f))]
print(screenshot_list)


res = ollama.chat(
   model="llava",
   messages=[
       {
           'role': 'user',
           'content': 'Assess interviewee eye contact and body language and provide improvements in 4 sentences:',
           'images': screenshot_list
       }
   ],
)


print(res['message']['content'])