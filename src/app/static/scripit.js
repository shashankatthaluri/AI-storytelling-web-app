// static/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Get the form, textarea, and result container elements
    const form = document.querySelector('form');
    const textarea = document.querySelector('textarea');
    const resultContainer = document.querySelector('.result');

    // Add event listener for form submission
    form.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        const prompt = textarea.value.trim(); // Get the prompt from the textarea
        if (!prompt) {
            alert('Please enter a prompt!'); // Display an alert if prompt is empty
            return;
        }

        try {
            // Clear previous results
            resultContainer.innerHTML = '';

            // Fetch data from the backend
            const storyResponse = await fetch('/api/generate-story', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt }) // Send prompt in JSON format
            });
            const storyData = await storyResponse.json(); // Parse JSON response

            // Display generated story
            const storyElement = document.createElement('p');
            storyElement.textContent = storyData.story;
            resultContainer.appendChild(storyElement); // Append story to result container
        } catch (error) {
            console.error('Error:', error.message); // Log any errors to console
            alert('An error occurred. Please try again later.'); // Display error message to user
        }
    });
});
