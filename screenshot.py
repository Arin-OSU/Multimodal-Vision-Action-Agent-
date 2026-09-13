import io
import pyautogui

from google.genai import types


def capture_screen_part():
    screenshot = pyautogui.screenshot()

    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")

    return types.Part.from_bytes(
        data=buffer.getvalue(),
        mime_type="image/png"
    )