"""Data access layer for questions and answers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .db import get_connection


@dataclass
class Answer:
    answer_id: int
    question_id: int
    answer_text: str


@dataclass
class Question:
    question_id: int
    question_text: str
    category: str | None
    answers: Sequence[Answer]


def fetch_questions(limit: int | None = None) -> Iterable[Question]:
    """Return questions and their answers."""
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        try:
            sql = (
                "SELECT q.question_id, q.question_text, q.category, "
                "a.answer_id, a.answer_text "
                "FROM questions q "
                "LEFT JOIN answers a ON q.question_id = a.question_id "
                "ORDER BY q.question_id"
            )
            if limit is not None:
                sql += " LIMIT %s"
                cursor.execute(sql, (limit,))
            else:
                cursor.execute(sql)

            grouped: dict[int, Question] = {}
            for row in cursor:
                answer = None
                if row["answer_id"] is not None:
                    answer = Answer(
                        answer_id=row["answer_id"],
                        question_id=row["question_id"],
                        answer_text=row["answer_text"],
                    )

                if row["question_id"] not in grouped:
                    grouped[row["question_id"]] = Question(
                        question_id=row["question_id"],
                        question_text=row["question_text"],
                        category=row["category"],
                        answers=[],
                    )

                if answer:
                    grouped[row["question_id"]].answers.append(answer)

            return grouped.values()
        finally:
            cursor.close()
