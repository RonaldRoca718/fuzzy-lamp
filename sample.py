from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
  userid = request.args.get('id')
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor
  cursor.execute(f"SELECT name FROM user WHERE id = {userid}")
  user = cursor.fetchone()

return f"User: {user[0]}"
  
