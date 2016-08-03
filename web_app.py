from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
from database_setup import Base, Person

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def main():
    return render_template('/main_page.html')

@app.route('/search/',methods=['GET','POST'])
def search():
	instrument = request.form['instrument']
	return render_template('results.html', instrument = instrument)

@app.route('/results/<str: instrument>',methods=['GET','POST'])
def results(instrument):
	if request.method == 'GET':
		

if __name__ == '__main__':
    app.run(debug=True)

