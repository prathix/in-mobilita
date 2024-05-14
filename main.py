from flask import Flask, render_template, jsonify, send_from_directory
import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    target_day = datetime.datetime(2024, 6, 6, 12, 0)
    remaining_time = target_day - datetime.datetime.now()
    countdown_dict = {
        'days': remaining_time.days,
        'hours': remaining_time.seconds // 3600,
        'minutes': (remaining_time.seconds % 3600) // 60,
        'seconds': remaining_time.seconds % 60
    }
    return render_template('index.html', countdown=countdown_dict)

@app.route('/update_countdown')
def update_countdown():
    target_day = datetime.datetime(2024, 6, 6, 9, 0)
    remaining_time = target_day - datetime.datetime.now()
    countdown_dict = {
        'days': remaining_time.days,
        'hours': remaining_time.seconds // 3600,
        'minutes': (remaining_time.seconds % 3600) // 60,
        'seconds': remaining_time.seconds % 60
    }
    return jsonify(countdown_dict)

if __name__ == '__main__':
    app.run(debug=True)
