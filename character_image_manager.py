# character_image_manager.py

import os
import requests
from config import CHARACTER_IMG_DIR, GENERATED_FACE_DIR, IMAGE_GEN_PROMPT, STABLE_DIFFUSION_API

def get_or_generate_character_image(character_name):
    char_img = os.path.join(CHARACTER_IMG_DIR, f"{character_name.lower()}.png")
    gen_img = os.path.join(GENERATED_FACE_DIR, f"{character_name.lower()}.png")
    # 1. Use manual image if available
    if os.path.exists(char_img):
        return char_img
    # 2. Otherwise, generate using Stable Diffusion
    os.makedirs(GENERATED_FACE_DIR, exist_ok=True)
    payload = {
        "prompt": f"{IMAGE_GEN_PROMPT}, {character_name} cartoon portrait",
        "steps": 25,
        "sampler_index": "Euler a",
        "width": 512,
        "height": 512,
        "cfg_scale": 7,
    }
    response = requests.post(f"{STABLE_DIFFUSION_API}/sdapi/v1/txt2img", json=payload)
    image_data = response.json()["images"][0]
    # Save as PNG
    import base64
    with open(gen_img, "wb") as f:
        f.write(base64.b64decode(image_data))
    return gen_img

if __name__ == "__main__":
    # Example usage
    for name in ["ravi", "anya", "narrator"]:
        img_path = get_or_generate_character_image(name)
        print(f"Image for {name}: {img_path}")