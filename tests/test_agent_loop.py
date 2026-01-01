from app.agent.agent_loop import run_agent


def test_agent_loop_returns_answer_and_trace():
    answer, trace = run_agent(
        "How does Kubernetes RBAC authorize API requests?"
    )

    assert isinstance(answer, str)
    assert len(answer) > 50

    assert isinstance(trace, dict)
    assert trace["final_state"] == "answered"
    assert trace["plan"]["need_clarification"] is False
    assert "search_kubernetes_docs" in trace["plan"]["tools"]


def test_agent_loop_clarification_path():
    answer, trace = run_agent("How should this be handled?")

    assert isinstance(answer, str)
    assert "?" in answer

    assert trace["final_state"] == "clarification"
    assert trace["plan"]["need_clarification"] is True
    assert trace["plan"]["tools"] == []


def test_agent_loop_cross_domain_execution():
    answer, trace = run_agent(
        "If a cloud outage exposed user data, what GDPR obligations apply?"
    )

    assert isinstance(answer, str)
    assert "http" in answer  # citations preserved

    tools = trace["plan"]["tools"]
    assert isinstance(tools, list)
    assert len(tools) >= 1
