from django.conf.urls import include, url
from url_api.views import ClickAPIView, LinkAPIView, LinkRetrieveAPIView, ClickRetrieveAPIView

urlpatterns = [
    url(r'^clicks/$', ClickAPIView.as_view(), name='click-list'),
    url(r'^clicks/(?P<pk>\d+)/$', ClickRetrieveAPIView.as_view(), name='click-detail'),
    url(r'^short_links/$', LinkAPIView.as_view(), name='link-list'),
    url(r'^short_links/(?P<pk>\d+)/$', LinkRetrieveAPIView.as_view(), name='link-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/api-token-auth/', views.obtain_auth_token),
]
