from django.shortcuts import render,redirect
from .models import Project,Profile,User
from .forms import newPostForm,ProfileForm,newReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
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
        return redirect('get')

    else:
        form = newPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=current_user).first()
    print(profile)
    images=Project.objects.filter(user=current_user)
    return render(request, 'my_awards/new_profile.html', {"images":images,"profile":profile})
  
@login_required(login_url='/accounts/login/')
def profile_form(request):
   current_user = request.user
   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
       if form.is_valid():
           profile = form.save(commit=False)
           profile.user = current_user
           profile.save()
       return redirect('profile')
   else:
       form = ProfileForm()
   return render(request, 'my_awards/profileform.html', {"form": form})


@login_required(login_url='/accounts/login/')
def review_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = newReviewForm(request.POST, request.FILES)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['usability_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review = form.save(commit=False)
            review.user = current_user
            review.Profile=profile
            review.save()
        return redirect('reviewform')

    else:
        form = newReviewForm()
    return render(request, 'new_post.html', {"form": form})   

