from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def main_view(request):
    return render(request, 'main/main.html')

