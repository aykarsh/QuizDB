"""Command-line entry point for the quiz application."""

from __future__ import annotations

import threading
import time
from typing import Iterable

from .models import Question, fetch_questions

TIMER_SECONDS = 20  # Five-minute quiz window


def countdown(stop_event: threading.Event) -> None:
    """End the quiz once the shared stop_event is set or the timer expires."""
    remaining = TIMER_SECONDS
    while remaining > 0 and not stop_event.is_set():
        time.sleep(1)
        remaining -= 1
    if not stop_event.is_set():
        print("\nTime up!\n")
        stop_event.set()


def ask_question(question: Question) -> bool:
    """Prompt the user for an answer and return True if they are correct."""
    print(f"\nQ{question.question_id}: {question.question_text}")
    response = input("Your answer: ").strip().lower()

    if not question.answers:
        print("No answers stored yet. Skipping.")
        return False

    accepted = {answer.answer_text.lower() for answer in question.answers}
    if response in accepted:
        print("Correct!\n")
        return True

    correct_answers = ", ".join(answer.answer_text for answer in question.answers)
    print(f"Incorrect. Acceptable answer(s): {correct_answers}\n")
    return False


def run_quiz(questions: Iterable[Question]) -> None:
    """Run the quiz loop with a shared timer."""
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=countdown, args=(stop_event,), daemon=True)
    timer_thread.start()

    score = 0
    total = 0

    for question in questions:
        if stop_event.is_set():
            break
        if ask_question(question):
            score += 1
        total += 1

    stop_event.set()
    timer_thread.join()

    if total == 0:
        print("No questions available. Add data to the database and try again.")
    else:
        print(f"Your score: {score}/{total}")


def main() -> None:
    questions = list(fetch_questions())
    run_quiz(questions)


if __name__ == "__main__":
    main()
