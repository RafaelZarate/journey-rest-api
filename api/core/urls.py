
from django.urls import path
from core.views import (
    ListGoalsView, ListUserView,
    ListRoadMapView
)

urlpatterns = [
    path(
        'goals/',
        ListGoalsView.as_view(),
        name='goals-all'
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
    )
]
