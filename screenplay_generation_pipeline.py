import openai
# openai.api_key = "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"


def screenplay_generation_util(scene: str, duration: int) -> str:
    prompt = f"""
    Your task is help an anime production company 
    create new, cretive and different anime 
    based on the scene idea provided

    Write a screenplay for a scene,
    based on the scene provided in the idea delimited by 
    triple backticks.

    The duration of the scene should be {duration} seconds long.

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


def generate_screenplay(scene: str, duration: int):
    print("Generating screenplay...")
    screenplay = screenplay_generation_util(scene, duration)
    screenplay_str = screenplay.replace("\n", " ")
    screenplay_html = screenplay.replace("\n", "<br />")
    return screenplay_str, screenplay_html


