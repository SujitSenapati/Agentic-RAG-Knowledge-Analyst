"""
Utility helpers shared across the application.
Currently responsible for loading prompt templates from disk.
"""

from pathlib import Path


def load_prompt(name: str) -> str:
    """
    Load a prompt template from the prompts directory.

    Args:
        name (str): File name of the prompt (e.g., 'planner.txt')

    Returns:
        str: Prompt content as string
    """
    path = Path("prompts") / name
    return path.read_text(encoding="utf-8")



def load_urls(path: str) -> list[str]:
    """
    Load a list of URLs from a text file.

    :param path: Path to the file containing URLs, one per line
    :type path: str
    :return: List of URLs
    :rtype: list[str]
    """
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]