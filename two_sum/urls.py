from two_sum.views import CostingViewSet, NumbersViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'numbers', NumbersViewSet)
router.register(r'', CostingViewSet, basename='costing')
urlpatterns = router.urls
