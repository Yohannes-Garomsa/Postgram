from rest_framework import routers
from core.auth.viewsets import RegisterViewSet,LoginViewSet,RefreshTokenViewSet
# from core.auth.viewsets.login import LoginViewSet





from core.user.viewsets import UserViewset

router=routers.SimpleRouter()
#####USER###
router.register(r'auth/register',RegisterViewSet,basename='auth-register')
router.register(r'auth/login',LoginViewSet,basename='auth-login')
router.register(r'user',UserViewset,basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register')
router.register(r'auth/refresh', RefreshTokenViewSet, basename='auth-refresh')


urlspatterns= [ *router.urls,]


##AUTH##
