# Multimodal Vision-Action Agent

A multimodal desktop AI agent that can **see the screen, understand what is happening, decide what action to take next, and interact with the computer through mouse and keyboard controls**.

The long-term goal is to build a reliable autonomous agent that can:

- Observe the desktop environment
- Understand applications, buttons, text fields, and UI elements
- Reason about the next action
- Execute mouse and keyboard actions
- Verify whether an action succeeded
- Recover from mistakes
- Complete multi-step tasks
- Learn reusable skills from past interactions

---

## Current Features

- Gemini API integration
- Desktop screenshot capture
- Multimodal screen understanding
- UI element identification
- Structured JSON action generation
- Coordinate-based action selection
- PyAutoGUI integration for mouse and keyboard control
- Basic safety testing before automatic execution

---

## Current Pipeline

```text
User Goal
   ↓
Screenshot
   ↓
Multimodal Model
   ↓
Screen Understanding
   ↓
Action Selection
   ↓
Structured JSON
   ↓
Mouse / Keyboard Action
