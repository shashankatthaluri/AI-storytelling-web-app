# AI Storytelling Web App 📚🤖

Welcome to the AI Storytelling Web App! This project aims to create an interactive web application that generates stories and accompanying images using state-of-the-art AI models. Harnessing the power of OpenAI for text generation and Stability.ai for image generation, this app brings storytelling to a whole new level.

<details>
   <summary> Idea on paper 📄🖋 </summary>
   
  
  Here's a general outline of the steps I planned when I thought of doing this project:

1. Planning and Research 🔎:
- Define the target audience and age group for the children's storytelling web app.
- Research existing children's storytelling apps to understand features, user experience, and content.
- Identify the specific AI capabilities you want to integrate, such as text generation, natural language understanding, or character generation.

2. Setting up Development Environment 🌎:
- Install Python and necessary libraries such as Flask for web development.
- Obtain API keys or access tokens for OpenAI and Stability.ai, if applicable.
- Set up a version control system like Git for managing code changes.

3. Designing the User Interface 🖥:
- Create wireframes or mockups of the web app's user interface.
- Design child-friendly and visually appealing UI elements, including colors, fonts, and illustrations.
- Consider incorporating interactive elements like animations or sound effects.

4. Implementing Backend Functionality 🔒:
- Develop the backend logic using Flask or another web framework.
- Integrate OpenAI's API for text generation to create story content.
- Implement features for user authentication, if desired, to save or personalize stories.

5. Integrating Stability.ai for Safety 🖼:
- Use Stability.ai to ensure that generated content is safe and appropriate for children.
- Implement content moderation mechanisms to filter out potentially harmful or inappropriate text.

6. Testing 🛠:
- Test the web app thoroughly to identify and fix any bugs or issues.
- Perform usability testing with children or parents to gather feedback on the app's user experience and content.

7. Deployment 👆:
- Choose a hosting provider for deploying the web app, such as Heroku or AWS.
- Set up the deployment environment and configure the web server.
- Deploy the web app to make it accessible to users.

8. Maintenance and Updates 👇:
- Monitor the web app for performance and security issues.
- Regularly update the app with new features, content, or improvements based on user feedback.
- Stay informed about changes or updates to the OpenAI and Stability.ai APIs and adjust the app accordingly.

</details>



## Features

✨ **Text Generation**: Utilize OpenAI's powerful text generation models to create captivating stories based on user prompts.

🎨 **Image Generation**: Leverage Stability.ai's cutting-edge technology to transform text prompts into stunning images that complement the stories.

🌐 **Web Interface**: Intuitive and user-friendly web interface allows users to interact with the AI models seamlessly.

## Installation 🖥

1. Clone the repository:
   ```bash
   git clone https://github.com/shashankatthaluri/AI-storytelling-web-app.git
   ```
2. Navigate to the project directory:

```bash
cd AI-storytelling-web-app
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Replace placeholder API keys:

- OpenAI API key: Replace 'YOUR_OPENAI_API_KEY' in src/app/api/openai/route.py.
- Stability.ai API key: Replace 'YOUR_STABILITY_API_KEY' in src/app/api/stability/route.py.

5. Run the application:

```bash
python app.py
```
## Usage ⚙

- Access the web application by visiting http://localhost:5000 in your web browser.

- Enter a prompt in the provided textarea.

- Click on the "Generate Story" button to generate a story along with accompanying images.

- Enjoy reading your AI-generated story and exploring the generated images!

## Project Structure 📂

```scss
AI-storytelling-web-app/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── openai/
│   │   │   │   └── route.py
│   │   │   └── stability/
│   │   │       └── route.py
│   │   ├── static/
│   │   │   ├── styles.css
│   │   │   └── script.js
│   │   ├── templates/
│   │   │   └── index.html
│   │   └── __init__.py
└── venv/
└── app.py
```

## Contributing 👩‍💻👨‍💻
Contributions are welcome! Feel free to open issues or pull requests for any improvements or features you'd like to see in the project.
