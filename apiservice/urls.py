from django.urls import path
from . import views

urlpatterns = [path("list_repositories/", views.GetRepositoriesView.as_view(), name="list_repositories")]
