from django.urls import path

from .views import AuthorListDetailsView, AuthorListView

app_name = 'authors'

urlpatterns = [
    path('', AuthorListView.as_view(), name='author_list'),
    path('<int:pk>/books/', AuthorListDetailsView.as_view(), name='author_details'),

]