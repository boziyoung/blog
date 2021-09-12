from django.shortcuts import render, get_object_or_404
# 需要对那个数据库对象进行操作就导入那个数据库的model
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    # render() 将数据渲染到指定模板上
    return render(request, 'blog/titles.html', {'blogs': blogs})


def blog_article(request, article_id):
    """请求具体的每篇文章"""
    # article = BlogArticles.objects.get(id=article_id)
    # 改进查询错误时的页面显示优化
    article = get_object_or_404(BlogArticles, id=article_id)

    pub = article.publish
    return render(request, 'blog/content.html', {"article": article, "publish": pub})
# Create your views here.
