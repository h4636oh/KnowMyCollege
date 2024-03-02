from flask import Flask, render_template, request, jsonify
import pandas as pd

# Taking the Data Base
file_path = 'static/DataBase - Sheet1.csv'
df = pd.read_csv(file_path)

# function for Data Base
def Value(rankAIR, df, placement_pref, coding_pref, campus_size_value, higher_studies_pref, states,Cultural_Pref,Branches,brand_value,Entra ):
    totals = []
    for index, row in df.iterrows():
        total = 0
        value1 = row['Placement ']
        value2 = row['Coding_Culture']
        value3 = row['Campus']
        value4_temp = row['Higher Eduction']
        
        value4=0
        if higher_studies_pref == 'y':
            value4 += 100
        else:
            value4 += 0

        value5 = 0
        arr = [100, 90, 80, 70, 60,50,40,30]
        for i in range(8):
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
        value9= row['Entrepreneurship_Culture']
        
                
                   
        

        total += int(placement_pref) * int(value1)
        total += int(coding_pref) * value2
        total += int(campus_size_value) * value3
        total += int(value4_temp) * value4
        total += int(value5)
        total += int(value6)*int(Cultural_Pref)
        total += value7_f
        total += value8*int(brand_value)
        total += value9*int(Entra)
        totals.append(total)
    LIST=[]
    df['Total'] = totals
    # filtered_df = df[df['Rank_Cutoff'] <= int(rankAIR)]
    sorted_df = df.sort_values(by='Total', ascending=False)
    # sorted_df = df.sort_values(by='Total', ascending=False)
    
    for index, row in sorted_df.iterrows():
        V1 = row['collage name']
        V2 = row['Branch']
        V3 = f"{V1} {V2}"  # Concatenating strings using f-string
        V4= row['CLOSING']
        if rankAIR-2000<= V4:
            LIST.append(V3)
    return LIST
#Sta = ['Chhattisgarh', 'Uttar Pradesh', 'Odisha', 'Maharashtra', 'Jharkhand']
#bra=['COMPUTER SCIENCE AND ENGINEERING','None','None','None','None','None','None','None']
#A=Value(df, 100, 100, 10, 'y', Sta,100,bra,50,50)
#print(A)





app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('./index.html')



campus_size_value = None  # Define a global variable

Final_List = [[],[]]

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
        
        culturalPref = request.form.get("culturalPref")
        print("culturalPref:", culturalPref) 

        startupPref = request.form.get("startupPref")
        print("startupPref:", startupPref) 

        states = []
        for i in range(1, 9):
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
        print("Selected Preferences:", preferences)
        TEMP=Value(rankAIR,df,placement_pref,coding_pref,campus_size_value,higher_studies_pref,states,culturalPref,preferences,tag_pref,startupPref)
        Final_List.clear()
        ctt = 1
        for i in TEMP:
            tempo = [ctt, i]
            Final_List.append(tempo)
            ctt+=1

    return render_template('form.html')

@app.route('/college')

def college_page():
    my_list = Final_List
    return render_template('college.html', my_list=my_list)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)