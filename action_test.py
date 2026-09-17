import os
import io
import json
import time
import pyautogui
from google import genai
from google.genai import types

# 1. Safety First: Enable the kill switch
# Drag your mouse to any corner of the screen to instantly stop the script!
pyautogui.FAILSAFE = True

# 2. Initialize the Gemini Client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Define the overall goal you want the agent to achieve
USER_GOAL = "Open Visual Studio Code."

def capture_screen_bytes():
    """Takes a screenshot and converts it to memory bytes for Gemini."""
    screenshot = pyautogui.screenshot()
    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    return buffer.getvalue()

def get_next_action(image_bytes, goal):
    """Sends the screenshot to Gemini and returns a parsed JSON dictionary."""
    prompt = f"""
    You are controlling a Windows computer.

    Goal:
    {goal}

    Look at the screenshot and choose exactly ONE next action to get closer to the goal.

    Return ONLY valid JSON matching this structure:
    {{
        "action": "click",      // can be "click", "type", or "done"
        "x": 123,               // required if action is "click"
        "y": 456,               // required if action is "click"
        "text": "hello",        // required if action is "type"
        "target": "target description",
        "reason": "why this helps"
    }}

    Rules:
    - Only choose one action.
    - Coordinates must match the screenshot.
    - Do not output markdown.
    - Do not output anything outside the JSON.
    - Try to open chrome
    """
    

    print("\nThinking...")
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            types.Part.from_text(text=prompt),
            types.Part.from_bytes(data=image_bytes, mime_type="image/png")
        ],
        config=types.GenerateContentConfig(temperature=0)
    )
    
    # Strip away accidental markdown if the model disobeys the prompt rules
    clean_text = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(clean_text)

def execute_action(action):
    """Translates the JSON dictionary into physical mouse/keyboard commands."""
    command = action.get("action")
    
    print(f"Reasoning: {action.get('reason')}")
    print(f"Target: {action.get('target')}")
    
    if command == "click":
        x, y = action.get("x"), action.get("y")
        print(f"Executing: Moving mouse to ({x}, {y}) and clicking.")
        pyautogui.moveTo(x, y, duration=0.5) 
        pyautogui.click()
        return True
        
    elif command == "type":
        text = action.get("text")
        print(f"Executing: Typing '{text}'")
        pyautogui.write(text, interval=0.05)
        return True
        
    elif command == "done":
        print("Agent has declared the task complete!")
        return False
        
    else:
        print(f"Unknown action: {command}")
        return False

# 3. The Orchestration Loop
print(f"Starting Agent. Goal: {USER_GOAL}")
step_count = 0
max_steps = 10  # Prevent infinite loops if the agent gets stuck

while step_count < max_steps:
    step_count += 1
    print(f"\n--- Step {step_count} ---")
    
    # Step A: Perceive the environment
    img_bytes = capture_screen_bytes()
    
    try:
        # Step B: Reason about the next action[cite: 2]
        action_dict = get_next_action(img_bytes, USER_GOAL)
        
        # Step C: Execute mouse and keyboard actions[cite: 2]
        continue_loop = execute_action(action_dict)
        
        if not continue_loop:
            break  # Exit the loop if the task is done
            
    except Exception as e:
        print(f"An error occurred: {e}")
        break
        
    # Pause for 2 seconds to let the computer's UI load before taking the next screenshot
    time.sleep(2)

print("\nAgent finished execution.")