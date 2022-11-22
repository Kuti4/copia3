from django.shortcuts import render
from .models import Comment
# Create your views here.
def showcomments(request):
    comments = Comment.objects.all()

    return render(request, 'comments/base.html', {'comments' : comments})
