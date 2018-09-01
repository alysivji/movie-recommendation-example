from app import app

from .resources import HealthCheck, UsersList, UsersPost, MoviesList, MoviesPost


app.add_url_rule("/health-check", view_func=HealthCheck.as_view("health_check"))

app.add_url_rule("/movies", view_func=MoviesList.as_view("movies_list"))
app.add_url_rule("/movies", view_func=MoviesPost.as_view("movies_post"))

app.add_url_rule("/users", view_func=UsersList.as_view("users_list"))
app.add_url_rule("/users", view_func=UsersPost.as_view("users_post"))
