
from django.urls import path
from .views import ListGoalsView

urlpatterns = [
    path('goals/',
        ListGoalsView.as_view(),
        name='goals-all'
    )
]
