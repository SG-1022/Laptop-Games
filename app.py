from flask import Flask, render_template, request, session
import random
import os

# TODO - Make a Footer and Navbar
# TODO - Make the website look like a website.
# TODO - Make the website runnable.

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/number_guessing_game', methods=['GET', 'POST'])
def guess_game():
    a = 0
    if 'secret_number' not in session:

        session['secret_number'] = random.randint(0, 9)
        while a == session['secret_number']:
            session['secret_number'] = random.randint(0, 9)

    secret_number = session['secret_number']


    other = True
    message = '<h1>Guess a number between 0 and 9</h1><img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

    if request.method == 'POST':
        user_guess = request.form.get('user_input', type=int)

        if user_guess == secret_number:
            other = False
            message = '<h1 style="color:green;">You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
            session.pop('secret_number')
        elif user_guess is not None:
            other = True
            if user_guess < secret_number:
                message = '<h1 style="color:red;">To Low, try again!</h1><img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>'
            elif user_guess > secret_number:
                message = '<h1 style="color:purple;">To High, try again!</h1><img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>'
            else:
                message = '<h1 style="color:red;">There is an error...</h1>'
        else:
            other = True
            message = '<h1>Guess a number between 0 and 9</h1><img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

    return render_template('number_guessing_game.html', output_val=message, a=other)

@app.route('/Snake-Game')
def Snake_Game():
    return render_template('snake_game.html')

if __name__ == '__main__':
    app.run()


