from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.views.generic import TemplateView


from core import views

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^_ah/', include('djangae.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^add/$', views.ArticleAdminCreateView.as_view(), name='article_admin_create'),
    url(r'^manage-blog/$', views.BlogAdminUpdateView.as_view(), name='blog_admin_update'),
    url(r'^delete-article/(?P<pk>[\d]+)/$', views.ArticleAdminDeleteView.as_view(), name='article_admin_delete'),
    url(r'^update-article/(?P<pk>[\d]+)/$', views.ArticleAdminUpdateView.as_view(), name='article_admin_update'),
)


if not settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^500/$', TemplateView.as_view(template_name='500.html')),
        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    )
