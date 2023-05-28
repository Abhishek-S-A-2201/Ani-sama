import openai
import ast
from API_TOKENS import OPEN_AI
openai.api_key = OPEN_AI

example = """{'scenes': [{'description': 'Ken stands in the middle of a deserted street.',
   'characters': ['Ken']},
  {'description': 'The Villain emerges from the shadows and taunts Ken.',
   'characters': ['The Villain']},
  {'description': 'The Villain attacks Ken with a bolt of dark energy and a shockwave.',
   'characters': ['Ken', 'The Villain']},
  {'description': 'Ken disarms and defeats The Villain.',
   'characters': ['Ken', 'The Villain']},
  {'description': 'The Villain transforms into a puff of smoke and vanishes, leaving Ken frustrated.',
   'characters': ['Ken', 'The Villain']},
  {'description': 'Ken stands alone in the middle of the street, reflecting on his victory.',
   'characters': ['Ken']}]}
"""


def scene_generation_util(screenplay: str) -> str:
    prompt = f"""
    Your task is to help an anime production company
    create new, creative and unique anime
    based on the character provided

    I will provide you with a screenplay and 
    your job is to describe and sepearte the screenplay into different scenes.
    The scenes should be visual descriptive.

    Return the result in JSON format.

    Ill provide you with an example format the file in the same way.

    example: <{example}>

    screenplay: ```{screenplay}```
    """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    res = completion["choices"][0]["message"]["content"]
    return res


def generate_scenes(screenplay: str):
    print("Generating scenes...")
    description = scene_generation_util(screenplay)
    scenes = ast.literal_eval(description)
    characters = []
    for i in scenes["scenes"]:
        characters.extend(i["characters"])

    return scenes, set(characters)
