from django.shortcuts import render
from django.shortcuts import HttpResponse
from random import choice
# Create your views here.

def index(request):
    data = ["Pizza", "Pasta", "Bread", "Salad" "Sushi", "Jam", "Pie"]
    #data = []
    context = {"foods": data}
    return render(request, "sandbox/index.html", context=context)