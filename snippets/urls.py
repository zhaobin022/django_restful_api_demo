from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views as user_views
from snippets import views as snippets_views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', snippets_views.api_root),
    url(r'^snippets/$',
        snippets_views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        snippets_views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        snippets_views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        user_views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        user_views.UserDetail.as_view(),
        name='user-detail')
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]