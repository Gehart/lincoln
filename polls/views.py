from .forms import CommentForm
from .models import Post, Tag, Comment
from .utils import ObjectDetailMixin

from django.http import Http404, JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from users.models import CustomUser



class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'polls/tag_detail.html'


class PostDetail(View):
    template_name = 'polls/post_detail.html'
    form_class = CommentForm()
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        comment = Comment.objects.all().filter(is_enable=True,
                                               parent_comment_id=None)
        context = {
            'post': post,
            'comment': comment,
            'form_class': self.form_class
        }
        return render(
            request, template_name=self.template_name, context=context)

    def post(self, request, slug):
        if request.method == 'POST':
            comment = Comment.objects.all().filter(is_enable=True,
                                                   parent_comment_id=None)
            form = CommentForm(request.POST)
            post = get_object_or_404(Post, slug__iexact=slug)
            if form.is_valid():
                perent = request.POST.get('comments_id')
                comments_qs = None
                if perent:
                    comments_qs = perent
                comment_to = Comment(
                    parent_comment_id = comments_qs,
                    article_id=post.id,
                    author_id=request.user.id,
                    body=form.cleaned_data['body'])
                comment_to.save()
        else:
            form = CommentForm()

        context = {
            'post': post,
            'comment': comment,
            'form_class': self.form_class
        }

        # ЕСЛИ АЯКС ЗАПРОС
        if request.is_ajax():
            # В ПЕРЕМЕННУЮ ДОБАВЛЯЕМ УЧАСТОК ВЕРСКИ, КОТОРОЙ НЕОБХОДИМО
            # ОБНОВИТЬ
            html = render_to_string('polls/includes/comments.html',
                                    context, request=request)
            # ВОЗВРАЩАЕМ ОБНОВЛЕННУЮ СТРАНИЦУ
            return JsonResponse({'forms': html})
        return render(
            request, template_name=self.template_name, context=context)

@login_required
def comment_remove(request, slug, pk):
    post = get_object_or_404(Post, slug__iexact=slug)
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.id == comment.author.id:
        comment.delete()
    else:
        raise Http404()

    return redirect('polls:post_detail_url', slug=post.slug)

# Отображение постов
def index(request):
    postsB = Post.objects.all().filter(publicate_in="B")



    posts = Post.objects.all().filter(publicate_in="L")
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'postsB': postsB,
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }
    return render(request, 'polls/index.html', context=context)

def serchArticles(request):
    search_query = request.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) |
                                    Q(body__icontains=search_query))

        tags = Tag.objects.filter(Q(title__icontains=search_query))
        context = {
            'posts': posts,
            'tags': tags
        }
    else:
        context = None
    return render(request, 'polls/search_article.html', context=context)

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'polls/tags_list.html', context={'tags': tags})
