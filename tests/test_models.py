"""Smoke tests for the data access layer."""

from app import models


def test_fetch_questions_returns_iterable(monkeypatch):
    class FakeCursor:
        def __init__(self):
            self.data = iter([
                {
                    "question_id": 1,
                    "question_text": "Sample question?",
                    "category": "Sample",
                    "answer_id": 1,
                    "answer_text": "Answer",
                }
            ])

        def execute(self, *_args):
            return None

        def __iter__(self):
            return self

        def __next__(self):
            return next(self.data)

        def close(self):
            return None

    class FakeConnection:
        def cursor(self, **_kwargs):
            return FakeCursor()

        def close(self):
            return None

    def fake_get_connection(*_args, **_kwargs):
        class FakeContextManager:
            def __enter__(self):
                return FakeConnection()

            def __exit__(self, *_exc):
                return False

        return FakeContextManager()

    monkeypatch.setattr(models, "get_connection", fake_get_connection)

    questions = list(models.fetch_questions())
    assert len(questions) == 1
    assert questions[0].answers[0].answer_text == "Answer"
