from database.models import Question


class Quiz:

    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def get_current_question(self) -> Question:
        return self.questions[self.current_question]

    def check_answer(self, user_answer: str) -> bool:
        current = self.get_current_question()
        is_correct = user_answer.lower() in [a.lower() for a in current.answers]
        if is_correct:
            self.score += 1
        return is_correct

    def next_question(self) -> bool:
        self.current_question += 1
        return self.current_question < len(self.questions)

    def get_result(self) -> tuple[int, int]:
        return self.score, len(self.questions)

