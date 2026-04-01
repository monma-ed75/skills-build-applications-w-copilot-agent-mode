"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # API routes
    path('api/', include(([
        # router will be attached below
    ], 'api'))),
]

# Register viewsets via a router to expose REST endpoints
router = routers.DefaultRouter()
router.register(r'users', tracker_views.TrackerUserViewSet)
router.register(r'teams', tracker_views.TeamViewSet)
router.register(r'activities', tracker_views.ActivityViewSet)
router.register(r'leaderboard', tracker_views.LeaderboardViewSet)
router.register(r'workouts', tracker_views.WorkoutViewSet)

# append router URLs
urlpatterns += [path('api/', include(router.urls))]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'teams': reverse('teams-list', request=request, format=format),
        'activities': reverse('activities-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workouts-list', request=request, format=format),
    })


# root should point to api_root
urlpatterns = [path('', api_root, name='api-root')] + urlpatterns
