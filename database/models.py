# database/models.py

from dataclasses import dataclass


@dataclass
class Achievement:
    name: str
    unlocked: bool

@dataclass
class Question:
    text: str
    answers: list[str]
    correct_feedback: str
    incorrect_feedback: str








