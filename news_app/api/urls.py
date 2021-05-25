from django.urls import path
from news_app.api.views import  (ArticleListCreateAPIView, ArticleDetailAPIView)

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('article/<int:pk>', ArticleDetailAPIView.as_view(), name='article-detail')
]