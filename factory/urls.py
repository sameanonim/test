from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from factory.views import FactoryViewSet, IndividualEntrepreneurViewSet, RetailNetworkViewSet

router = routers.DefaultRouter()
router.register(r'factories', FactoryViewSet)
router.register(r'retail_networks', RetailNetworkViewSet)
router.register(r'individual_entrepreneurs', IndividualEntrepreneurViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]