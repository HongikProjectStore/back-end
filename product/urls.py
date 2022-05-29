from rest_framework import routers
from .views import ProductViewSet

router = routers.SimpleRouter()
router.register('', ProductViewSet)

urlpatterns = router.urls
