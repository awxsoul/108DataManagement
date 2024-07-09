# Importing the Flask module
from flask import Flask, render_template,request
import mysql.connector

# Create an instance of the Flask class
app = Flask(__name__)

#Database Connection
db = mysql.connector.connect(host="localhost", user="root", password="Basement2024",database="onezeroeight")
cursor = db.cursor()

#Query to get key details 
startq='''SELECT *
FROM onezeroeight.ambulance 
INNER JOIN onezeroeight.emergency_calls 
ON ambulance.amb_id=emergency_calls.amb_assigned
INNER JOIN onezeroeight.hospital 
ON hospital.hospital_id=emergency_calls.hospital_admitted
INNER JOIN onezeroeight.patient
ON patient.patient_id=emergency_calls.patient_id
INNER JOIN onezeroeight.timestamps
ON timestamps.op_info=emergency_calls.op_info'''

# Define a route for the root URL
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        formdata=[]
        formdata.append(request.form["stext"])
        formdata.append(request.form["searching"])

        if formdata[1]=="pat":
            cursor.execute(startq+" WHERE patient_name like '%"+str(formdata[0])+"%'")
        elif formdata[1]=="hos":
            cursor.execute(startq+" WHERE hospital_name like '%"+str(formdata[0])+"%'")
        elif formdata[1]=="amb":
            cursor.execute(startq+" WHERE reg_no like '%"+str(formdata[0])+"%'")
        elif formdata[1]=="call":
            cursor.execute(startq+" WHERE call_id like '%"+str(formdata[0])+"%'")
        else:
            cursor.execute(startq+" ORDER BY emergency_calls.call_id")
        x=cursor.fetchall()
        return render_template('index.html',t=formdata,data=x)
    

    
    else:
        cursor.execute(startq+" ORDER BY emergency_calls.call_id")
        x=cursor.fetchall()
        # Render the HTML template
        return render_template('index.html',data=x)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)