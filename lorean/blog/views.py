from django.shortcuts import render

def base_start(request):
	return render(request , 'base.html')

def video(request):
	return render(request , 'blog/video.html')

def foto_vision(request):
	return render(request , 'blog/foto_vision.html')
