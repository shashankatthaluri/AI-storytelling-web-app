from flask import Blueprint, request, jsonify
import requests
import json

stability_blueprint = Blueprint('stability', __name__)

# Replace 'YOUR_STABILITY_API_KEY' with your actual Stability.ai API key
stability_api_key = 'YOUR_STABILITY_API_KEY'

@stability_blueprint.route('/generate-images', methods=['POST'])
def generate_images():
    data = request.json
    story = data.get('story')

    if not story:
        return jsonify({'error': 'No story provided'}), 400

    try:
        prompts = get_prompts(story)
        images = []

        for prompt in prompts:
            text_prompts = [{'text': prompt}]
            response = requests.post(
                'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {stability_api_key}'
                },
                data=json.dumps({'text_prompts': text_prompts})
            )
            result = response.json()
            image_data = result.get('artifacts')[0].get('base64')
            images.append(image_data)

        return jsonify({'images': images}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_prompts(story):
    # You can implement your logic here to extract prompts from the story if you have any 
    # For now, let's just split the story into sentences and use them as prompts
    return story.split('.')
