from rest_framework import routers
from apps.products import api_views as product_views
from apps.products import swagger


router = routers.DefaultRouter()
router.register(r'product', product_views.ProductViewSet)
router.register(r'order', product_views.OrderViewSet)