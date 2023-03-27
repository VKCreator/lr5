from flask import Flask, render_template, request, session, url_for, redirect
from utils_game import createGame, processGame
from forms import GameForm

app = Flask(__name__)

# work with session
app.config['SECRET_KEY'] = 'bc916900ed8190ab5ffa194356nhdfh45656'

@app.route('/', methods=["GET"])
def index():

    gameState = {}
    form = GameForm()

    createGame(gameState)

    for key, value in gameState.items():
        session[key] = value

    return render_template("index.html", context=gameState, form=form)

@app.route('/game', methods=["POST"])
def gaming():

    gameState = {}
    form = GameForm(request.form)

    for key, value in session.items():
        gameState[key] = value

    if request.method == 'POST' and form.validate():

        if gameState["currentAttempts"] > 0:
            processGame(gameState, request.form["userGuessNumberInput"])

            for key, value in gameState.items():
                session[key] = value

            session.modified = True
        else:
            return redirect(url_for('index'))

    return render_template("index.html", context=gameState, form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', text="Похоже, что такой страницы не существует..."), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template('error.html', text="Метод запроса запрещён!"), 405

if __name__ == "__main__":
    app.run(debug=True)