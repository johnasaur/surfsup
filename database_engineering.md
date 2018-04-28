

```python
# dependencies
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime 
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
```


```python
# create engine
engine = create_engine("sqlite:///hawaii.sqlite")
```


```python
# connect engine
conn = engine.connect()
```


```python
df = pd.read_csv("Lesson-Plans/clean_hawaii_measurements.csv")
df_stations = pd.read_csv("Lesson-Plans/hawaii_stations.csv")
```


```python
# create base
Base =  declarative_base()
```


```python
# create class for measrm
class Measurements(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    date = Column(String)
    prcp = Column(Float)
    tobs = Column(Float)
```


```python
# create class for stations
class Stations(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
```


```python
# create all to create table for all measurements
Base.metadata.create_all(engine)
session = Session(bind=engine)
```


```python
# ORM to create list mgmt for measurements
measrm_data = df.to_dict(orient="records")
measrm_data[0]
```




    {'date': '1/1/10', 'prcp': 0.08, 'station': 'USC00519397', 'tobs': 65}




```python
# ORM to create list mgmt for stations
stations_data = df_stations.to_dict(orient="records")
stations_data[0]
```




    {'elevation': 3.0,
     'latitude': 21.2716,
     'longitude': -157.8168,
     'name': 'WAIKIKI 717.2, HI US',
     'station': 'USC00519397'}


