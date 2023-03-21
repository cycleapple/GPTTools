# GPT Tool

This is a web application built using Flask that provides various tools that utilize the OpenAI GPT-3 API.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Tools](#tools)
  - [Email Generation Tool](#email-generation-tool)
  - [Excel Formula Generation Tool](#excel-formula-generation-tool)
  - [Regex Generation Tool](#regex-generation-tool)
- [Contributing](#contributing)
- [License](#license)

# Overview
This web application provides tools for generating emails, Excel formulas, and regular expressions using the OpenAI GPT-3 API. It also includes a tool for generating questions and answers based on a provided PDF file.

# Installation
1. Clone the repository to your local machine:
```bash
git clone https://github.com/your_username/gpt-tool.git
```
2. Navigate to the root directory of the project:
```bash
cd gpt-tool
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory of the project and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

5. Start the Flask development server:

```bash
python app.py
```

6. Open your web browser and navigate to http://localhost:5000 to access the web application.

# Usage
Once the application is running, you can access the various tools by clicking on the corresponding links on the home page.

# Tools
## Email Generation Tool
This tool generates an email based on user-provided input for the sender, recipient, subject, and language. The generated email is created using the OpenAI GPT-3 API.

## Excel Formula Generation Tool
This tool generates an Excel formula based on user-provided input for the requirement and selection (Google Sheet or Excel). The generated formula is created using the OpenAI GPT-3 API.

## Regex Generation Tool
This tool generates a regular expression based on user-provided input for the requirement. The generated regular expression is created using a Python package called regex and is tested against sample input using an online regular expression tester, Regex101.

# Contributing
Contributions are always welcome! If you have any ideas for improvements or new features, feel free to create a pull request.

# License
This project is licensed under the MIT License.