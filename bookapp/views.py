
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import bookapp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout

# Create your views here.
def createBook(request):
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('author')
        price=request.POST.get('price')
        image=request.FILES.get('image')
        
        if image:
            book = bookapp(name=name, author=author, price=price, image=image)
            book.save()
            return redirect('table')
        else:
            messages.error(request, "Image is required")
    return render(request,'admin/createbook.html')
    # if request.method=='POST':
    #     form=BookForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    # else:
    #     form=BookForm()
    # return render(request,'createbook.html',{'form':form})   

def bookTable(request):
    book=bookapp.objects.all()
    print(book)
    return render(request,'admin/booktable.html',{'books':book})


def deleteItem(request,book_id):
    book=bookapp.objects.get(id=book_id)
    if request.method=='POST':
        book.delete()
        return redirect('home')
    return render(request,'admin/deleteBook.html',{'book':book})

def updateBook(request,book_id):
    b=bookapp.objects.get(id=book_id)
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('author')
        price=request.POST.get('price')
        image=request.FILES.get('image')
        b.name=name
        b.author=author
        b.price=price
        if image:  # Only update image if a new one is provided
            b.image = image
        b.save()
        return redirect('table')
    return render(request,'admin/.html',{'book1':b})


def details(request,book_id):
    b=bookapp.objects.get(id=book_id)
    return render(request,'admin/details.html',{'book':b})

def index(request):
    return render(request,'admin/base.html')

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
def search(request):
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
    return render(request, 'admin/search.html', context)

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"this username is alredy exist")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"this email is exist")

            return redirect('login')
        else:
            messages.info("password is not match")
    return render(request,"admin/register.html")

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            auth_login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,"please provide correct details")
    return render(request,'admin/login.html')
def logout(request):
    auth_logout(request)
    return redirect('login')
def Homepage(request):
    return render(request,'admin/homepage.html')
