import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set up OpenAI API authentication using the API key from the environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a function to generate an email using GPT
def generate_email(sender, recipient, subject, language):
    # Define the prompt for generating the email
    if language == 'en':
        prompt = f"""
        Write an professional business email from {sender} to {recipient} with the subject "{subject}" in {language}:

        ---
        """
    elif language == 'zh_TW':
        prompt = f"""
        #zh-tw 用繁體中文，台灣人用字寫一封專業口吻的Email 由 {sender} 撰寫 給 {recipient} 收件 主題是 "{subject}":

        ---
        """
    else:
        prompt = f"""
        Write an email from {sender} to {recipient} with the subject "{subject}":

        ---
        """

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

    # Extract the generated email from the response and return it
    email = response.choices[0].message.content.strip()
    return email
