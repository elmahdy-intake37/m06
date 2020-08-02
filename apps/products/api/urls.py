from rest_framework import routers
from .views import ProductOneViews, ProductTwoViews

app_name = 'products'
router = routers.DefaultRouter(trailing_slash=False)
router.register('one/', ProductOneViews, basename='product_one')
router.register('two/', ProductTwoViews, basename='product_two')



urlpatterns = router.urls
