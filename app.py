from flask import Flask, request, render_template
import sklearn
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__,template_folder="template")

model = pickle.load(open("flight_price_modal.pkl", "rb"))

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/predict", methods = ["GET", "POST"])
def predict():


    if request.method == "POST":

        # Date_of_Journey
        date_dept = request.form["dept_time"]

        Journey_day = int(pd.to_datetime(date_dept, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dept, format="%Y-%m-%dT%H:%M").month)

        # Departure hour and minute
        Dep_hour = int(pd.to_datetime(date_dept, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dept, format="%Y-%m-%dT%H:%M").minute)

        # Arrival hour and minute
        date_arr = request.form["arrival_time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Duration hours and minutes
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        # Total Stops
        Total_stops = int(request.form["stops"])

        # Airline
        airlines = request.form['airline']
        if (airlines == 'Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airlines == 'Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

        elif (airlines == 'Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )

        #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
        #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
        #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
        #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
        #    'Airline_Multiple carriers',
        #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
        #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
        #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
        #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
        #    'Destination_Kolkata', 'Destination_New Delhi']

        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output = round(prediction[0], 2)

        return render_template('home.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

"""
        Source = request.form['source']
        if Source == 'Delhi':
            temp_array = temp_array + [1, 0, 0, 0, 0]
        elif Source == 'Kolkata':
            temp_array = temp_array + [0, 1, 0, 0, 0]
        elif Source == 'Mumbai':
            temp_array = temp_array + [0, 0, 1, 0, 0]
        elif Source == 'Chennai':
            temp_array = temp_array + [0, 0, 0, 1, 0]
        elif Source == 'Banglore':
            temp_array = temp_array + [0, 0, 0, 0, 1]

        Destination = request.form['destination']
        if Destination == 'Cochin':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0]
        elif Destination == 'Delhi':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0]
        elif Destination == 'Mumbai':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0]
        elif Destination == 'Hyderabad':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0]
        elif Destination == 'Kolkata':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0]
        elif Destination == 'Banglore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1]"""

"""
        Source = request.form["source"]
        if (Source == 'Delhi'):
            Source_Delhi  = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0


        elif (Source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1

        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        Destination = request.form["destination"]
        if (Destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Mumbai = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Mumbai = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'Mumbai'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Mumbai = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Mumbai = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0

        elif (Destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Mumbai = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1

        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Mumbai = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        

        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Source_Delhi ,
            Source_Kolkata ,
            Source_Mumbai ,
            Source_Chennai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_Mumbai
        ]])
        
        output = round(prediction[0])

        return render_template('index.html', prediction_text="Your Flight price is Rs. {}".format(output))
    else:
        return render_template("index.html")

if __name__ == "__main__":
    model = pickle.load(open("flight_price_modal.pkl", "rb"))
    app.run(debug=True)


temp_array = [Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy] + temp_array

        data = np.array([temp_array])
        my_prediction = int(model.predict(data)[0])
        return render_template('index.html', prediction_text="Your Flight price is Rs. {}".format(my_prediction))
"""


