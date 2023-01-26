import requests
import os

def predict_prompt(prompt):
  apiKey = os.environ["OPENAI_API_KEY"]
  model = 'text-davinci-003'
  temperature = 0.
  maxTokens = 150

  url = 'https://api.openai.com/v1/completions'
  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + apiKey
  }
  payload = {
      'model': model,
      'prompt': prompt,
      'temperature': temperature,
      'max_tokens': maxTokens
  }

  response = requests.post(url, headers=headers, data=json.dumps(payload))

  response_json = json.loads(response.text)
  return response_json['choices'][0]['text']