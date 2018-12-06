#!flask/bin/python
from flask import Flask, jsonify
import sqlite3
import math

app = Flask(__name__)


@app.route('/trip/<string:trip_begin>/<string:trip_end>', methods=['GET'])
def get_highlights(trip_begin,trip_end):
    conn = sqlite3.connect('tour.db')
    c = conn.cursor()	
    trip_id_statement = c.execute("SELECT id FROM trip WHERE trip_begin = '{}' and trip_end = '{}';".format(trip_begin,trip_end))
    trip_id = trip_id_statement.fetchone()[0]
    highlight_ids_statement = c.execute("SELECT highlight_id FROM relation WHERE trip_id = '{}';".format(trip_id))
    highlight_ids = highlight_ids_statement.fetchall()

    highlight_dict = {}
    for hid in highlight_ids:
        #print(hid)
        highlight_row = c.execute("SELECT name,latitude,longitude FROM highlight WHERE id = '{}';".format(hid[0]))
        for highlight in highlight_row.fetchall():
            highlight_dict[highlight[0]] = { 'latitude': str(highlight[1]), 'longitude': str(highlight[2]) }

    conn.close()
    return jsonify({"highlights": highlight_dict})

@app.route('/highlight/<string:latitude>/<string:longitude>', methods=['GET'])
def get_nearest_highlight(latitude,longitude):
    lat = float(latitude)
    lon = float(longitude)
    conn = sqlite3.connect('tour.db')
    c = conn.cursor()
    highlights_coords = c.execute("SELECT name,latitude,longitude FROM highlight;")

    smallest_distance = math.inf
    smallest_name = ""
    smallest_lat = 0.0
    smallest_lon = 0.0
    for highlight in highlights_coords.fetchall():
        cur_lat = highlight[1]
        cur_lon = highlight[2]
        cur_distance = math.sqrt( ( cur_lat - lat )**2 + (cur_lon - lon)**2 )
        if( cur_distance < smallest_distance):
            smallest_distance = cur_distance
            smallest_name = highlight[0]
            smallest_lat = cur_lat
            smallest_lon = cur_lon
    if(smallest_distance == math.inf):
        return jsonify("abort!!!")

    conn.close()
    return jsonify(  {"nearest_highlight": { "name": smallest_name, "latitude": smallest_lat, "longitude": smallest_lon } })


if __name__ == '__main__':
    app.run(debug=True)