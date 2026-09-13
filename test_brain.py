from agent_brain import AgentBrain


brain = AgentBrain()

action = brain.decide_next_action(
    "Open Visual Studio Code."
)

print("\nBRAIN OUTPUT")
print("------------")
print("Tool:", action.name)
print("Arguments:", action.args)