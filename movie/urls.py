from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch
app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
]

