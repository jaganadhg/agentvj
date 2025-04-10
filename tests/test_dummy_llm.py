import pytest
from test_code import DummyLLM

def test_dummy_llm_generate():
    llm = DummyLLM()
    response = llm.generate("Test prompt")
    assert "text" in response
    assert "confidence" in response
    assert "tokens_used" in response
    assert "finish_reason" in response
    assert 0.3 <= response["confidence"] <= 0.9
    assert 10 <= response["tokens_used"] <= 50

def test_dummy_llm_batch_generate():
    llm = DummyLLM()
    prompts = ["Prompt 1", "Prompt 2"]
    responses = llm.batch_generate(prompts)
    assert len(responses) == len(prompts)
    for response in responses:
        assert "text" in response
        assert "confidence" in response
        assert "tokens_used" in response
        assert "finish_reason" in response
        assert 0.3 <= response["confidence"] <= 0.9
        assert 10 <= response["tokens_used"] <= 50
