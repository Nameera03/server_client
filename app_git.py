from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_git.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    # Dummy data (replace with your actual data)
    data = {'name1': 'english', 'number1': 113, 'name2': 'marathi', 'number2':311}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
