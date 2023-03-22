import openai
import urllib.parse

def generate_regex(requirement):
    prompt = f"You are now a Regex Expert, please write a Regex that can {requirement}, only tell me the expression nothing else"
    # Code to call the ChatGPT API and generate the regex goes here
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
    generated_regex = response.choices[0].message.content.strip()
    regex_encoded = urllib.parse.quote_plus(generated_regex)
    regex101_url = f"https://regex101.com/?regex={regex_encoded}"
    return generated_regex, regex101_url
