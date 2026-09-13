from google.genai import types


click_tool = types.FunctionDeclaration(
    name="click_at_coordinates",
    description="Click once at the specified screen coordinates.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "x": {
                "type": "integer",
                "description": "Horizontal screen coordinate."
            },
            "y": {
                "type": "integer",
                "description": "Vertical screen coordinate."
            }
        },
        "required": ["x", "y"]
    }
)


type_tool = types.FunctionDeclaration(
    name="type_text",
    description="Type text into the currently focused text field.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The exact text to type."
            }
        },
        "required": ["text"]
    }
)


press_key_tool = types.FunctionDeclaration(
    name="press_key",
    description="Press a single keyboard key.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "key": {
                "type": "string",
                "description": "Key to press, such as enter, tab, escape, or backspace."
            }
        },
        "required": ["key"]
    }
)


hotkey_tool = types.FunctionDeclaration(
    name="hotkey",
    description="Press a keyboard shortcut made of multiple keys.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "keys": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Keys in the shortcut, for example ['ctrl', 'l']."
            }
        },
        "required": ["keys"]
    }
)


scroll_tool = types.FunctionDeclaration(
    name="scroll",
    description="Scroll the active window vertically.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "amount": {
                "type": "integer",
                "description": "Positive scrolls up, negative scrolls down."
            }
        },
        "required": ["amount"]
    }
)


complete_tool = types.FunctionDeclaration(
    name="task_complete",
    description="Use only when the user's requested task is visibly complete.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "Short summary of what was completed."
            }
        },
        "required": ["summary"]
    }
)


desktop_tools = types.Tool(
    function_declarations=[
        click_tool,
        type_tool,
        press_key_tool,
        hotkey_tool,
        scroll_tool,
        complete_tool
    ]
)