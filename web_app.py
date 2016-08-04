from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
from database_setup import Base, Person
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/search/',methods=['GET','POST'])
def search():
	instrument = request.form['instrument']
	list_of_instruments = session.query(Person).filter_by(name = instrument).all()
	list_of_people = []
	for instrument in list_of_instruments:
		list_of_people.append(instrument.person)
	return render_template('search.html', Person = list_of_people)

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
			return redirect(url_for('search'))
		else:
			return render_template('main_page.html', error = True)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'GET':
		currentyear = datetime.now().year
		years = range(currentyear, currentyear - 101, -1)
		months = range(1, 13)
		days = range(1, 32)
		return render_template('sign_up.html', years = years, months = months, days = days)
	else:
		dob = datetime(int(request.form['year']), int(request.form['month']), int(request.form['day']))
		user = Person(name = request.form['name'],
						gender = request.form['gender'],
						nationality = request.form['nationality'],
						city = request.form['city'],
						email = request.form['email'],
						password = request.form['password'],
						genre = request.form['genre'],
						phone = request.form['phone'],
						dob = dob,
						tv_shows = request.form['tv_shows'])
		#Come back
		instruments = Instrument(request.form['instrument'])
		for instrument in instruments:
			instrument_object = Instrument(name = instrument)
			session.add(instrument_object)	
			user.instrument.append(instrument_object)

		session.add(user)
		session.commit()
		return redirect(url_for('search'))


if __name__ == '__main__':
    app.run(debug=True)

