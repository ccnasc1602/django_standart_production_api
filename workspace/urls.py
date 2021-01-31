from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyView)
router.register(r'operator', views.OperatorView)
router.register(r'person', views.PersonView)
router.register(r'group-product', views.GroupProductsView)

urlpatterns = [
    path('api/', include(router.urls)),
]
