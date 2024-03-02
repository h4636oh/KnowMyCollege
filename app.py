from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/college')
def college_page():
    items = [{'college': "IITB", 'placement': 20000}]
    return render_template('college.html', items=items)

campus_size_value = None  # Define a global variable

@app.route('/form', methods=['GET', 'POST'])
def form():
    global campus_size_value  # Access the global variable
    if request.method == "POST":
        placement_pref = request.form.get("placementPref")
        print("Placement Preference:", placement_pref) 

        coding_pref = request.form.get("codingPref")
        print("Coding Preference:", coding_pref) 

        campus_size_value = request.form.get("campusSize")
        print("Campus Size:", campus_size_value) 

        higher_studies_pref = request.form.get("higherStudiesPref")
        print("Higher Studies Preference:", higher_studies_pref) 

        states = []
        for i in range(1, 6):
            state = request.form.get(f'choice{i}')
            if state:
                states.append(state)
        print("Your Selected Indian States:")
        for state in states:
            print(state)

    return render_template('form.html')
# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
