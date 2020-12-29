from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo 
from scrape_mars import scrape_all


app = Flask(__name__)
app.config ['MONGO_URI'] = 'mongodb://localhost:27017/mission_mars'
mongo = PyMongo (app)

db = mongo.db
collection = db['mars_data']