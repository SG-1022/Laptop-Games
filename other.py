from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def guess_game():
    secret_number = random.randint(0, 9)

    print(f"The secret number is: {secret_number}")

    other = True
    message = '<h1>Guess a number between 0 and 9</h1><img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

    if request.method == 'GET':
        user_guess = request.form.get('user_input', type=int)

        if user_guess == secret_number:
            other = False
            message = '<h1 style="color:green;">You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
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

    return render_template('index.html', output_val=message, a=other)

if __name__ == '__main__':
    app.run(debug=True)


