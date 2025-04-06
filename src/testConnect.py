# -*- coding: utf-8 -*-
from datetime import timedelta
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import (ClusterOptions, ClusterTimeoutOptions)

username = "admin"
password = "Art_12503"
bucket_name = "travel-sample"
auth = PasswordAuthenticator( username, password,)

timeout_opts = ClusterTimeoutOptions(connect_timeout=timedelta(seconds=20),
                                          kv_timeout=timedelta(seconds=20))

options = ClusterOptions(auth, timeout_options=timeout_opts)
cluster = Cluster('couchbase://127.0.0.1', options)
cluster.wait_until_ready(timedelta(seconds=5))

cb = cluster.bucket(bucket_name)

cb_coll = cb.scope("inventory").collection("airline")
cb_coll_default = cb.default_collection()

# upsert document function
def upsert_document(doc):
    print("\nUpsert CAS: ")
    try:
        # key will equal: "airline_8091"
        key = doc["type"] + "_" + str(doc["id"])
        result = cb_coll.upsert(key, doc)
        print("CAS =" + str(result.cas))
    except Exception as e:
        print(e)

# get document function
def get_airline_by_key(key):
    print("\nGet airline for key = "+key+" :")
    try:
        result = cb_coll.get(key)
        print("Data:")
        data_str = result.content_as[str]
        print(data_str)
        data = eval(data_str)
        print("name:     "+ data["name"])
        print("callsign: "+ data["callsign"])
        print("iata:     "+ data["iata"])
        print("icao:     "+ data["icao"])
        
    except Exception as e:
        print(e)

airline = {
    "type": "airline",
    "id": 111222333,
    "callsign": "TEST",
    "iata": "SVO",
    "icao": "ULN",
    "name": "My Airways",
}

upsert_document(airline)
get_airline_by_key("airline_111222333")
get_airline_by_key("airline_10")
