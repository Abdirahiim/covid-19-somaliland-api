from flask import Flask, jsonify, request,Blueprint #import objects from the Flask model
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='ADDRESS',
user='USER',
password='PASSWORD',
db='DATABASE',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

locationdata = Blueprint('location_data', __name__)#define app using Flask

# fetches all the locations
@locationdata.route('/locations', methods=['GET'])
def locations():
    with connection.cursor() as cursor:
        connection.connect() #opens the connection
        sql = "SELECT * from locations" 
        cursor.execute(sql) # executes the sql statement
        result = cursor.fetchall() # fetches all rows
        connection.close() # closes connection
        return jsonify({'locations' : result}) # displays data in json format

# fetches the location associated with the chosen id
@locationdata.route('/locations/id/<int:id>', methods=['GET'])
def returnFromID(id):
    with connection.cursor() as cursor:
        connection.connect() #opens the connection
        cursor.execute('SELECT * FROM locations WHERE id = %s' , id)  # executes the sql statement
        result = cursor.fetchone() # fetches one row
        connection.close() # closes connection
        return jsonify({'locations' : result})  # displays data in json format

# fetches the location associated with the chosen province name
@locationdata.route('/locations/province/<string:province>', methods=['GET'])
def returnFromProvince(province):
    with connection.cursor() as cursor:
    # Read a single record
        connection.connect()
        cursor.execute('SELECT * FROM locations WHERE province = %s' , province)
        result = cursor.fetchone()
        connection.close() # closes connection
        return jsonify({'locations' : result})          

# fetches the location associated with the chosen city name
@locationdata.route('/locations/city/<string:city>', methods=['GET'])
def returnFromCity(city):
    with connection.cursor() as cursor:
    # Read a single record
        connection.connect()
        cursor.execute('SELECT * FROM locations WHERE city = %s' , city)
        result = cursor.fetchone()
        connection.close() # closes connection
        return jsonify({'locations' : result})  