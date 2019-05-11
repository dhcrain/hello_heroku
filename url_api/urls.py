from django.conf.urls import include, url
from rest_framework.authtoken import views

from url_api.views import ClickAPIView, LinkListCreateAPIView, LinkRetrieveAPIView, LinkUrlRetrieveAPIView, \
    ClickRetrieveAPIView

urlpatterns = [
    url(r'^clicks/$', ClickAPIView.as_view(), name='click-list'),
    url(r'^clicks/(?P<pk>\d+)/$', ClickRetrieveAPIView.as_view(), name='click-detail'),
    url(r'^short_links/$', LinkListCreateAPIView.as_view(), name='link-list'),
    url(r'^short_links/(?P<pk>\d+)/$', LinkRetrieveAPIView.as_view(), name='link-detail'),
    url(r'^short_links/d/(?P<hash_id>\w+)', LinkUrlRetrieveAPIView.as_view(), name='link-forward'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls'))
]
