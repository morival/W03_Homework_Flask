from flask import render_template, request
from app import app
from app.models.game import Game
from app.models.player import *
from random import *

# Welcome Page
@app.route('/')
def index():
    return render_template('welcome.html', title="Home")

# Play Against Yourself Page
@app.route('/play-yrs')
def start_playing():
    return render_template('index.html', title="Play Against Yourself", img_visibility=" hidden")

# Form Player vs Player Page
@app.route('/play-rps', methods=['POST'])
def play_rps():
    player1 = Player(request.form['player1'], request.form['choice1'])
    player2 = Player(request.form['player2'], request.form['choice2'])
    game = Game(player1, player2)
    reply = game.play_new_game(player1, player2)
    # RPS Image CSS properties
    cp1 = game.clip_path(player1)
    ml1 = game.margin_left(player1)
    mt1 = game.margin_top(player1)
    cp2 = game.clip_path(player2)
    ml2 = game.margin_left(player2)
    mt2 = game.margin_top(player2)
    return render_template('index.html', reply=reply, cp1=cp1, ml1=ml1, mt1=mt1, cp2=cp2, ml2=ml2, mt2=mt2)

# Play Against Computer Page
@app.route('/play-cpu')
def play_computer():
    return render_template('play-cpu.html', title="Play Against Computer", img_visibility=" hidden")

# Form Player vs Computer Page
@app.route('/play-rps-cpu', methods=['POST'])
def play_rps_cpu():
    player1 = Player(request.form['player1'], request.form['choice1'])
    player2 = Player('Computer', (["rock","paper","scissors"])[randrange(0, 3)])
    game = Game(player1, player2)
    reply = game.play_new_game(player1, player2)
    # RPS Image CSS properties
    cp1 = game.clip_path(player1)
    ml1 = game.margin_left(player1)
    mt1 = game.margin_top(player1)
    cp2 = game.clip_path(player2)
    ml2 = game.margin_left(player2)
    mt2 = game.margin_top(player2)
    return render_template('play-cpu.html', reply=reply, cp1=cp1, ml1=ml1, mt1=mt1, cp2=cp2, ml2=ml2, mt2=mt2)

# URL Form Page
@app.route('/<hand1>/<hand2>', methods=['GET'])
def play_game(hand1, hand2):
    player1 = Player("Player 1", hand1)
    player2 = Player("Player 2", hand2)
    game = Game(player1, player2)
    reply = game.play_new_game(player1, player2)
    return render_template('index.html', reply=reply)
    
