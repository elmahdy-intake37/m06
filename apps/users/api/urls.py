from rest_framework import routers
from .views import TrackUserViews

app_name = 'track_users'
router = routers.DefaultRouter(trailing_slash=False)
router.register('', TrackUserViews, basename='track_users')



urlpatterns = router.urls
