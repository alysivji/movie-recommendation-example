from app import app

from .api import HealthCheck


app.add_url_rule("/health-check/", view_func=HealthCheck.as_view("show_users"))
