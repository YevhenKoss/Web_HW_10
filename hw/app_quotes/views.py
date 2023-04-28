from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect

# Create your views here.
from .utils import get_mongo_db
from .models import Author, Quote, Tag
from .forms import QuoteForm, AuthorForm, TagForm


def main(request, page=1):
    db_quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(db_quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    top_tags = Quote.objects.values('tags__tag').annotate(quote_count=Count('tags__tag')).order_by('-quote_count')[:10]
    tag_name = []
    for tag in top_tags:
        tag_name.append(tag['tags__tag'])
    return render(request, "app_quotes/index.html", context={'quotes': page_obj, "top_ten_tags": tag_name})


def author_about(request, _id):
    print(_id)
    author = Author.objects.get(pk=_id)
    print(author.fullname, type(author))

    return render(request, 'app_quotes/author.html', context={'author': author})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="app_quotes:home")
        else:
            return render(request, "app_quotes/add_quote.html", context={'form': QuoteForm(), "message": "Form not valid"})
    return render(request, "app_quotes/add_quote.html", context={'form': QuoteForm()})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="app_quotes:home")
        else:
            return render(request, "app_quotes/add_author.html",
                          context={'form': AuthorForm(), "message": "Form not valid"})
    return render(request, "app_quotes/add_author.html", context={'form': AuthorForm()})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "app_quotes/add_tag.html", context={'form': TagForm(), "message": "Form not valid"})
    return render(request, "app_quotes/add_tag.html", context={'form': TagForm()})


def find_by_tag(request, _id):
    per_page = 10
    quotes = Quote.objects.filter(tags=_id).all()
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_tags = Quote.objects.values('tags__tag') \
                   .annotate(quote_count=Count('tags__tag')) \
                   .order_by('-quote_count')[:10]
    tag_name = []
    for tag in top_tags:
        tag_name.append(tag['tags__tag'])

    return render(request, "app_quotes/index.html", context={'quotes': page_obj,
                                                         "top_ten_tags": tag_name})
