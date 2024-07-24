from django.urls import path
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'posts', views.UserViewSet)
# router.register(r'posts', views.ExampleView)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', views.PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>', views.PostUpdateDestroy.as_view(), name='post-update-destroy'),
]