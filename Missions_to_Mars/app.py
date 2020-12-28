from flask import Flask, render_template,redirect
import pymongo
from scrape_mars import scrape_all


app = Flask(__name__)
