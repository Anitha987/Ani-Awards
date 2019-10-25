from django.shortcuts import render
from .models import Project,Profile,User
from .forms import newPostForm,ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def get(request):
    images=Project.objects.all()
    return render(request,'my_awards/index.html',{"images":images})

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = newPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.Profile=profile
            image.save()
        return redirect('well')

    else:
        form = newPostForm()
    return render(request, 'new_post.html', {"form": form})


