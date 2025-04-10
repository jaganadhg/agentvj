# AgentVJ

AgentVJ is a demo project for creating an AI agent from scratch. This project was created for a demo at the TMLS Micro Summit.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

To use the AgentVJ, you can create an instance of the agent and run it with a task. Below is an example of how to use the agent:

```python
from vj.agents.core import BaseAgent, AgentMemory
from vj.tools.tool import CalculatorTool

class MyAgent(BaseAgent):
    def generate_action(self, task: str) -> dict:
        # Implement action generation logic
        pass

    def execute_action(self, action: dict) -> Any:
        # Implement action execution logic
        pass

# Create an instance of the agent
tools = [CalculatorTool()]
model = lambda x: x  # Dummy model for demonstration
agent = MyAgent(tools=tools, model=model)

# Run the agent with a task
task = "Calculate the sum of 2 and 3"
result = agent.run(task)
print(result)
```

## Example Code Snippets

Here are some example code snippets to demonstrate the usage of the AgentVJ:

### Example 1: Using the CalculatorTool

```python
from vj.tools.tool import CalculatorTool

# Create an instance of the CalculatorTool
calculator = CalculatorTool()

# Execute a mathematical expression
expression = "2 + 3"
result = calculator.execute(expression)
print(f"Result: {result}")
```

### Example 2: Creating a Custom Agent

```python
from vj.agents.core import BaseAgent, AgentMemory
from vj.tools.tool import CalculatorTool

class CustomAgent(BaseAgent):
    def generate_action(self, task: str) -> dict:
        # Implement custom action generation logic
        return {"tool": "calculator", "input": task}

    def execute_action(self, action: dict) -> Any:
        # Implement custom action execution logic
        tool = self.tools[action["tool"]]
        return tool.execute(action["input"])

# Create an instance of the custom agent
tools = [CalculatorTool()]
model = lambda x: x  # Dummy model for demonstration
agent = CustomAgent(tools=tools, model=model)

# Run the agent with a task
task = "5 * 6"
result = agent.run(task)
print(f"Result: {result}")
```
