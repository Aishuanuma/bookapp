from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('',views.createBook,name='home'),
    path('table/',views.bookTable,name='table'),
    path('delete/<int:book_id>/', views.deleteItem, name='delete'),
    path('update/<int:book_id>/',views.updateBook,name='update'),
    path('details/<int:book_id>/',views.details,name='details'),
    path('index/',views.index),
    path('search/',views.search,name='search'),
    path('register/',views.register),
    path('login/',views.login,name='login'),
    path('homepage/',views.Homepage,name='homepage'),
    path('logout/',views.logout,name='logout'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)