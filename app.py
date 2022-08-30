
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import Flask
from flask import Flask,jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create an app, being sure to pass __name__
app = Flask(__name__)




# Define what to do when a user hits the index route
@app.route("/")
def home():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )


# Define what to do when a user hits the /precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    session=Session(engine)
    #Convert the query results to a dictionary using date as the key and prcp as the value.
    query_results = session.query(Measurement.date,Measurement.prcp).all()
    session.close()

    prcp_date =[]
    for date,prcp in query_results:
        prcp_dict={}
        prcp_dict["Date"]=date
        prcp_dict["Precipitation"]=prcp
        prcp_date.append(prcp_dict)
    return jsonify(prcp_date)


@app.route('/api/v1.0/stations')
def stations():
    session=Session(engine)
    #Convert the query results to a dictionary using date as the key and prcp as the value.
    query_results = session.query(Station.id,Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).all()
    session.close()

    stn =[]
    for id,station,name,latitude,longitude,elevation in query_results:
        stn_dict={}
        stn_dict["Id"]=id
        stn_dict["Station"]=station
        stn_dict["Name"]=name
        stn_dict["Latitude"]=latitude
        stn_dict["Longitude"]=longitude
        stn_dict["Elevation"]=elevation
        stn.append(stn_dict)
    return jsonify(stn)



if __name__ == "__main__":
    app.run(debug=True)
