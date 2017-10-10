import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from short_app.models import Bookmark, Click
from short_app.forms import BookmarkCreateForm


class IndexView(ListView):
    model = Bookmark
    template_name = 'index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context["form"] = BookmarkCreateForm()
        return context


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login_view')


class ProfileView(CreateView):
    template_name = 'profile.html'
    model = Bookmark
    fields = ['title', 'url', 'description']
    success_url = reverse_lazy('profile_view')

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context["bookmark"] = Bookmark.objects.filter(user_id=self.request.user)
            context["form"] = BookmarkCreateForm()
        else:
            context["bookmark"] = Bookmark.objects.all()
        return context


class UserProfileView(ListView):
    model = Bookmark
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        user_id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["bookmark"] = Bookmark.objects.filter(user_id=user_id)
        context["form"] = BookmarkCreateForm()
        return context


class ShortenLink(CreateView):
    model = Bookmark
    fields = ['title', 'url', 'description']
    success_url = reverse_lazy('profile_view')

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        return super(ShortenLink, self).form_valid(form)


class ForwardView(View):

    def get(self, request, *args, **kwargs):
        hash_id = self.kwargs.get('hash_id', None)      # gets hash_id
        link = Bookmark.objects.get(hash_id=hash_id)    # looks up the link from the hash_id
        Click.objects.create(link=link, time_click=datetime.datetime.now())
        return HttpResponseRedirect(link.url)


class EditBookmark(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url', 'description']
    success_url = reverse_lazy('profile_view')
    template_name = 'update.html'


class LinkDelete(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('profile_view')

    def get_object(self, queryset=None):
        link = super(LinkDelete, self).get_object()
        if not link.user == self.request.user:
            raise Http404
        hashid = Bookmark.objects.get(id=link.id)
        self.hashid = hashid
        return link


# class ClickView(TemplateView):
#     model = Click
#     template_name = "short_app/click_list.html"
#
#     def get_context_data(self, **kwargs):
#         bookmark_pk = self.kwargs.get('pk')
#         context = super().get_context_data(**kwargs)
#         context["bookmark"] = Bookmark.objects.get(id=bookmark_pk)
#         context["clicks"] = Click.objects.filter(link=bookmark_pk)
#         return context


class BookmarkView(ListView):
    model = Bookmark


class UserView(ListView):
    model = User
