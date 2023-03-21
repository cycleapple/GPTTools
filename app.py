from flask import Flask, render_template, request, redirect
from email_generation import generate_email
from excel_formula_generator import generate_excel_formula
from regex_generator import generate_regex
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/excel_formula_generation_tool', methods=['GET', 'POST'])
def excel_formula_generation_tool():
    if request.method == 'POST':
        # Get the form data
        requirement = request.form['requirement']
        selection = request.form['selection']

        # Generate the formula using GPT
        formula = generate_excel_formula(requirement, selection)

        # Render the template with the generated formula
        return render_template('excel_formula_generation_tool.html', formula=formula)

    # Render the template with the form
    return render_template('excel_formula_generation_tool.html')

@app.route('/email_generation_tool', methods=['GET', 'POST'])
def email_generation_tool():
    if request.method == 'POST':
        # Get the form data
        sender = request.form['sender']
        recipient = request.form['recipient']
        subject = request.form['subject']
        language = request.form['language']

        # Generate the email using GPT
        email = generate_email(sender, recipient, subject, language)

        # Render the template with the generated email
        return render_template('email_generation_tool.html', email=email)

    # Render the template with the form
    return render_template('email_generation_tool.html')

@app.route('/regex_generation_tool', methods=['GET', 'POST'])
def regex_generation_tool():
    if request.method == 'POST':
        # Get the form data
        requirement = request.form['requirement']
        
        # Generate the regex
        regex, regex101_url = generate_regex(requirement)

        # Render the template with the generated regex and regex101 URL
        return render_template('regex_generation_tool.html', regex=regex, regex101_url=regex101_url)

    # Render the template with the form
    return render_template('regex_generation_tool.html')

if __name__ == '__main__':
    app.run(debug=True)
