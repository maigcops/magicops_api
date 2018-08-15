from rest_framework import routers
from magicops_api.v1 import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
