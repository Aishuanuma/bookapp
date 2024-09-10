from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    
    path('user/',views.bookTable1,name='user'),
    path('details1/<int:book_id>/',views.details1,name='details'),
    path('index1/',views.index1),
    path('search1/',views.search1,name='search'),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)