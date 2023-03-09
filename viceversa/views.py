from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	message = request.GET['message']
	return render(request, 'reverse.html', {'message': message[::-1]})