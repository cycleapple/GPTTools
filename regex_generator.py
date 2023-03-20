import openai
import urllib.parse

def generate_regex(requirement):
    prompt = f"You are now a Regex Expert, please write a Regex that can {requirement}, only tell me the expression nothing else"
    # Code to call the ChatGPT API and generate the regex goes here
    model_engine = "text-davinci-003"
    max_tokens = 1024
    temperature = 0.5
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
    generated_regex = response.choices[0].text.strip()
    regex_encoded = urllib.parse.quote_plus(generated_regex)
    regex101_url = f"https://regex101.com/?regex={regex_encoded}"
    return generated_regex, regex101_url
