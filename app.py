from flask import Flask, render_template, request, jsonify
import pandas as pd

# Taking the Data Base
file_path= 'D:\DEV\KnowMyCollege\static\DataBase.csv'
df = pd.read_csv(file_path)
# function for Data Base
def Value(df,placement_pref,coding_pref,campus_size_value,higher_studies_pref,states):
    
    for index, row in df.iterrows():
        value1 = row['Placement']
        value2 = row['Coding_Cultuter']
        value3=  row['Campus']
        value4_temp= row['Higer Eduction']
        
        if value4_temp == 'y':
            value4=100
        else:
            value4=0
        
        
        value5=0
        arr=[100,90,80,70,60]
        for i in range(5):
            if states[i] == row['STATE']:
                value5=arr[i] 
        
            
        row['Total'] += placement_pref*value1
        row['Total'] += coding_pref* value2
        row['Total'] += campus_size_value*value3
        row['Total'] += higher_studies_pref*value4
        row['Total'] += value5
        
    print(df['Total'])
        
    




app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('./index.html')

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
