#!/usr/bin/env  python 
import subprocess
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass

from loguru import logger
from vj.agents.core import BaseAgent


class Tool:
    """
    Base class for agent tools
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the tool with given arguments
        """
        raise NotImplementedError


class CalculatorTool(Tool):
    """
    Tool for evaluating mathematical expressions using Linux bc calculator
    """

    def __init__(self):
        super().__init__(
            name="calculator",
            description="Evaluates mathematical expressions using Linux bc calculator",
        )

    def execute(self, expression: str) -> Any:
        """
        Execute mathematical calculation using bc

        Args:
            expression (str): Mathematical expression to evaluate

        Returns:
            float: Result of the calculation

        Raises:
            ValueError: If expression is invalid or calculation fails
        """
        try:
            # Create bc process with the expression
            process = subprocess.Popen(
                ["bc", "-l"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            # Send expression to bc and get result
            output, error = process.communicate(input=expression)

            if error or process.returncode != 0:
                raise ValueError(f"Calculation failed: {error}")

            # Convert result to float
            result = float(output.strip())
            return result

        except (subprocess.SubprocessError, ValueError) as e:
            raise ValueError(f"Failed to evaluate expression '{expression}': {str(e)}")
