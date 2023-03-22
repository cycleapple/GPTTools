import openai

def generate_excel_formula(requirement, selection):
    prompt = f"You are now an Excel Formula Expert, please write a formula that can {requirement} for {selection}, no explanation"
    model = "gpt-3.5-turbo"
    messages = [{"role": "user", "content": prompt}]
    temperature = 0.7
    max_tokens = 1024
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature = temperature,
        max_tokens = max_tokens
    )
    generated_formula = response.choices[0].message.content.strip()
    return generated_formula
