import os

# Ensure folders exist
folders = ["characters", "generated_faces", "voices", "animations", "videos"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Project folders created and ready!")

# --- SCRIPT GENERATION WITH OPENAI ---

try:
    from config import OPENAI_API_KEY
except ImportError:
    print("Error: 'config.py' with OPENAI_API_KEY not found. Please create config.py.")
    OPENAI_API_KEY = None

if OPENAI_API_KEY:
    import openai

    openai.api_key = OPENAI_API_KEY

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative script writer for cartoon Instagram Reels."},
                {"role": "user", "content": "Write a funny short cartoon script for kids, around 50 words."}
            ]
        )
        script_text = response['choices'][0]['message']['content']
        print("\nGenerated Script:\n", script_text)
    except Exception as e:
        print("Error generating script with OpenAI:", e)
else:
    print("Skipping script generation. Add your OpenAI API key to config.py to enable this step.")

print("Ready to start building your pipeline steps!")