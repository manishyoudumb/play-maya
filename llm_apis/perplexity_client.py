import requests
import os
import json

class PerplexityClient:
    """Client for interacting with the Perplexity AI API."""

    def __init__(self, verbose=False):
        """Initialize the Perplexity AI client with the API key."""
        self.api_key = os.getenv('PERPLEXITY_API_KEY')
        self.base_url = "https://api.perplexity.ai/chat/completions"
        self.verbose = verbose

    def stream_completion(self, messages, model, temperature=0.7, max_tokens=2048, **kwargs):
        """Stream completion from the Perplexity AI API.

        Args:
            messages (list): List of messages.
            model (str): Model for completion.
            temperature (float): Temperature for sampling.
            max_tokens (int): Maximum number of tokens to generate.
            **kwargs: Additional keyword arguments.

        Yields:
            str: Text generated by the Perplexity AI API.
        """
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.post(self.base_url, json=payload, headers=headers, stream=False)
            response.raise_for_status()
            data = response.json()
            message_content = data['choices'][0]['message']['content']
            yield message_content
        except Exception as e:
            if self.verbose:
                import traceback
                traceback.print_exc()
            else:
                print(f"An error occurred streaming completion from Perplexity AI API: {e}")
            raise RuntimeError(f"An error occurred streaming completion from Perplexity AI API: {e}")

# Test the PerplexityClient
if __name__ == "__main__":
    client = PerplexityClient(verbose=True)
    messages = [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "What is the current price of Tesla stock?"
        }
    ]
    model = "llama-3-sonar-small-32k-online"

    print("Response:")
    for chunk in client.stream_completion(messages, model):
        print(chunk)