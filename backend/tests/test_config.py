from app.config import settings


def test_default_settings():
    assert settings.app_name == "LinkScope API"
    assert settings.environment == "development"
    assert settings.cors_origins == "http://localhost:3000"