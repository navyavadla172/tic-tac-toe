from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the game board and state
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

@app.route("/")
def index():
    return render_template("index.html", board=board, current_player=current_player)

@app.route("/move/<int:row>/<int:col>")
def make_move(row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        if check_winner():
            return render_template("index.html", board=board, current_player=current_player, winner=current_player)
        elif is_board_full():
            return render_template("index.html", board=board, current_player=current_player, winner="Tie")
        current_player = "O" if current_player == "X" else "X"
    return redirect(url_for("index"))

def check_winner():
    for i in range(3):
        if all([cell == current_player for cell in board[i]]) or all([board[j][i] == current_player for j in range(3)]):
            return True
    if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        return True
    if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
        return True
    return False

def is_board_full():
    for row in board:
        if " " in row:
            return False
    return True

if __name__ == "__main__":
    app.run(debug=True)
