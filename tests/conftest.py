import pytest

from app import app


@pytest.fixture(scope="session")
def client():
    app.testing = True
    return app.test_client()


@pytest.fixture(scope="session")
def movie_factory():
    def _create_movie(**params):
        record = {
            "title": "Top Gun",
            "release_year": 1986,
            "description": "Naval fighter jets",
        }

        for key, value in params.items():
            if key in record:
                record[key] = value
        return record
    return _create_movie
