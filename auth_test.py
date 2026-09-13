import os
from google import genai

key = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=key)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Reply with exactly: AUTH WORKS"
)

print(response.text)