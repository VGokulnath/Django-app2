from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),   #path for class based view
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('add',views.CreateItem.as_view(),name='create_item'), #add
    path('update/<int:id>/',views.update_item,name='update_item'), #update_item
    path('delete/<int:id>/',views.delete_item,name='delete_item'),


]