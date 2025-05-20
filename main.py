from flask import Flask, render_template, request
app = Flask(__name__)
# Route for the web-based guessing game
@app.route('/web_guesser', methods=['GET', 'POST'])
def web_guesser():
    if request.method == 'GET':
        # Initialize the range for guessing
        max_number = 1000
        min_number = 0
        # Render the welcome page and pass the initial range
        return render_template('welcome.html', max_number=max_number, min_number=min_number)
    elif request.method == 'POST':
        # Get the current guessing range from the form
        max_number = int(request.form.get('max_number'))
        min_number = int(request.form.get('min_number'))
        # Read the user's feedback from the form
        answer = request.form.get('answer')
        if answer == "correct":
            # If the guess was correct, show a win message
            return render_template('win.html')
        elif answer == "too big":
            # If guess is too big, adjust upper bound
            max_number = int(((max_number - min_number) / 2) + min_number)
        elif answer == "too small":
            # If guess is too small, adjust lower bound
            min_number = int(((max_number - min_number) / 2) + min_number)
        # Make a new guess based on the updated range
        guess_number = int(((max_number - min_number) / 2) + min_number)
        message = f"I think it's {guess_number}"
        # Render the main game page with updated state
        return render_template('main.html',
                               max_number=max_number, min_number=min_number,
                               guess_number=guess_number, message=message)
    return None

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)