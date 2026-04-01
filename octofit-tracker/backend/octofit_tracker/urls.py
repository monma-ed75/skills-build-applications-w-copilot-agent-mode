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
import os
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
    # If running in a Codespace, prefer the canonical Codespace URL using
    # the CODESPACE_NAME environment variable. Otherwise fall back to the
    # request's absolute URI (usually localhost).
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base = f"https://{codespace}-8000.app.github.dev"
    else:
        base = request.build_absolute_uri('/')[:-1]

    return Response({
        'users': f"{base}/api/users/",
        'teams': f"{base}/api/teams/",
        'activities': f"{base}/api/activities/",
        'leaderboard': f"{base}/api/leaderboard/",
        'workouts': f"{base}/api/workouts/",
    })


# root should point to api_root
urlpatterns = [path('', api_root, name='api-root')] + urlpatterns
