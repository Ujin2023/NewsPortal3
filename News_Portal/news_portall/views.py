from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .filters import PostFilter
from .forms import PostFormCreateNews
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

class NewsList(ListView):
    model = Post
    template_name = 'default.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    

    

class NewsDetail(DetailView):
    model = Post
    template_name = 'default.html'
    cntext_object_name = 'post'

class PostCreate(CreateView):
    form_class = PostFormCreateNews
    model = Post
    template_name = 'news_create.html'

class PostUpdate(UpdateView):
    form_class = PostFormCreateNews
    model = Post
    template_name = 'news_update.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_create')

class ArticleCreate(CreateView):
    form_class = PostFormCreateNews
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save()
        if self.request.path == '/article/create/':
            post.snpost = 'stat'
        return super().form_valid(form)

class ArticleUpdate(UpdateView):
    form_class = PostFormCreateNews
    model = Post
    template_name = 'news_update.html'

class ArticleDelete(CreateView):
    form_class = PostFormCreateNews
    model = Post
    template_name = 'article_delete.html'

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protect.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return reverse_lazy('default')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name = 'author').exists()
        return context

class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('news_portal.add_post',
                           'news_portal.change_post')