from datetime import datetime

from app.schemas.movies import movies_post_schema

from hypothesis import given, strategies as st

CURRENT_YEAR = datetime.now().year


@given(
    title=st.text(),
    release_year=st.integers(max_value=CURRENT_YEAR),
    description=st.text(),
)
def test_movie_post_schema(title, release_year, description):
    record = {
        "title": title,
        "release_year": release_year,
        "description": description,
    }

    result = movies_post_schema.load(record)
    movie = result.data

    assert movie.title == title
    assert movie.release_year == release_year
    assert movie.description == description
