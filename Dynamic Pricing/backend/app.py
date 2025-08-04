from flask import Flask, render_template, request
import pickle
import numpy as np
import datetime

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('base.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        dep_date = request.form['dep_date']
        dep_place = request.form['dep_place']
        dest_place = request.form['dest_place']
        travel_class = request.form['travel_class']
        passenger_type = request.form['passenger_type']
        seat_type = request.form['seat_type']

        date_obj = datetime.datetime.strptime(dep_date, '%Y-%m-%d')
        is_weekend = date_obj.weekday() >= 5

        price_addition = 0
        if is_weekend:
            price_addition += 1000
        if is_festival(dep_date):
            price_addition += 2000
        if seat_type == 'window':
            price_addition += 500
        elif seat_type == 'middle':
            price_addition += 200
        elif seat_type == 'outside':
            price_addition += 100
        if travel_class == 'business':
            price_addition += 3000

        features = [
            encode_place(dep_place),
            encode_place(dest_place),
            encode_class(travel_class),
            encode_passenger(passenger_type),
            encode_seat(seat_type),
        ]
        features = np.array(features).reshape(1, -1)
        base_price = model.predict(features)[0]
        final_price = base_price + price_addition

        return render_template('pred.html', price=round(final_price, 2))

    return render_template('pred.html', price=None)


# Match encodings from Colab
def encode_place(place):
    return {'Bangalore': 0, 'Delhi': 1, 'Kolkata': 2, 'Mumbai': 3}.get(place, 0)

def encode_class(cls):
    return {'business': 0, 'economy': 1}[cls]

def encode_passenger(p_type):
    return {'army': 0, 'senior': 1, 'student': 2}[p_type]

def encode_seat(seat):
    return {'middle': 0, 'outside': 1, 'window': 2}[seat]

def is_festival(date_str):
    return date_str in ['2025-01-26', '2025-08-15', '2025-10-02', '2025-11-04', '2025-12-25']

if __name__ == '__main__':
    app.run(debug=True)



