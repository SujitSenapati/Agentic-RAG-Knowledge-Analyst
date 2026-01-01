from app.agent.judge import judge_answer


def test_judge_approves_grounded_answer():
    verdict = judge_answer(
        question="What is Kubernetes RBAC?",
        answer="Kubernetes RBAC controls access using Roles and RoleBindings "
               "(https://kubernetes.io/docs/reference/access-authn-authz/rbac/).",
        evidence="Kubernetes RBAC documentation ..."
    )

    assert verdict["score"] >= 0.7
    assert verdict["verdict"] == "approve"
