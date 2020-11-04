import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import pickle



train_data=pd.read_excel("Data_Train.xlsx")
pd.set_option("display.max_columns",None)

print(train_data.head())

train_data.dropna(inplace=True)

train_data['Journey_day']=pd.to_datetime(train_data.Date_of_Journey,format='%d/%m/%Y').dt.day

train_data['Journey_month']=pd.to_datetime(train_data.Date_of_Journey,format='%d/%m/%Y').dt.month

train_data.drop('Date_of_Journey',axis=1,inplace=True)

print(train_data.head())

train_data['Dep_hour']=pd.to_datetime(train_data.Dep_Time).dt.hour

train_data['Dep_min']=pd.to_datetime(train_data.Dep_Time).dt.minute

train_data.drop('Dep_Time',axis=1,inplace=True)

train_data['Arrival_hour']=pd.to_datetime(train_data.Arrival_Time).dt.hour

train_data['Arrival_min']=pd.to_datetime(train_data.Arrival_Time).dt.minute

train_data.drop('Arrival_Time',axis=1,inplace=True)

Duration = list(train_data['Duration'])

for i in range(len(Duration)):
    if len(Duration[i].split()) != 2:    # Check if duration contains only hour or mins
        if 'h' in Duration[i]:              #if the duration as h
            Duration[i] = Duration[i].strip() + " 0m"       # split and add 0m if is contains just 0h
        else:
            Duration[i] = "0h " + Duration[i]               # else add 0h

duration_mins = []
duration_hours = []

for i in range(len(Duration)):
    duration_hours.append(int(Duration[i].split(sep="h")[0]))
    duration_mins.append(int(Duration[i].split(sep="m")[0].split()[-1]))

train_data['Duration_hours']=duration_hours
train_data['Duration_mins']=duration_mins

train_data.drop('Duration',axis=1,inplace=True)


Airline = train_data[["Airline"]]

Airline = pd.get_dummies(Airline, drop_first= True)

Source = train_data[["Source"]]

Source = pd.get_dummies(Source, drop_first= True)

Destination = train_data[["Destination"]]

Destination = pd.get_dummies(Destination, drop_first= True)

train_data.drop(["Route","Additional_Info"],axis=1,inplace=True)

train_data.replace({'non-stop':0, '1 stop':1,'2 stops':2, '3 stops':3 ,'4 stops':4},inplace=True)

new_train_data=pd.concat([train_data, Airline, Source, Destination], axis = 1)

new_train_data.drop(["Airline", "Source", "Destination"], axis=1, inplace = True)

X = new_train_data.loc[:, ['Total_Stops', 'Price', 'Journey_day', 'Journey_month', 'Dep_hour',
       'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
       'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
       'Airline_Jet Airways', 'Airline_Jet Airways Business',
       'Airline_Multiple carriers',
       'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
       'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
       'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
       'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       'Destination_Kolkata', 'Destination_New Delhi']]
X.rename(columns={"Destination_New Delhi": "Destination_Mumbai"},inplace=True)
print(X.head())

y = new_train_data['Price']
print(y.head())


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=30)

rf_reg=RandomForestRegressor()
rf_reg.fit(X_train, y_train)



filename='flight_price_modal.pkl'
pickle.dump(rf_reg, open(filename, 'wb'))

