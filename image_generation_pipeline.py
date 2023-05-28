import torch
from diffusers import StableDiffusionPipeline
import os
from torch import autocast

pre_trained = "./pre_trained/waifu-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(
    pre_trained,
    torch_dtype=torch.float32
).to('mps')


def save_img(file_path, image):
    os.makedirs(file_path, exist_ok=True)
    base_count = len(os.listdir(file_path)) + 1
    file_path = os.path.join(file_path, f"img_{base_count:02}.png")
    image.save(file_path)
    return file_path


def generate_character_images(characters: list):
    generator = torch.Generator("mps")
    character_images = {"characters": []}
    for character in characters:
        character_images["characters"].append({"name": character["name"], "images": []})
        for i in range(4):
            seed = generator.seed()
            generator = generator.manual_seed(seed)
            prompt = f"{character['description']}, anime, high resolution, detailed, illustration concept art anime key " \
                "visual trending pixiv fanbox by wlop and greg rutkowski and makoto shinkai and studio ghibli"
            with autocast("mps"):
                image = pipe(prompt, guidance_scale=6).images[0]
            file = os.path.join("./images", character['name'])
            os.makedirs(file, exist_ok=True)
            file = save_img(file, image)
            character_images["characters"][-1]["images"].append(file)

    return character_images
