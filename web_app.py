from flask import Flask, render_template, request, url_for, redirect
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


####Nada's stuff
# @app.route('/')
# def main():
#     return render_template('/main_page.html')

# @app.route('/search/',methods=['GET','POST'])
# def search():
# 	instrument = request.form['instrument']
# 	return render_template('results.html', instrument = instrument)

# @app.route('/results/<str: instrument>',methods=['GET','POST'])
# def results(instrument):
# 	if request.method == 'GET':
####

#YOUR WEB APP CODE GOES HERE
@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('main_page.html')
	else:
		email = request.form('email')
		password = request.form('password')
		user = session.query(Person).filter_by(email=email).first()
		if password == user.password:
			return redirect(url_for('search'), user.id)
		else:
			return render_template('main_page.html', error = True)


@app.route('/sign_up', methods=['GET', 'POST'])
def add_friend():
	if request.method == 'GET':
		currentyear = datetime.now().year
		years = range(currentyear, currentyear - 101, -1)
		months = range(1, 13)
		days = range(1, 32)
		return render_template('sign_up.html', years = years, months = months, days = days)
	else:
		dob = datetime(int(request.form['year']), int(request.form['month']), int(request.form['day']))
		friend = Person(name = request.form['name'],
						gender = request.form['gender'],
						nationality = request.form['nationality'],
						city = request.form['city'],
						email = request.form['email'],
						password = request.form['password'],
						instrument = request.form['instrument'],
						genre = request.form['genre'],
						phone = request.form['phone'],
						dob = dob,
						tv_shows = request.form['tv_shows'])

		session.add(friend)
		session.commit()

		return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)

