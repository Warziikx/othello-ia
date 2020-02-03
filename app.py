import json
from flask import Flask, render_template, send_from_directory, session
from collections import namedtuple

from src.game import Game

app = Flask(__name__)
app.secret_key = 'GwH!wXhhug#8G$j5$&pHGnat'


@app.route('/')
def play():
    if session.get('turn'):
        turn = session['turn']
        data = json.loads(session['game'])
        game = Game(**data)
    else:
        game = Game(8, 8, None)
        game.start()
        turn = 0
    # Traitement

    # Après traitement
    turn = turn + 1
    session['game'] = game.to_json()
    session['turn'] = turn
    return render_template('index.html', board=game.board, turn=turn)


@app.route('/public/css/<path:path>')
def send_js(path):
    return send_from_directory('public/css', path)


if __name__ == '__main__':
    app.run()
