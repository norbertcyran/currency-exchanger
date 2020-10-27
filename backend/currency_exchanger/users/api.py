from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'userinfo', views.UserInfoViewset)
