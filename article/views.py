from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn, ArticlePost
# 9月13日0.2版本
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import ArticleColumnForm, ArticlePostForm
# 9月14日0.3版本
from django.views.decorators.http import require_POST
# Create your views here.


# @login_required(login_url='/account/login/')
# def article_column(request):
#     """
#     9月12日0.1版本代码， 可run
#     :param request:
#     :return:
#     """
#     columns = ArticleColumn.objects.filter(user=request.user)
#     return render(request, "article/column/article_column.html", {"columns": columns})

@login_required(login_url='/account/login/')
@csrf_exempt   # 可以解決提交表單時遇到的csrf錯誤
def article_column(request):
    """
    9月13日0.2版本代码， 可run
    :param request:
    :return:
    """
    if request.method == "GET":

        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()              # 创建表单类实例对象
        return render(request, "article/column/article_column.html", {"columns": columns, 'column_form': column_form})
    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)

        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("1")


# 9月14日 0.3版本
@require_POST   # 保证此视图函数只接受通过post方式提交的数据
@login_required(login_url='/account/login/')
@csrf_exempt   # 可以解決提交表單時遇到的csrf錯誤
def rename_article_column(request):
    column_name = request.POST["column_name"]
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")


@require_POST   # 保证此视图函数只接受通过post方式提交的数据
@login_required(login_url='/account/login/')
@csrf_exempt   # 可以解決提交表單時遇到的csrf錯誤
def del_article_column(request):
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


@login_required(login_url='/account/login')
@csrf_exempt
def article_post(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return render(request, "article/column/article_post.html", {"article_post_form": article_post_form, "article_columns":article_columns})