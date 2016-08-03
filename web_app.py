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

		return redirect(url_for('search'), user.id)

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
