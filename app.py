import json
from flask import Flask, render_template, send_from_directory, session, redirect, url_for, request

from src.board import Board
from src.game import Game
from src.cell import Cell, EMPTY, WHITE, BLACK, PLAYABLE

Difficulty = {2: 'Facile', 4: 'Normal', 6: 'Difficile'}

app = Flask(__name__)
app.secret_key = 'GwH!wXhhug#8G$j5$&pHGnat'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/store')
def store():
    return render_template('store.html')


@app.route('/new', methods=["POST"])
def new():
    # recupération des parametres du form ou assignation par défault
    size = int(request.form.get('size')) if request.form.get('size') is not None else 8
    difficulty = int(request.form.get('difficulty')) if request.form.get('difficulty') is not None else 3
    # remove old game data
    if session.get('turn'):
        session.pop('turn')
    if session.get('game'):
        session.pop('game')
    if session.get('difficulty'):
        session.pop('difficulty')

    # création du nouveau jeu
    game = Game(size, None, difficulty)
    game.start()
    turn = 1
    # ajout du novueau jeu en session
    session['difficulty'] = Difficulty[difficulty]
    session['game'] = game.toJSON()
    session['turn'] = turn
    return redirect(url_for('play'))


@app.route('/game')
def play():
    xPlayed = request.args.get('x')
    yPlayed = request.args.get('y')
    turn = session['turn']
    data = json.loads(session['game'])
    game = Game(**data)
    game.board = Board(**game.board)
    # Traitement
    # Si il y'a une valeur
    if xPlayed is not None and yPlayed is not None:
        xPlayed = int(xPlayed)
        yPlayed = int(yPlayed)
        if game.board.is_valid_move(xPlayed, yPlayed, WHITE):
            game.board.make_move(xPlayed, yPlayed, WHITE)
            turn = turn + 1
    # Après traitement
    session['game'] = game.toJSON()
    session['turn'] = turn
    print(game.board.board)
    return render_template('game.html', board=game.board.board, turn=turn, difficulty=session['difficulty'])


@app.route('/public/css/<path:path>')
def send_css(path):
    return send_from_directory('public/css', path)


@app.route('/public/img/<path:path>')
def send_img(path):
    return send_from_directory('public/img', path)


if __name__ == '__main__':
    app.run()
