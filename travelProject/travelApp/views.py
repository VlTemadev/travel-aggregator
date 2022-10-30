from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Category, About


# def home(request):
#     model = Post
#     posts = Post.objects.all().order_by('postDate')
#     return render(request, "index.html", {
#         'posts': posts
#     })


def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post-detail.html",{
        'post':post
    })


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"


class PostByCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context