# script_generator.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_script(topic="Teenage love, funny, school romance"):
    prompt = (
        f"Write a short cartoon script for a YouTube/Instagram Reel on the topic: {topic}.\n"
        "Format with character names, dialogue, and simple scene/narrator directions."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    script = response['choices'][0]['message']['content']
    return script

if __name__ == "__main__":
    script = generate_script()
    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)
    print("Script written to script.txt")