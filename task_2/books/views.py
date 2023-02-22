from django.shortcuts import render, redirect
from django.urls import reverse

from books.models import Book


def index(request):
    return redirect(reverse('books'))


def books_view(request):
    template = 'books/index.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def book(request, pub_date):
    template = 'books/books_list.html'
    dict_book = Book.objects.order_by('pub_date').all()
    list_date = [str(book.pub_date) for book in dict_book]
    page = sorted(list(set(list_date)))
    page_back = page[page.index(pub_date) - 1]
    if page.index(pub_date) - 1 < 0:
        page_back = None
    try:
        page_to = page[page.index(pub_date) + 1]
    except:
        page_to = None
    page_start = list_date.index(pub_date)
    page_len = list_date.count(pub_date)
    aim_books = dict_book[page_start:page_start+page_len]
    context = {'books': aim_books,
               'page': pub_date,
               'page_to': page_to,
               'page_back': page_back}
    return render(request, template, context)
