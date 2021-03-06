
from django.urls import path
from api.views import (
    ListTaskView, ListUserView,
    ListRoadMapView, ListJourneyView,
    UserDataView
)

urlpatterns = [
    path(
        'tasks/',
        ListTaskView.as_view(),
        name='task-all'
    ),
    path(
        'users/',
        ListUserView.as_view(),
        name='user-all'
    ),
    path(
        'roadmaps/',
        ListRoadMapView.as_view(),
        name='roadmap-all'
    ),
    path(
        'journeys/',
        ListJourneyView.as_view(),
        name='journey-all'
    ),
    path(
        'users/me',
        UserDataView.as_view(),
        name='user-data'
    )
]
