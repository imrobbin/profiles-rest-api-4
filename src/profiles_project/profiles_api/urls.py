from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    url('hello-view/', views.HelloApiView.as_view()),
    url('', include(router.urls))
]
