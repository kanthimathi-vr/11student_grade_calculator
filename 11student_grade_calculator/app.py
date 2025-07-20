from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            score = float(request.form.get('score', 0))
        except ValueError:
            score = 0
        # Redirect with score as query param
        return redirect(url_for('result', score=score))
    return render_template('home.html')

@app.route('/result')
def result():
    score = request.args.get('score', default=None, type=float)
    if score is None:
        return redirect(url_for('home'))
    letter_grade = calculate_letter_grade(score)
    return render_template('result.html', score=score, letter_grade=letter_grade)

if __name__ == '__main__':
    app.run(debug=True)
