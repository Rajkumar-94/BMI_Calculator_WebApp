"""
This is a Flask application that can be used to interview QA engineers.
All the application does is to calculate the factorial of a number.
But there have been bugs seeded. For example, this application will go into an infinite loop if you pass it a negative number.
To learn more, see the README.md of this application.
"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calculate_bmi(w,h):
    "Calculate the Body mass index"
    return round(w/(h*h),2)

def weight_categogy(result):
    if result<=18.5:
        return "Under Weight"
    elif result>18.5 and result<25:
        return "Normal Weight"
    elif result>=25 and result<=29.9:
        return "Over Weight"
    elif result>30:
        return "Obese"

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
        result_category=weight_categogy(result)
        api_response = {"answer": result,"type_of":result_category}
        return jsonify(api_response)

#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464, debug= True)