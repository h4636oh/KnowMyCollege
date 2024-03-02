from flask import Flask, render_template, request, jsonify
import pandas as pd

# Taking the Data Base
file_path = 'D:\DEV\KnowMyCollege\static\DataBase.csv'
df = pd.read_csv(file_path)

# function for Data Base
def Value(df, placement_pref, coding_pref, campus_size_value, higher_studies_pref, states,Cultural_Pref,Branches,brand_value,Entra ):
    totals = []
    for index, row in df.iterrows():
        total = 0
        value1 = row['Placement ']
        value2 = row['Coding_Cultuter']
        value3 = row['Campus']
        value4_temp = row['Higer Eduction']
        
        value4=0
        if higher_studies_pref == 'y':
            value4 += 100
        else:
            value4 += 0

        value5 = 0
        arr = [100, 90, 80, 70, 60]
        for i in range(5):
            if states[i] == row['STATE']:
                value5 = arr[i]
                
        value6 = row['Cultural_Activity'] 
        
        value7= row['Parent Branch']
        value7_f=0
        arr2=[100,88,76,64,52,40,28,16]
        
        for i in range(len(Branches)):
            if value7== Branches[i]:
                value7_f+=arr2[i]
                
        value8= row['Brand_Value']
        value9= row['Entreaprenurship_Culture']
        
                
                   
        

        total += placement_pref * value1
        total += coding_pref * value2
        total += campus_size_value * value3
        total += value4_temp * value4
        total += value5
        total += value6*Cultural_Pref
        total += value7_f
        total += value8*brand_value
        total += value9*Entra
        totals.append(total)

    df['Total'] = totals
    print(df['Total'])

#Sta = ['Chhattisgarh', 'Uttar Pradesh', 'Odisha', 'Maharashtra', 'Jharkhand']
#Value(df, 100, 100, 10, 'y', Sta)
#print(df.columns)





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

        rankAIR = placement_pref = request.form.get("rankAIR")
        print("Rank:", rankAIR) 

        placement_pref = request.form.get("placementPref")
        print("Placement Preference:", placement_pref) 

        coding_pref = request.form.get("codingPref")
        print("Coding Preference:", coding_pref) 

        campus_size_value = request.form.get("campusSize")
        print("Campus Size:", campus_size_value) 

        higher_studies_pref = request.form.get("higherStudiesPref")
        print("Higher Studies Preference:", higher_studies_pref) 

        tag_pref = request.form.get("codingPref")
        print("codingPref:", tag_pref) 

        startupPref = request.form.get("startupPref")
        print("startupPref:", startupPref) 

        states = []
        for i in range(1, 6):
            state = request.form.get(f'choice{i}')
            if state:
                states.append(state)
        print("Your Selected Indian States:")
        for state in states:
            print(state)


    preferences = []  # Initialize an empty list to store preferences

    # Retrieve and store preferences 1 to 8
    for i in range(1, 9):
        preference = request.form.get(f"preference{i}")
        if preference:
            preferences.append(preference)

    # Process the preferences as needed
    for pr in preferences:
        print(pr)

    return render_template('form.html')
# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
