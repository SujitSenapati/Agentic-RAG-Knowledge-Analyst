"""
Tool registry for agent tool discovery.

Responsibilities:
- Maintain a central registry of all tools
- Store tool metadata (description, domains)
- Enable planner-driven dynamic tool invocation
"""

from typing import Callable, Dict, List

TOOL_REGISTRY: Dict[str, Dict] = {}


def register_tool(name: str, description: str, domains: List[str]):
    """
    Decorator to register a function as an agent tool.

    Args:
        name: Tool name referenced by the planner
        description: Natural language description of tool capability
        domains: Keywords describing tool domain knowledge
    """
    def decorator(func: Callable):
        TOOL_REGISTRY[name] = {
            "func": func,
            "description": description.strip(),
            "domains": domains,
        }
        return func
    return decorator
