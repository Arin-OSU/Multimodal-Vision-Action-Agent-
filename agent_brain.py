import os

from google import genai
from google.genai import types

from screenshot import capture_screen_part
from tools import desktop_tools
from prompts import SYSTEM_PROMPT
from parser import parse_tool_call


class AgentBrain:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"]
        )

        self.model = "gemini-3.6-flash"

    def decide_next_action(self, goal: str):

        screen = capture_screen_part()

        prompt = f"""
USER GOAL:
{goal}

Inspect the screenshot and choose the single best next action.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                types.Part.from_text(text=prompt),
                screen
            ],
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[desktop_tools],
                automatic_function_calling=
                    types.AutomaticFunctionCallingConfig(
                        disable=True
                    ),
                tool_config=types.ToolConfig(
                    function_calling_config=
                        types.FunctionCallingConfig(
                            mode="ANY"
                        )
                ),
                temperature=0
            )
        )

        return parse_tool_call(response)