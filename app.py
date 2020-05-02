from flask import Flask, jsonify, request, Blueprint, render_template #import objects from the Flask model
from flask_swagger_ui import get_swaggerui_blueprint
import sys
from latest import latestData
from locations import locationData

app = Flask(__name__) #define app using Flask

# swagger specific
SWAGGER_URL = ''
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Covid-19 Somaliland API"
    }
)

# connects all the microservices
app.register_blueprint(latestData)
app.register_blueprint(locationData)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
        app.run(debug=True, port='8080')