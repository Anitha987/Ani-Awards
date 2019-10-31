from django.shortcuts import render,redirect
from .models import Project,Profile,User
from .forms import newPostForm,ProfileForm,newReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status

# Create your views here.
@login_required(login_url='/accounts/login/')
def get(request):
    current_user = request.user
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
def rating(request):
    current_user = request.user
    project=Project.objects.filter(user=current_user).first()
    rating = round(((project.design + project.usability + project.content)/3),1)
    if request.method == 'POST':
        form = newReviewForm(request.POST)
        if form.is_valid:
            # project.vote_submissions += 1
            project = form.save(commit=False)

            if project.design == 0:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 0:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 0:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
            return redirect('get')
    else:
        form = newReviewForm()
    return render(request,'voteform.html',{'form':form,'project':project,'rating':rating})    

class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        merch = Project.objects.all()
        serializer = ProjectSerializer(get_merch, many=True)
        return Response(serializer.data)