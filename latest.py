from flask import Flask, jsonify, request,Blueprint #import objects from the Flask model
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='ADDRESS',
user='USER',
password='PASSWORD',
db='DATABASE',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

latestData = Blueprint('latest_data', __name__)#define app using Flask

# fetches the latest data
@latestData.route('/latest', methods=['GET'])
def LatestData():
 with connection.cursor() as cursor:
    connection.connect() #opens the connection
    sql = "SELECT * from latest"
    cursor.execute(sql) #executes the sql statement
    result = cursor.fetchall() # fetches all the rows
    connection.close() # closes connection
    return jsonify({'latest' : result}) # displays data in json format