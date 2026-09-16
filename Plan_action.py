import pyautogui
import time

# Enable the kill-switch (drag physical mouse to a screen corner to stop the script)
pyautogui.FAILSAFE = True 

def execute_action(action_data):
    """Converts Gemini's JSON dictionary into physical OS actions."""
    
    # Read the 'action' type from the JSON
    command = action_data.get("action")
    
    if command == "click":
        # Extract coordinates[cite: 1]
        target_x = action_data.get("x")
        target_y = action_data.get("y")
        
        print(f"Moving mouse to ({target_x}, {target_y})...")
        # Move the mouse smoothly over 0.5 seconds
        pyautogui.moveTo(target_x, target_y, duration=0.5) 
        pyautogui.click()
        print("Click complete!")
        
    elif command == "type":
        # If the AI suggests typing, extract the text
        text_to_type = action_data.get("text", "")
        print(f"Typing: {text_to_type}")
        pyautogui.write(text_to_type, interval=0.05)
        
    elif command == "done":
        print("Agent believes the task is complete!")
        return False # Returns False to signal the loop should stop
        
    else:
        print(f"Unknown action suggested by Gemini: {command}")
    
    # Pause to let your computer's UI load before the next step
    time.sleep(1)
    return True