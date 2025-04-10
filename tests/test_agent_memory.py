import pytest
from vj.agents.core import AgentMemory

def test_agent_memory_add_step():
    memory = AgentMemory()
    step = {"action": "test_action", "result": "test_result"}
    memory.add_step(step)
    assert len(memory.steps) == 1
    assert memory.steps[0] == step

def test_agent_memory_reset():
    memory = AgentMemory()
    step = {"action": "test_action", "result": "test_result"}
    memory.add_step(step)
    memory.reset()
    assert len(memory.steps) == 0
    assert len(memory.conversation) == 0
