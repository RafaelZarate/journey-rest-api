
from django.urls import path
from core.views import ListGoalsView, ListUserView

urlpatterns = [
    path(
        'goals/',
        ListGoalsView.as_view(),
        name='goals-all'
    ),
    path(
        'users/',
        ListUserView.as_view(),
        name='user-all')
]
