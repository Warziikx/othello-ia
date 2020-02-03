from flask import Flask
from src.board import Board

app = Flask(__name__)


@app.route('/')
def hello_world():
    board = Board(8,8)
    board.new_board()
    
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
