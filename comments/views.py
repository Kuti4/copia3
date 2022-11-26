from django.shortcuts import render, HttpResponseRedirect
from .models import Comment
from .forms import WriteCommentForm, DeleteCommentForm
from django.forms import CheckboxInput
# Create your views here.

def showcomments(request):
    comments = Comment.objects.all()[::-1]

    form = WriteCommentForm(request.POST)

    if request.user.is_superuser:
        deleteform = DeleteCommentForm()
    
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            #   ids = request.POST.getlist()
            comment.save()
            return HttpResponseRedirect(request.path)
        
        for i in Comment.objects.all():
            print((str(i.id)))
            if request.POST.get(str(i.id)):
                Comment.objects.filter(id=i.id).delete()
        comments = Comment.objects.all()
    else:
        form = WriteCommentForm()
    return render(request, 'comments/writecomment.html', {'comments' : comments, 'form' : form})
