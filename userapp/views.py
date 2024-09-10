

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.db.models import Q
from bookapp.models import bookapp



def bookTable1(request):
    book=bookapp.objects.all()
    print(book)
    return render(request,'user/usertable.html',{'books':book})





    b=Book.objects.get(id=book_id)
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('author')
        price=request.POST.get('price')
        b.name=name
        b.author=author
        b.price=price
        b.save()
        return redirect('table')
    return render(request,'update.html',{'book1':b})


def details1(request,book_id):
    b=bookapp.objects.get(id=book_id)
    return render(request,'user/details1.html',{'book':b})

def index1(request):
    return render(request,'user/base1.html')

# def search(request):
#     query:None
#     books:None
#     if 'q' in request.GET:
#         query=request.GET.get('q')
#         books=Book.objects.filter(Q(name__icontains=query) | Q(author__icontains==query) | Q(price__icontains==query))
#     else:
#         books=[]
#     context={'books':books,'query':query}
#     return render(request,'search.html',context)
def search1(request):
    query = None
    books = []
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = bookapp.objects.filter(
            Q(name__icontains=query) | 
            Q(author__icontains=query) | 
            Q(price__icontains=query)
        )
    else:
        
        books=[]
    context = {'books': books, 'query': query}
    return render(request, 'user/usersearch.html', context)

