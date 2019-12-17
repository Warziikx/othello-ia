from flask import Flask, render_template

from src.board import Board

app = Flask(__name__)


@app.route('/')
def hello_world():
    board = Board()
    b = board.new_board(8, 8)
    newboard = board.get_departure_cells(b)
    return render_template('index.html', board=b)
if __name__ == '__main__':
    app.run()
