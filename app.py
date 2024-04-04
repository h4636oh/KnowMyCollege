from flask import Flask, render_template, request, jsonify, redirect
import pandas as pd
# import gunicorn 
#from Responce import get_conversational_chain_csv

# Taking the Data Base
file_path = 'static/Database - Sheet1.csv'
df = pd.read_csv(file_path)

# function for Data Base
def Value(rankAIR, df, placement_pref, coding_pref, campus_size_value, higher_studies_pref, states,Cultural_Pref,Branches,brand_value,Entra ):
    totals = []
    for index, row in df.iterrows():
        total = 0
        value1 = row['Placement ']
        value2 = row['Coding_Culture']
        value3 = row['Campus']
        value4_temp = row['Higher Education']
        
        value4=0
        if higher_studies_pref == 'y':
            value4 += 100
        else:
            value4 += 0

        value5 = 0
        arr = [100, 81, 64, 49, 36,25,16,9]
        for i in range(len(states)):
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
        
                
                   
        

        total += int(placement_pref) * int(value1)*3
        total += int(coding_pref) * value2*2
        total += int(campus_size_value) * value3*0.5
        total += int(value4_temp) * value4
        total += int(value5)
        total += int(value6)*int(Cultural_Pref)*2
        total += value7_f*5
        total += value8*int(brand_value)*1
        total += value9*int(Entra)*4
        totals.append(total)
    LIST=[]
    df['Total'] = totals
    # filtered_df = df[df['Rank_Cutoff'] <= int(rankAIR)]
    sorted_df = df.sort_values(by='Total', ascending=False)
    # sorted_df = df.sort_values(by='Total', ascending=False)
    Values=[]
    for index, row in sorted_df.iterrows():
        V1 = row['College Name']
        V2 = row['Branch']
        V6= row['Total']
        V6=V6/500
        V6=round(V6,1)
        
        V3 = f"{V1} {V2}"  # Concatenating strings using f-string
        V4= row['CLOSING']
        if int(rankAIR)-2000<= V4:
            LIST.append(V3)
            Values.append(V6)
    
    return LIST,Values






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
        TEMP,V6=Value(rankAIR,df,placement_pref,coding_pref,campus_size_value,higher_studies_pref,states,culturalPref,preferences,tag_pref,startupPref)
        Final_List.clear()
        ctt = 1
        for i in range(len(TEMP)):
            tempo = [ctt, TEMP[i],V6[i]]
            Final_List.append(tempo)
            ctt+=1
        

        return redirect('/college')
    return render_template('/form.html')


@app.route('/college')
def college_page():
    my_list = Final_List
    return render_template('college.html', my_list=my_list)


@app.route('/ai')
def ai_page():
    return render_template('./ai.html')
messages = [
        {"sender": "bot", "content": "Welcome to the chatbot!"},
        {"sender": "bot", "content": "How can I assist you today?"}
    ]
@app.route('/ai_chatbot', methods=['GET', 'POST'])
def ai_chatbot():
    global messages
    if request.method == 'POST':
        # Get the user's question from the form
        question = request.form.get('question')
        # Append the user's question to the messages list
        messages.append({'sender': 'user', 'content': question})
        # Process the question and generate a bot response (dummy response for demonstration)
        bot_response = "This is a bot response."
        # Append the bot's response to the messages list
        messages.append({'sender': 'bot', 'content': bot_response})
    return render_template('aichatbot.html', messages=messages)
@app.route('/ai_colleges')
def ai_colleges():
    return render_template('ai_colleges.html')
@app.route('/ai_list')
def ai_list():
    return render_template('ai_list.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
