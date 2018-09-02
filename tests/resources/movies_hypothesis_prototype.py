# trying out property based testing, really slow

from datetime import datetime
import json

from hypothesis import given, strategies as st

from app.resources.movies import MoviesPost
from app import db

# calculating constants
CURRENT_YEAR = datetime.now().year


@given(
    title=st.text(),
    release_year=st.integers(max_value=CURRENT_YEAR),
    description=st.text(),
)
def test_post_success(movie_factory, title, release_year, description):
    """Test Happy Path"""
    # Arrange
    record = movie_factory(
        title=title, release_year=release_year, description=description
    )
    db.session.begin_nested()

    # Act
    create_movie_view = MoviesPost()
    result = create_movie_view.dispatch_request(injected_data=record)

    # cleanup
    db.session.rollback()

    # Assert
    assert result.status_code == 201
    movie = json.loads(result.json)

    assert "errors" not in movie
    assert movie["title"] == title
    assert movie["release_year"] == release_year
    assert movie["description"] == description


@given(release_year=st.integers(min_value=CURRENT_YEAR + 1))
def test_post_movie_after_current_year_error(movie_factory, release_year):
    """Test inserting movie after current year"""
    # Arrange
    record = movie_factory(release_year=release_year)

    # Act
    create_movie_view = MoviesPost()
    result = create_movie_view.dispatch_request(injected_data=record)

    # Assert
