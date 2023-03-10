import requests
import os
import json
from getpass import getpass
import warnings

def predict_prompt(prompt):
  apiKey = os.environ.get("OPENAI_API_KEY")
  if apiKey is None:
    print("""Api Key is missing. Head over to:
https://beta.openai.com/account/api-keys
Please enter OPENAI API KEY:""")
    apiKey = input()
    apiKey = apiKey.strip()
    assert "sk-" in apiKey, "API Key needs to start with sk-..."
    os.environ["OPENAI_API_KEY"] = apiKey
  model = os.environ.get("OPENAI_MODEL",None)
  if not model:
    model = 'text-davinci-003'
    os.environ["OPENAI_MODEL"] = model
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
  response_json = response.json()
  try:
    return response_json['choices'][0]['text']
  except KeyError:
    print(response_json)
    # warnings.warn(str(response_json))
  except Exception as e:
    return f"Error {str(e)}"