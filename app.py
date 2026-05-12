from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patient.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Patient Table
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    disease = db.Column(db.String(200))

# Create Database
with app.app_context():
    db.create_all()

# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':
            return redirect(url_for('dashboard'))

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Add Patient
@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        disease = request.form['disease']

        patient = Patient(name=name, age=age, disease=disease)

        db.session.add(patient)
        db.session.commit()

        return redirect(url_for('view_patients'))

    return render_template('add_patient.html')

# View Patients
@app.route('/patients')
def view_patients():
    patients = Patient.query.all()
    return render_template('view_patients.html', patients=patients)

# Update Patient
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_patient(id):
    patient = Patient.query.get(id)

    if request.method == 'POST':
        patient.name = request.form['name']
        patient.age = request.form['age']
        patient.disease = request.form['disease']

        db.session.commit()

        return redirect(url_for('view_patients'))

    return render_template('update_patient.html', patient=patient)

# Delete Patient
@app.route('/delete/<int:id>')
def delete_patient(id):
    patient = Patient.query.get(id)

    db.session.delete(patient)
    db.session.commit()

    return redirect(url_for('view_patients'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)