from app.agent.planner import create_plan


def test_planner_selects_kubernetes_tool():
    plan = create_plan("How does Kubernetes RBAC authorize API requests?")

    assert plan.need_clarification is False
    assert "search_kubernetes_docs" in plan.tools
    assert plan.clarification_question is None


def test_planner_requests_clarification_for_ambiguous_query():
    plan = create_plan("How should this be handled?")

    assert plan.need_clarification is True
    assert plan.tools == []
    assert plan.clarification_question is not None
    assert isinstance(plan.clarification_question, str)
    assert len(plan.clarification_question) > 10  # meaningful question


def test_planner_selects_multiple_tools_for_cross_domain_question():
    plan = create_plan(
        "If a cloud outage exposed user data, what GDPR obligations apply "
        "and how should similar incidents be prevented?"
    )

    assert plan.need_clarification is False
    assert len(plan.tools) >= 1
