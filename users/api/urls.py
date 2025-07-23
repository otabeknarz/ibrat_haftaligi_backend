from rest_framework.routers import DefaultRouter

from users.api import views

router = DefaultRouter()
router.register("users", views.UserViewSet)
router.register("invitations", views.InvitationViewSet)

urlpatterns = router.urls
