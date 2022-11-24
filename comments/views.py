from django.shortcuts import render, HttpResponseRedirect
from .models import Comment
from .forms import WriteCommentForm
# Create your views here.

def showcomments(request):
    comments = Comment.objects.all()[::-1]
    form = WriteCommentForm(request.POST)
    
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()

            return HttpResponseRedirect(request.path)
    else:
        form = WriteCommentForm()
    return render(request, 'comments/writecomment.html', {'comments' : comments, 'form' : form})
