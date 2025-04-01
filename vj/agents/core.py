#!/usr/bin/env python

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from vj.tools.tool import Tool

from loguru import logger


class AgentMemory:
    """
    Handles agent's memory and conversation history
    """

    def __init__(self):
        self.steps = []
        self.conversation = []

    def add_step(self, step: dict):
        self.steps.append(step)

    def reset(self):
        self.steps = []
        self.conversation = []


class AgentMemory:
    """Handles agent's memory and conversation history"""

    def __init__(self):
        self.steps = []
        self.conversation = []

    def add_step(self, step: dict):
        self.steps.append(step)

    def reset(self):
        self.steps = []
        self.conversation = []


class BaseAgent(ABC):
    """
    Abstract base class for all AI agents
    """

    def __init__(
        self,
        tools: List[Tool],
        model: callable,
        max_steps: int = 10,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ):
        self.tools = {t.name: t for t in tools}
        self.model = model
        self.max_steps = max_steps
        self.name = name
        self.description = description
        self.memory = AgentMemory()
        self.current_step = 0

    @abstractmethod
    def generate_action(self, task: str) -> dict:
        """Generate next action based on current state"""
        pass

    @abstractmethod
    def execute_action(self, action: dict) -> Any:
        """Execute the generated action"""
        pass

    def run(self, task: str):
        """Main execution loop"""
        self.memory.reset()
        for step in range(self.max_steps):
            self.current_step = step
            try:
                action = self.generate_action(task)
                result = self.execute_action(action)
                if self.is_final_answer(result):
                    return result
                self.update_memory(action, result)
            except AgentError as e:
                logger.error(f"Step {step} failed: {str(e)}")
                break
        return None

    def update_memory(self, action: dict, result: Any):
        """Update agent memory with step results"""
        self.memory.add_step(
            {"step": self.current_step, "action": action, "result": result}
        )

    def is_final_answer(self, result: Any) -> bool:
        """Determine if result is a final answer"""
        return False


class AgentError(Exception):
    """Base class for agent exceptions"""

    pass


# Example Executor Implementations
class LocalExecutor:
    def execute(self, code: str) -> Any:
        # Implement safe code execution
        pass


class DockerExecutor:
    def execute(self, code: str) -> Any:
        # Implement Docker-based execution
        pass
