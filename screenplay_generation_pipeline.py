import openai
from API_TOKENS import OPEN_AI
openai.api_key = OPEN_AI


def screenplay_generation_util(scene: str) -> str:
    prompt = f"""
    Your task is help an anime production company 
    create new, cretive and different anime 
    based on the scene idea provided

    Write a screenplay for a scene,
    based on the scene provided in the idea delimited by 
    triple backticks.

    Give me the screen play in the form of a story.
    Which is passed on to the producer, to read and approve.

    idea: ```{scene}```

    """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    res = completion["choices"][0]["message"]["content"]

    return res


def generate_screenplay(scene: str):
    print("Generating screenplay...")
    screenplay = screenplay_generation_util(scene)
    screenplay_str = screenplay.replace("\n", " ")
    screenplay_html = screenplay.replace("\n", "<br />")
    return screenplay_str, screenplay_html


