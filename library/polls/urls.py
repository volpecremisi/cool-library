from django.urls import path

from . import views

app_name = 'coolLibrary'
urlpatterns = [
    path('', views.IndexView.as_view(), name= 'index'),
    path('<int:pk>/', views.SelectionView.as_view(), name='selection'),
    path('authentication', views.AuthenticationView.as_view(), name='authentication'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<int:book_id>/checkLogin/', views.checkLogin, name='checkLogin'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('addNewUser/', views.addNewUser, name='addNewUser'),
    path('<int:book_id>/manageLoans/', views.manageLoans, name='manageLoans')
]