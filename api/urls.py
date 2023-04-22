from django.urls import path,include
from .import views
from .views import Listsss

# from .views import ItemsViewSet
# from rest_framework import routers

urlpatterns = [
    
    path('edit/',views.Listsss.as_view()),
    path('edit/<int:pk>',views.Listaaa.as_view()),
    # path('edit/',views.list),
    # path('edit/<int:pk>',views.lists),
      
]

## viewsets api

# router = routers.DefaultRouter()
# router.register('viewset', ItemsViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]