from rest_framework import routers
from core.auth.viewsets.register import RegisterViewSet





from core.user.viewsets import UserViewset

router=routers.SimpleRouter()
#####USER###

router.register(r'user',UserViewset,basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register')


urlspatterns= [ *router.urls,]

##AUTH##
