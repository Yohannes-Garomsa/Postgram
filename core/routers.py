from rest_framework import routers
from rest_framework_nested import routers
from core.auth.viewsets import RegisterViewSet,LoginViewSet,RefreshTokenViewSet
# from core.auth.viewsets.login import LoginViewSet

from core.comment.viewsets import CommentViewSet
from core.user.viewsets import UserViewset
from core.post.viewsets import PostViewSet

router=routers.SimpleRouter()
#####USER###
router.register(r'auth/register',RegisterViewSet,basename='auth-register')
router.register(r'auth/login',LoginViewSet,basename='auth-login')
router.register(r'user',UserViewset,basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register')
router.register(r'auth/refresh', RefreshTokenViewSet, basename='auth-refresh')
router.register(r'post', PostViewSet, basename='post')
router.register(r'post', PostViewSet, basename='post')
posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment'   )



urlspatterns= [ 
               *router.urls,
               *posts_router.urls
               ]


##AUTH##
