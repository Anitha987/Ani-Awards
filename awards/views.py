from django.shortcuts import render
from django.contrib.auth.decorators import login_required.

# Create your views here.
@login_required(login_url='/accounts/login/')
def get(request):
    return render(request,'my_awards/index.html')

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


