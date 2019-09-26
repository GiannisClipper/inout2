from django.urls import path
from . import views

urlpatterns = [
    # No trailing slash when url represent an action
    path('signup', views.signup, name='signup'),
    path('<int:id>/', views.Retrieve.as_view(), name='retrieve_user'),
]