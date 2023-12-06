from rest_framework import routers
from apps.products import api_views as product_views


router = routers.DefaultRouter()
router.register(r'product', product_views.ProductViewSet)