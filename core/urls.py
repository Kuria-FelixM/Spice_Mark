from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'taxes', TaxViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'refunds', RefundViewSet)
router.register(r'ordersitems', OrderItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'analytics', AnalyticsViewSet)
router.register(r'shippings', ShippingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]