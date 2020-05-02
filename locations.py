from flask import Flask, jsonify, request,Blueprint #import objects from the Flask model
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='ADRESS',
user='USER',
password='PASSWORD',
db='DATABASE',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

locationData = Blueprint('location_data', __name__)#define app using Flask

# fetches all the locations
@locationData.route('/locations', methods=['GET'])
def locations():
    with connection.cursor() as cursor:
        connection.connect() #opens the connection
        sql = "SELECT * from locations" 
        cursor.execute(sql) # executes the sql statement
        result = cursor.fetchall() # fetches all rows
        return jsonify({'locations' : result}) # displays data in json format

# fetches the location associated with the chosen id
@locationData.route('/locations/id/<int:id>', methods=['GET'])
def returnFromID(id):
    with connection.cursor() as cursor:
        connection.connect() #opens the connection
        cursor.execute('SELECT * FROM locations WHERE id = %s' , id)  # executes the sql statement
        result = cursor.fetchone() # fetches one row
        return jsonify({'locations' : result})  # displays data in json format

# fetches the location associated with the chosen province name
@locationData.route('/locations/province/<string:province>', methods=['GET'])
def returnFromProvince(province):
    with connection.cursor() as cursor:
    # Read a single record
        connection.connect()
        cursor.execute('SELECT * FROM locations WHERE province = %s' , province)
        result = cursor.fetchone()
        return jsonify({'locations' : result})          

# fetches the location associated with the chosen city name
@locationData.route('/locations/city/<string:city>', methods=['GET'])
def returnFromCity(city):
    with connection.cursor() as cursor:
    # Read a single record
        connection.connect()
        cursor.execute('SELECT * FROM locations WHERE city = %s' , city)
        result = cursor.fetchone()
        return jsonify({'locations' : result})  
