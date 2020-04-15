from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import dateutil.relativedelta
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    """Home Page"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    import dateutil.relativedelta

    results = session.query(Measurement.date).all()

    MaxDate_str_lst = max(results)

    MaxDate_str = MaxDate_str_lst[0]

    MaxDate = dt.datetime.strptime(MaxDate_str,"%Y-%m-%d").date()

    sdate = MaxDate - dateutil.relativedelta.relativedelta(months=12)
    qry_prcp = session.query(Measurement.date, func.avg(Measurement.prcp).label('avg_prcp')).filter(Measurement.date >= sdate).group_by(Measurement.date)

    df_prcp = pd.read_sql_query(qry_prcp.statement, session.bind)

    df_prcp.sort_values(by=['date'])

    df_prcp.set_index('date')['avg_prcp'].to_dict
    df_prcp.to_dict('List_prcp')
    
    return jsonify(List_prcp)

@app.route("/api/v1.0/stations")
def stations():
    results4 = session.query(Measurement.station, func.count(Measurement.station).label('NumST')).group_by(Measurement.station)

    data4 = dict((station,NumST) for station,NumST in results4)

    sorted_data4 = dict(sorted(data4.items(), key=lambda item: item[1], reverse=True))

    return jsonify(sorted_data4)


@app.route("/api/v1.0/tobs")
def tobs():
    def tobs():
    qry_temp = 'SELECT tobs FROM Measurement WHERE station = "' + most_active_station +'" AND date >=' + str(sdate) +' AND tobs IS NOT NULL'
    results5 = session.execute(qry_temp)

    data5 = []

    for row in results5:
        data5.append(row[0])

    return data5

@app.route("/api/v1.0/<start>")
def start(start):
    def calc_temps(start_date, end_date):
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
if __name__ == '__main__':