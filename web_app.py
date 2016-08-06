from flask import Flask, render_template, request, url_for, redirect
from flask import session as flasksession
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
from database_setup import Base, Person, Interests, PersonToInterests, Instrument, PersonToInstrument
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/search/')
def search():
	instrument_name = request.args.get('instrument', None)
	list_of_people = []
	if 'user_id' in flasksession:
		if instrument_name is None: # only instruments, didn't get instrument
			return render_template('search.html', users = list_of_people)
		else:
				user_city = session.query(Person).filter_by(id = flasksession['user_id']).first().city
				instrument = session.query(Instrument).filter_by(name = instrument_name).first()
				if instrument is None: # only instruments
					return render_template('search.html', users = list_of_people, error1 = True) # can't find instrument
				else:
					list_of_people_instruments = instrument.persons
					for person in list_of_people_instruments:
						if person.city == user_city:
							list_of_people.append(person)
							print (person.name)
					if list_of_people == []: #with cities
						return render_template('search.html', users = list_of_people, error1 = True)
					else:
						return render_template('search.html', users = list_of_people)
	else:
		return render_template('search.html', users = list_of_people, error2 = True)

#YOUR WEB APP CODE GOES HERE
@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('main_page.html')
	else:
		email = request.form['email']
		password = request.form['password']
		user = session.query(Person).filter_by(email=email).first()
		if password == user.password:
			flasksession['user_id'] = user.id
			return redirect(url_for('search'))
		else:
			return render_template('main_page.html', error = True)


@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
	currentyear = datetime.now().year
	years = range(currentyear, currentyear - 101, -1)
	months = range(1, 13)
	days = range(1, 32)	
	if request.method == 'GET':
		currentyear = datetime.now().year
		years = range(currentyear, currentyear - 101, -1)
		months = range(1, 13)
		days = range(1, 32)
		return render_template('sign_up.html', years = years, months = months, days = days)
	else:
		if request.form['password'] == request.form['confirm_password']:	
			dob = datetime(int(request.form['year']), int(request.form['month']), int(request.form['day']))
			user = Person(name = request.form['name'],
							gender = request.form['gender'],
							nationality = request.form['nationality'],
							city = request.form['city'],
							email = request.form['email'],
							password = request.form['password'],
							genre = request.form['genre'],
							phone = request.form['phone'],
							dob = dob)
			session.add(user)
			#Instruments
			instruments = request.form.getlist('instrument')
			if not (len(instruments) == 1 and instruments[0] == ''):#check if there is input of instruments
				if instruments[-1] == '':
					instruments.pop()
				for instrument in instruments:
					instrument_object = session.query(Instrument).filter_by(name=instrument).first()
					if not instrument_object:
						instrument_object = Instrument(name = instrument)
						session.add(instrument_object)		
					user.instrument.append(instrument_object)
				#Interersts
				tv_show = request.form['tv_shows']
				hobbie_object = session.query(Interests).filter_by(name=tv_show).first()
				if not hobbie_object:
					hobbie_object = Interests(name = tv_show)
					session.add(hobbie_object)		
				user.interests.append(hobbie_object)
					
				session.commit()
				return redirect(url_for('main'))
			else:
				return render_template('sign_up.html', years = years, months = months, days = days, error = True)
		else:
			return render_template('sign_up.html', years = years, months = months, days = days, error = True)

@app.route('/compare/<int:person_id>/')
def compare(person_id):
	user_object = session.query(Person).filter_by(id = flasksession['user_id']).first()
	print(user_object.name)
	person_object = session.query(Person).filter_by(id = person_id).first()
	print(person_object.name)	
	return render_template('compare.html', person = person_object , user = user_object)

if __name__ == '__main__':
    app.run(debug=True)


#fix adding date after error in sign up 
#  delete from list of instruments in sing up the other (check if one is empty and delete it)
