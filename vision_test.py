import os
import io
import pyautogui

from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

screenshot = pyautogui.screenshot()

screenshot.save("debug_screenshot.png")
print("Saved local screenshot as 'debug_screenshot.png'")

buffer = io.BytesIO()
screenshot.save(buffer, format="PNG")
image_bytes = buffer.getvalue()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/png"
        ),
        "Describe exactly what is currently visible on my computer screen. "
        "Identify the main applications, windows, buttons, text fields, "
        "and anything I could interact with. Do not take any actions yet."
    ]
)

print("\n--- Gemini's Analysis ---")
print(response.text)
