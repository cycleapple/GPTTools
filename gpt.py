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
    print(language)
    if language == 'en':
        prompt = f"""
        Write an email from {sender} to {recipient} with the subject "{subject}" in {language}:

        ---
        """
    elif language == 'zh':
        prompt = f"""
        #zh-tw 寫一封Email 由 {sender} 撰寫 給 {recipient} 收件 主題是 "{subject}":

        ---
        """
    else:
        prompt = f"""
        Write an email from {sender} to {recipient} with the subject "{subject}":

        ---
        """
    
    # Call the OpenAI API to generate the email
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n = 1,
        stop=None,
    )

    # Extract the generated email from the response and return it
    email = response.choices[0].text.strip()
    return email
