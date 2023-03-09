from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	message = request.GET['message']
	count_words = len(message.split())
	return render(request, 'reverse.html', {'message': message[::-1]}, {'count_words': count_words})