from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request,'home.html') #use django render function instead of creating own HttpResponse

