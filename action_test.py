import os
import io
import json
import pyautogui

from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

# Take screenshot
screenshot = pyautogui.screenshot()

buffer = io.BytesIO()
screenshot.save(buffer, format="PNG")
image_bytes = buffer.getvalue()

prompt = """
You are controlling a Windows computer.

Goal:
Open Visual Studio Code.

Look at the screenshot and choose exactly ONE next action.

Return ONLY valid JSON:

{
  "action": "click",
  "x": 123,
  "y": 456,
  "target": "target description",
  "reason": "why this helps"
}

Rules:
- Only choose one click.
- Coordinates must match the screenshot.
- Do not output markdown.
- Do not output anything outside the JSON.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        types.Part.from_text(text=prompt),
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/png"
        )
    ],
    config=types.GenerateContentConfig(
        temperature=0
    )
)

print("RAW RESPONSE:")
print(response.text)

action = json.loads(response.text)

print("\nPARSED ACTION:")
print(action)

print(
    f"\nGemini wants to click "
    f"({action['x']}, {action['y']}) "
    f"on: {action['target']}"
)