from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Blogs, Bloggers, Comment


def index(request):
    return render(request, 'index.html', )


class BlogsListView(generic.ListView):
    model = Blogs
    paginate_by = 10


class BlogsDetailView(generic.DetailView):
    model = Blogs


class BloggersListView(generic.ListView):
    model = Bloggers
    paginate_by = 10


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description', ]

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['blogs'] = get_object_or_404(Blogs, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.bloggers = self.request.user
        form.instance.blogs = get_object_or_404(Blogs, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blogs-detail', kwargs={'pk': self.kwargs['pk'], })


class BlogsListbyBloggersView(generic.ListView):
    model = Blogs
    paginate_by = 10

    def get_queryset(self):
        id = self.kwargs['pk']
        target_bloggers = get_object_or_404(Bloggers, pk=id)
        return Blogs.objects.filter(bloggers=target_bloggers)

    def get_context_data(self, **kwargs):
        context = super(BlogsListbyBloggersView, self).get_context_data(**kwargs)
        context['bloggers'] = get_object_or_404(Bloggers, pk=self.kwargs['pk'])
        return context
