import google.generativeai as genai

genai.configure(api_key = "AIzaSyBsY5WV-ucMyP84yoq6gSfwWZ3a1I8KCo8") 

for i in genai.list_models():
    print(i.name)
    