import json

from flask import Flask, render_template, send_from_directory, session, redirect, url_for, request

from src.board import Board
from src.cell import WHITE, BLACK
from src.game import Game
from src.minmax import MinMax

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
    difficulty = int(request.form.get('difficulty')) if request.form.get('difficulty') is not None else 2
    # remove old game data
    if session.get('turn'):
        session.pop('turn')
    if session.get('game'):
        session.pop('game')
    if session.get('difficulty'):
        session.pop('difficulty')

    # création du nouveau jeu
    game = None
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
    x_played = request.args.get('x')
    y_played = request.args.get('y')
    turn = session['turn']
    data = json.loads(session['game'])
    game = Game(**data)
    game.board = Board(**game.board)
    # Traitement
    # Si il y'a une valeur
    if x_played is not None and y_played is not None:
        x_played = int(x_played)
        y_played = int(y_played)
        if game.board.is_valid_move(x_played, y_played, WHITE):
            game.board.make_move(x_played, y_played, WHITE)
            turn = turn + 1
            minmax = MinMax(game)
            (x, y) = minmax.best_move(BLACK)
            game.board.make_move(x, y, BLACK)
    game.board.get_playable()
    session['game'] = game.toJSON()
    session['turn'] = turn
    return render_template('game.html', board=game.board.board, turn=turn, difficulty=session['difficulty'])


@app.route('/public/css/<path:path>')
def send_css(path):
    return send_from_directory('public/css', path)


@app.route('/public/img/<path:path>')
def send_img(path):
    return send_from_directory('public/img', path)


if __name__ == '__main__':
    app.run()
