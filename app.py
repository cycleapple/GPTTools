from flask import Flask, render_template, request, url_for, redirect
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

@app.route('/stable_diffusion_tool')
def stable_diffusion_tool():
    return render_template('stable_diffusion_tool.html')

@app.route('/regex_generation_tool', methods=['GET', 'POST'])
def regex_generation_tool():
    if request.method == 'POST':
        # Get the form data
        requirement = request.form['requirement']
        
        # Generate the regex
        regex = generate_regex(requirement)

        # Generate the regex101 URL
        regex101_url = url_for('regex101', url=f'https://regex101.com/?regex={regex}')

        # Render the template with the generated regex and regex101 URL
        return render_template('regex_generation_tool.html', regex=regex, regex101_url=regex101_url)

    # Render the template with the form
    return render_template('regex_generation_tool.html')


@app.route('/regex101')
def regex101():
    regex_url = request.args.get('url')
    return redirect(regex_url)


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
    return generated_regex

if __name__ == '__main__':
    app.run(debug=True)
