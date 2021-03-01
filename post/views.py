from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
# Post
class PostObjectMixin(object):
    model = Post
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj

# we need to add by default user who is loged in as user_who_posted the same thing need to be done for
# comment too, also we need to add default post when comment 
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post/post_create.html'
    model = Post
    form_class = PostForm # this works good but overriden because we need both get and post
    def form_valid(self, form):
        form.instance.user_who_posted_id = self.request.user.user_id  # this should work fine
        return super().form_valid(form)

class PostUpdateView(PostObjectMixin, UpdateView):
    model = Post
    template_name = 'post/post_update.html'
    form_class = PostForm
    # success_url = reverse_lazy('post:post-detail', kwargs={"pk": self.pk})

class PostDeleteView(PostObjectMixin, DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home_view')

class PostDetailView(PostObjectMixin, DetailView):
    model = Post
    # form_class = PostModelForm
    template_name = 'post/post_detail.html'

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'

# Comment
class CommentObjectMixin(object):
    model = Comment
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj

class CommentCreateView(CreateView):
    # model = Post
    template_name = 'post/comment_create.html'
    form_class = CommentForm # this works good but overriden because we need both get and post
    # note that we need to take user_who_posted as current user_id by default the same thing for comment
    model = Comment
    def form_valid(self, form):
        form.instance.user_id = self.request.user  # this should work fine
        form.instance.on_post = Post.objects.get(post_id=self.request.POST['post_id'])
        return super().form_valid(form)
    # adding post id to context so it can be fetched for adding it into comment
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs['post_id']
        return context

class CommentUpdateView(CommentObjectMixin, UpdateView):
    model = Comment
    template_name = 'post/comment_update.html'
    form_class = CommentForm
    # success_url = reverse_lazy('comment:comment-detail', kwargs={"pk": self.pk})

class CommentDeleteView(CommentObjectMixin, DeleteView):
    model = Comment
    template_name = 'post/comment_delete.html'
    success_url = reverse_lazy('home_view') # try to replace this static url

class CommentListView(ListView):
    model = Comment
    template_name = 'post/comment_list.html'
    # queryset = Comment.objects.filter(on_post=self.kwargs['post_id'])
    def get_queryset(self):
        self.post_id = self.kwargs['post_id']
        return Comment.objects.filter(on_post=self.post_id)

class CommentDetailView(CommentObjectMixin, DetailView):
    model = Comment
    # form_class = PostModelForm
    template_name = 'post/comment_detail.html'
