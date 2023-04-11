from django.urls import path,include
from .import views
from .views import Listsss

urlpatterns = [
    
    path('edit/',views.Listsss.as_view()),
    path('edit/<int:pk>',views.Listaaa.as_view()),
    # path('edit/',views.list),
    # path('edit/<int:pk>',views.lists),
    
   
]