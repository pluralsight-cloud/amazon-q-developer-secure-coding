from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')
    app.logger.info(f'User submitted: {user_input}')
    return 'Input received', 200

if __name__ == '__main__':
    app.run()
