from rest_framework.routers import SimpleRouter
from django.urls import path

from . import views

app_name = "posts_api"

# urlpatterns = [
#     path("users/", views.UserList.as_view(), name="specific_post"),
#     path("users/<int:pk>/", views.UserDetail.as_view(), name="specific_post"),
#     path("<int:pk>/", views.PostDetail.as_view(), name="specific_post"),
#     path("", views.PostsList.as_view(), name="all_post"),
# ]

router = SimpleRouter()
router.register("users", views.UserViewSet, basename="users_api")
router.register("", views.PostsViewSet, basename="posts_api")

urlpatterns = router.urls
