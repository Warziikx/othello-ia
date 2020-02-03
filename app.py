import json
from flask import Flask, render_template, send_from_directory, session, redirect, url_for, request
from src.game import Game

app = Flask(__name__)
app.secret_key = 'GwH!wXhhug#8G$j5$&pHGnat'


@app.route('/')
def index():
    return render_template('index.html')


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

    # création du nouveau jeu
    game = Game(size, size, None)
    game.start()
    turn = 1
    # ajout du novueau jeu en session
    session['game'] = game.to_json()
    session['turn'] = turn
    return redirect(url_for('play'))


@app.route('/game')
def play():
    username = request.args.get('username')
    turn = session['turn']
    data = json.loads(session['game'])
    game = Game(**data)
    # Traitement
    # Si il y'a une valeur
    if username is not None:
        turn = turn + 1

    # Après traitement
    session['game'] = game.to_json()
    session['turn'] = turn
    return render_template('game.html', board=game.board, turn=turn)


@app.route('/public/css/<path:path>')
def send_js(path):
    return send_from_directory('public/css', path)


if __name__ == '__main__':
    app.run()
