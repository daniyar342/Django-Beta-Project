from rest_framework import routers
from apps.products import api_views as product_views
from apps.products.api_views import *
from apps.blog.views import *
from apps.products import swagger


router = routers.DefaultRouter()
router.register(r'product', product_views.ProductViewSet)
router.register(r'order', product_views.OrderViewSet)
router.register(r'blog_events', BlogEventsView)
router.register(r'public_blog', PublicBlogView)
router.register(r'product', ProductRetrieveView, basename='your-model')


