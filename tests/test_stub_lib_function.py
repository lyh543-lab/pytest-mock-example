from app.greetings import get_greeting_string


def test_get_greeting_string():
    assert get_greeting_string() == 'Greetings, user'
