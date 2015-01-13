from django.views.generic import (
    ListView, View, DeleteView, UpdateView, CreateView
)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from google.appengine.api import users

from blog.core.models import Article, Blog
from blog.core.forms import ArticleForm, BlogForm


class BlogMixin(object):
    """
    Basic mixin for all the views. Update the context with additional
    information that is required across the whole site, typically
    to render base.html properly
    """
    def get_context_data(self, *args, **kwargs):
        context = super(BlogMixin, self).get_context_data(*args, **kwargs)
        blog = Blog.get_unique()
        context.update({
            'blog': blog,
            'active_user': users.get_current_user(),
            'is_admin': users.is_current_user_admin()
        })
        return context


class AdminRequiredMixin(object):
    """
    Mixin that redirects to the login page if users are not
    authenticated or they are not administrators
    """
    def get_after_login_url(self):
        return reverse('index')

    def dispatch(self, request, *args, **kwargs):
        if not users.is_current_user_admin():
            url = users.create_login_url(self.get_after_login_url())
            return HttpResponseRedirect(url)
        return super(AdminRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class LoginView(View):
    """
    A simple login page that uses Google App Engine authentication
    """
    def get(self, request):
        index = reverse('index')
        url = users.create_login_url(index)
        return HttpResponseRedirect(url)


class LogoutView(View):
    """
    A simple logout page that uses Google App Engine authentication
    """
    def get(self, request):
        index = reverse('index')
        url = users.create_logout_url(index)
        return HttpResponseRedirect(url)


class IndexView(BlogMixin, ListView):
    """
    The index page of the site. Contains the body and the titles of
    all the articles.
    """
    template_name = 'index.html'
    queryset = Article.objects.all().order_by('-created_at')


class ArticleAdminCreateView(AdminRequiredMixin, BlogMixin, CreateView):
    """
    Administration page to create articles.
    """
    template_name = 'form.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('index')


class BlogAdminUpdateView(AdminRequiredMixin, BlogMixin, UpdateView):
    """
    Administration page to update blog settings.
    """
    template_name = 'form.html'
    form_class = BlogForm

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return Blog.get_unique()


class ArticleAdminDeleteView(AdminRequiredMixin, BlogMixin, DeleteView):
    """
    Delete the article with a given key
    """
    model = Article
    template_name = 'article_confirm_delete.html'

    def get_success_url(self):
        return reverse('index')


class ArticleAdminUpdateView(AdminRequiredMixin, BlogMixin, UpdateView):
    """
    Administration page to update articles.
    """
    template_name = 'form.html'
    form_class = ArticleForm
    model = Article

    def get_success_url(self):
        return reverse('index')
