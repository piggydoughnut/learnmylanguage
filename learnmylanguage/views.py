from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import api_view

from .models import Player, Game

from .credentials import *

import duolingo
lingo  = duolingo.Duolingo(duolingo_uname, duolingo_pwd)

def index(request):
    return render(request, 'learnmylanguage/index.html', {})

def game(request, game_id):
    return render(request, 'learnmylanguage/game.html', {})

def faq(request):
    return render(request, 'learnmylanguage/faq.html', {})

@api_view(['POST'])
def signup(request):
    # if request.data.get('player1') is None:
    #     return Response('Missing POST DATA', status=400)

    # try:
    u=request.data['player1']
    lingo.set_username(u['username'])
    streak=lingo.get_streak_info()
    info=lingo.get_language_details(u['language'])
    print(info)
    print(streak)

    p1=Player(
        username=u['username'],
        language=u['language'],
        email=u['email'],
        goal=streak['daily_goal'],
        streak=info['streak'],
        points=info['points']
    )
    p1.save()

    u=request.data['player2']
    lingo.set_username(u['username'])
    streak=lingo.get_streak_info()
    info=lingo.get_language_details(u['language'])

    p2=Player(
        username=u['username'],
        language=u['language'],
        email=u['email'],
        goal=streak['daily_goal'],
        streak=info['streak'],
        points=info['points']
    )
    p2.save()

    # except:
    #     return Response('Incorrect response', status=400)

    # game=Game()
    return HttpResponse('ya')

# Returns users currently studied languages
@api_view(['POST'])
def getlanguages(request):

    if request.data.get('username') is None:
        return Response('Missing POST DATA', status=400)

    u=request.data['username']
    lingo.set_username(u)

    try:
        r = lingo.get_languages()
        print(r)
    except:
        return Response('Incorrect response', status=400)
    return Response({'language_preference':r})
