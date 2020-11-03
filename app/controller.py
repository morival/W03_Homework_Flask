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
    return render_template('index.html', reply=reply, img_visibility=" visible")

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
    hand_icon1 = game.select_icon(player1)
    # hand_icon2 = game.select_icon(player2)
    return render_template('play-cpu.html', reply=reply, img_visibility=" visible", hand_icon1=hand_icon1)

# URL Form Page
@app.route('/<hand1>/<hand2>', methods=['GET'])
def play_game(hand1, hand2):
    player1 = Player("Player 1", hand1)
    player2 = Player("Player 2", hand2)
    game = Game(player1, player2)
    reply = game.play_new_game(player1, player2)
    return render_template('index.html', reply=reply)
    
