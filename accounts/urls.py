from django.conf.urls import url
from .views import UserList, UserDetail

urlpatterns = [
    url(r'users/', UserList.as_view(), name='user-list'),
    url(r'users/update/<int:id>', UserDetail.as_view(), name='user-update')
]