from hypothesis import given, strategies as st

from app.constants import CURRENT_YEAR
from app.schemas.movies import movies_post_schema


#################
# Deserialization
#################
@given(
    title=st.text(),
    release_year=st.integers(max_value=CURRENT_YEAR),
    description=st.text(),
)
def test_post_schema_creating_new_movie(
    movie_factory, title, release_year, description
):
    """Test Happy Path"""
    # Arrange
    record = movie_factory(
        title=title, release_year=release_year, description=description
    )

    # Act
    result = movies_post_schema.load(record)

    # Assert
    assert len(result.errors) == 0

    movie = result.data
    assert movie.title == title
    assert movie.release_year == release_year
    assert movie.description == description


@given(release_year=st.integers(min_value=CURRENT_YEAR + 1))
def test_post_schema_error_creating_movie_after_current_year(
    movie_factory, release_year
):
    """Test inserting movie after current year"""
    record = movie_factory(release_year=release_year)

    result = movies_post_schema.load(record)

    assert len(result.errors) == 1
    assert "release_year" in result.errors


###############
# Serialization
###############
