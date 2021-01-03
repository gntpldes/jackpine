from rest_framework import routers
from .api import FinanceViewSet

router = routers.DefaultRouter()
router.register('api/jpfinace', FinanceViewSet, 'Finance')

urlpatterns = router.urls