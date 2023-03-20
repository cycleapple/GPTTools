from flask import Flask, render_template, request
from gpt import generate_email
import openai


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

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

@app.route('/email_optimize_tool')
def email_optimize_tool():
    return render_template('email_optimize_tool.html')

@app.route('/stable_diffusion_tool')
def stable_diffusion_tool():
    return render_template('stable_diffusion_tool.html')

@app.route('/story_generation_tool')
def story_generation_tool():
    return render_template('story_generation_tool.html')

if __name__ == '__main__':
    app.run(debug=True)
