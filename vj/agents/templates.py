from dataclasses import dataclass
from typing import List, Optional
from loguru import logger


@dataclass
class ReactAgentTemplate:
    """Template for React-style agents using TOML configuration"""

    DEFAULT_TEMPLATE = """
# React Agent Template Configuration
[agent]
name = "react_agent"
description = "A React-style agent that follows thought-observation-action cycle"
max_steps = 10
temperature = 0.7

[prompts]
system = '''You are a React agent that thinks step by step:
1. Analyze the task
2. Think about what to do
3. Execute an action
4. Observe the result
5. Repeat until task is complete'''

thought_template = '''
Task: {task}
Previous Actions: {history}
Current Step: {step}

Thought: Let me think about this step by step:
1) {thought}

Action: {action}
'''

observation_template = '''
Observation: {observation}
Next step: {next_step}
'''

[output_format]
thought = "string"  # Agent's reasoning process
action = "json"     # Must include 'tool' and 'input' fields
observation = "string"  # Result of action execution

[constraints]
max_thought_length = 500
max_retries = 3
timeout = 30  # seconds
"""

    def __init__(self, template_str: Optional[str] = None):
        self.template = template_str or self.DEFAULT_TEMPLATE

    def load(self) -> str:
        """Load the template string"""
        return self.template

    def save(self, filepath: str):
        """Save template to file"""
        try:
            with open(filepath, "w") as f:
                f.write(self.template)
            logger.info(f"Template saved to {filepath}")
        except Exception as e:
            logger.error(f"Failed to save template: {str(e)}")
            raise

    @classmethod
    def from_file(cls, filepath: str) -> "ReactAgentTemplate":
        """Load template from file"""
        try:
            with open(filepath, "r") as f:
                template_str = f.read()
            return cls(template_str)
        except Exception as e:
            logger.error(f"Failed to load template: {str(e)}")
            raise
