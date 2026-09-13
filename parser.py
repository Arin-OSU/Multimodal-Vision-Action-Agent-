from dataclasses import dataclass
from typing import Any


@dataclass
class ToolCall:
    name: str
    args: dict[str, Any]


def parse_tool_call(response) -> ToolCall:

    if not response.function_calls:
        raise ValueError("Gemini returned no tool call.")

    if len(response.function_calls) > 1:
        raise ValueError("Expected exactly one tool call.")

    call = response.function_calls[0]

    return ToolCall(
        name=call.name,
        args=dict(call.args)
    )