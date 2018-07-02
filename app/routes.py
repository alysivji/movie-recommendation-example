from app import app

from .resources import (
    HealthCheck,
    UsersList,
    CreateUser,
    MoviesList,
    CreateMovie
)


app.add_url_rule("/health-check", view_func=HealthCheck.as_view("health_check"))

app.add_url_rule("/movies", view_func=MoviesList.as_view("movies_list"))
app.add_url_rule("/movies", view_func=CreateMovie.as_view("movies_post"))

app.add_url_rule("/users", view_func=UsersList.as_view("users_list"))
app.add_url_rule("/users", view_func=CreateUser.as_view("users_post"))
