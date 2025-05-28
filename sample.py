from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
  user_id = request.args.get('id')
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor
  cursor.execute("SELECT name FROM user WHERE id = {user_id}")
  
