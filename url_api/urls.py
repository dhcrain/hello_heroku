from django.conf.urls import include, url
from url_api.views import ClickAPIView, LinkAPIView

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^clicks/', ClickAPIView.as_view(), name='click-list'),
    url(r'^short_links/', LinkAPIView.as_view(), name='link-list')
]