from flask import Blueprint, request, jsonify, Flask
import openai



openai_blueprint = Blueprint('openai', __name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API keys
openai.api_key = 'YOUR_OPENAI_API_KEY'

@openai_blueprint.route('/generate-story', methods=['POST'])
def generate_story():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=512
        )
        generated_text = response.choices[0].text.strip()
        return jsonify({'story': generated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
