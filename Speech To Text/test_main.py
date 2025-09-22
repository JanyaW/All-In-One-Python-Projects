import main  
import speech_recognition
import pytest

def test_record_voice_returns_phrase(monkeypatch):
    """Test that record_voice returns the recognized phrase using mocked recognizer."""

    fake_phrase = "hello world"

    class FakeRecognizer:
        def adjust_for_ambient_noise(self, source):
            pass
        def listen(self, source):
            return "fake audio"
        def recognize_google(self, audio, language="en"):
            return fake_phrase

    class FakeMicrophone:
        def __enter__(self):
            return "fake mic"
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
