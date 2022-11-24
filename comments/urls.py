from django.urls import path
from comments.views import showcomments

urlpatterns = [
        path('comments/', showcomments, name='comments'),
]
