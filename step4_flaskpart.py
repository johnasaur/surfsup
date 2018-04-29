# dependencies
import datetime as dt
import numpy as np 
import pandas as pd 
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask, jsonify

# engine to create to the db
engine = create_engine("sqlite:///hawaii.sqlite")

# load orm with automap
Base = automap_base()

# tables from orm
Base.prepare(engine, reflect=True)

measrm = Base.classes.measurements
stations = Base.classes.stations

# start session
session = Session(engine)

# start flask and create routes
app = Flask(__name__)

# precipitation route
@app.route("/api/v1.0/precipitation")
def prcp():
    lastyr = dt.date.today() - dt.timedelta(days=365)
    precip = session.query(measrm.date, func.sum(measrm.prcp)).filter(measrm.date >= lastyr).group_by(measrm.date).order_by(measrm.date.all()
    )

# stations route
@app.route("/api/v1.0/stations")
def stations():
    stations1 = session.query(stations, station).all()
    stations2 = list(np.ravel(stations1))
    return jsonify(stations2)


# tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    lastyr = dt.date.today() - dt.timedelta(days = 365)
    tobs1 = session.query(measrm.tobs).filter(measrm.date >= lastyr).all()
    tobs2 = list(np.ravel(tobs1))
    return jsonify(tobs2)

# <start> route
@app.route("/api/v1.0<start>")
def start1():
    start2 = session.query(func.avg(measrm.tobs), func.min(measrm.tobs),func.max(measrm.tobs)).\
    filter(measrm.date >= arrivedt).all()
    metrics_dict = {"avg": start2[0][0], "min": start2[0][1],
    "max": start2[0][2]}
    return jsonify(metrics_dict)

# <start>/<end>
@app.route("/api/v1.0/start/end")
def avg_max_min():
    various_temps = session.query(func.avg(measrm.tobs), func.min(measrm.tobs), func.max(measrm.tobs)).\
    filter(measrm.date.between("2015-09-10", "2015-09-16")).all()
    metrics_dict2 = {"avg": various_temps[0][0], "min": various_temps[0][1],
    "max": various_temps[0][2]}
    return jsonify(metrics_dict2)


if __name__ == "__main__":
    app.run(debug=True)
    