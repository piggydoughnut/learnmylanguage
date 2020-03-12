from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'learnmylanguage/index.html', {})

def signup(request):
    return HttpResponse('You are signing up.')

def game(request, game_id):
    return HttpResponse('Your gaming number is' + str(game_id))

def faq(request):
    return render(request, 'learnmylanguage/faq.html', {})
