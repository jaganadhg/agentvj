import pytest
from vj.tools.tool import CalculatorTool

def test_calculator_tool_execute():
    calculator = CalculatorTool()
    expression = "2 + 3"
    result = calculator.execute(expression)
    assert result == 5.0

def test_calculator_tool_invalid_expression():
    calculator = CalculatorTool()
    invalid_expression = "2 +"
    with pytest.raises(ValueError):
        calculator.execute(invalid_expression)
