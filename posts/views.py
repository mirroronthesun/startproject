from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created_at')[:3]
    context = {'posts':posts}
    return render(request 'post/index.html', context)