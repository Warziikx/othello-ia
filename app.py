from flask import Flask, render_template, send_from_directory, session

from src.game import Game

app = Flask(__name__)
app.secret_key = 'GwH!wXhhug#8G$j5$&pHGnat'


@app.route('/')
def play():
    game = Game(8, 8)
    game.start()
    session['game'] = game.to_json()
    return render_template('index.html', board=game.board)


@app.route('/public/css/<path:path>')
def send_js(path):
    return send_from_directory('public/css', path)


if __name__ == '__main__':
    app.run()

