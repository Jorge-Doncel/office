import os
from dotenv import load_dotenv
load_dotenv()

def transformToGeoPoint(s):
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        return None
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }
    

clean_offices["geopoint"] = clean_offices.apply(transformToGeoPoint, axis=1)

def geocode(address):
    res = requests.get(f"https://geocode.xyz/{address}", params={"json":1})
    data = res.json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }

def getQuery(info, queryParams={}):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("ID"),
    client_secret=os.getenv("SECRET"),
    v='20200623',
    ll="37.78986,-122.45712",
    query=info,
    radius=6000,
    limit=500
    )
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)

def getId(idcategory, radio):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("ID"),
    client_secret=os.getenv("SECRET"),
    v='20200623',
    ll="37.78986,-122.45712" ,
    categoryId=idcategory,
    radius=radio,
    limit=500
    )
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)

def geoQueryNear(point,radius=10000):
    return {
        "geopoint":{
            "$near": {
                "$geometry": point,
                "$maxDistance": radius,
                "$minDistance": 0
            }
        }
    }

def officeLocation(coordenates):
    res = requests.get(f"https://geocode.xyz/{coordenates}", params={"json":1})
    data = res.json()
    return {
        "type":"Point",
        "coordinates":data
    }