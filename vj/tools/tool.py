#!/usr/bin/env  python
import subprocess
import math
import re
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass

from loguru import logger


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
        Execute mathematical calculation using Python's eval (with safety constraints)

        Args:
            expression (str): Mathematical expression to evaluate

        Returns:
            float: Result of the calculation

        Raises:
            ValueError: If expression is invalid or calculation fails
        """
        try:
            # Clean the expression - strip list enumeration if present
            expression = expression.strip()

            # Remove list notation prefix if present (e.g., "1. " or "2. ")
            if re.match(r"^\d+\.\s+", expression):
                expression = re.sub(r"^\d+\.\s+", "", expression)

            # Validate input (only allow basic math operations and numbers)
            if not re.match(r"^[\d\s\+\-\*\/\(\)\.\^\%\,]*$", expression):
                raise ValueError(
                    f"Expression contains invalid characters: '{expression}'"
                )

            # Create a safe environment with only math functions
            safe_dict = {
                "abs": abs,
                "round": round,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "pow": math.pow,
                "pi": math.pi,
                "e": math.e,
            }

            # Replace ^ with ** for exponentiation (common in calculators)
            expression = expression.replace("^", "**")

            # Evaluate the expression
            result = eval(expression, {"__builtins__": {}}, safe_dict)
            return float(result)

        except Exception as e:
            logger.error(f"Calculator error: {str(e)}")
            raise ValueError(f"Failed to evaluate expression '{expression}': {str(e)}")
