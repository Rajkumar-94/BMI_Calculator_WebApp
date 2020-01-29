"""
This is a Flask application that can be used to interview QA engineers. 
All the application does is to calculate the factorial of a number. 
But there have been bugs seeded. For example, this application will go into an infinite loop if you pass it a negative number.
To learn more, see the README.md of this application.
"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calculate_bmi(w,h):
    "Calculate the factorial of a number"
#    if n==0:
#        return 1
#    else:
    return round(w/(h*h),2)

@app.route("/", methods=['GET', 'POST'])
@app.route("/bmicalculator", methods=['GET', 'POST'])
def bmi_calculator():
    "Endpoint for calculating the factorial of a number"
    if request.method == 'GET':
        #return the form
        return render_template('bmi_calculator.html')
    if request.method == 'POST':
        #return the answer
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        result = calculate_bmi(weight,height)
        api_response = {"answer": result}
        return jsonify(api_response)

@app.route("/terms")
def terms_and_conditions():
    "Return terms and conditions"
    return "This is the terms and conditions document. We are not yet ready with it. Stay tuned!"

@app.route("/privacy")
def privacy():
    "Return privacy statement"
    return "This is the privacy document. We are not yet ready with it. Stay tuned!"
    

#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464, debug= True)