import openai

def generate_excel_formula(requirement, selection):
    prompt = f"You are now an Excel Formula Expert, please write a formula that can {requirement} for {selection}"
    model_engine = "text-davinci-003"
    max_tokens = 1024
    temperature = 0.7
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    generated_formula = response.choices[0].text.strip()
    return generated_formula
