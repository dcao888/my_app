from datetime import datetime

from db import Record

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# create db connection 
engine = create_engine('postgresql+psycopg2://usr:pass@postgres/db')
Session = sessionmaker(bind = engine)
session = Session()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # if someone submits a form ...
    if request.form:
        record = Record(user = 'dcao888', 
                        record = request.form.get('record'),
                        upload_dttm = datetime.now())
        session.add(record)
        session.commit()

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)