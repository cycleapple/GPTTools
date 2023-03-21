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
        #zh-tw 用繁體中文，台灣人的口吻寫一封商業Email 由 {sender} 撰寫 給 {recipient} 收件 主題是 "{subject}，同時生成一個合適的主旨":

        ---
        """
    else:
        prompt = f"""
        Write an email from {sender} to {recipient} with the subject "{subject}":

        ---
        """
    
    # Call the OpenAI API to generate the email
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n = 1,
        stop=None,
    )

    # Extract the generated email from the response and return it
    email = response.choices[0].text.strip()
    return email
