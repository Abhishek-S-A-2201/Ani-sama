import openai
import ast
# openai.api_key = "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"

example = """{'characters': [{'name': 'Ken',
   'description': 'A tall, muscular man with a determined look on his face'},
  {'name': 'The Villain',
   'description': 'Clad in a hooded robe, obscuring his face. He wields a wicked-looking staff, crackling with purple energy.'}],
 'background': {'location': 'City streets',
  'time': 'Night',
  'atmosphere': 'Deserted'}
 }"""


def visuals_generation_util(screenplay: str) -> str:
    prompt = f"""
    Your task is to help an anime production company
    create new, creative and unique anime
    based on the character provided

    I will provide you with a screen play and 
    your job is to extract the characters and background from the screenplay
    and give me a visual description of all the characters and background,
    based on the screenplay delimited by 
    triple backticks.

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


def generate_visuals(screenplay: str):
    print("Generating the visuals...")
    description = visuals_generation_util(screenplay)
    visuals = ast.literal_eval(description)
    return visuals["characters"], visuals["background"]

