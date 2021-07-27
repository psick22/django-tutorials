from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book


def first(request):
    return HttpResponse('First message from views')


class Another(View):
    books = Book.objects.filter(is_published=True)
    output = ''
    for book in books:
        output += f"We have {book.title}({book.price}) with ID-{book.pk} in DB<br>"

    def get(self, request):
        return HttpResponse(self.output)
