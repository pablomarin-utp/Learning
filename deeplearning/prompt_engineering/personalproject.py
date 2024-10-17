import requests

api_key = "sk-proj-VLmmcRprOhmoZE4ZQeTBT3BlbkFJBmBzyc2JYZZZZGEdhy10"
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
