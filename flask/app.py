from flask import Flask, request, render_template_string, redirect, url_for
import csv

app = Flask(__name__)


form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='popo.css') }}">
    <title>Student Information Form</title>
</head>
<body>
    <div class="background">
        <h2 class="form-title">Student Information Form</h2>
        <form action="/submit" method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br><br>

            <label for="rollNumber">Roll Number:</label><br>
            <input type="text" id="rollNumber" name="rollNumber" required><br><br>

            <label for="board">Board:</label><br>
            <input type="text" id="board" name="board" required><br><br>

            <label for="marks">Marks:</label><br>
            <input type="number" id="marks" name="marks" required><br><br>
            
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
'''

# Route for displaying the form
@app.route('/')
def form():
    return render_template_string(form_html)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    
    name = request.form['name']
    roll_number = request.form['rollNumber']
    board = request.form['board']
    marks = request.form['marks']

    
    with open('submissions.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'rollNumber', 'board', 'marks']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'name': name, 'rollNumber': roll_number, 'board': board, 'marks': marks})

    
    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
