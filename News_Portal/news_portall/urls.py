from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostUpdate, PostDelete, ArticleCreate, ProtectedView

urlpatterns =[
    path('posts/', NewsList.as_view()),
    path('post/<int:pk>', NewsDetail.as_view(), name='default'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update', PostUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='article_delete'),
    path('protect/', ProtectedView.as_view(), name='protect'),

]