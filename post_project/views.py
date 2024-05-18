from django.shortcuts import render

# Create your views here.
def post_project(request):
    return render(request, "post_project/postproject.html")
