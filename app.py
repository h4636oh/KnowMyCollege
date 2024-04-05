from flask import Flask, render_template, request, jsonify, redirect
import pandas as pd
# import gunicorn 
from response import user_input
import os

# Taking the Data Base
app = Flask(__name__, static_folder='static')

file_path = os.path.join(app.root_path, 'static/DataBase.csv')
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
    college_names=[]
    Branch_names=[]
    Placement=[]
    coding=[]
    campus=[]
    cultural=[]
    entrupr=['Entrepreneurship_Culture']
    for index, row in sorted_df.iterrows():
        college_name = row['College Name']
        Branch_name = row['Branch']
        PLA=row['Placement ']
        Co=row['Coding_Culture']
        Ca=row['Campus']
        CU=row['Cultural_Activity']
        en=row['Entrepreneurship_Culture']
        V6= row['Total']
        V6=V6/500
        V6=round(V6,1)
        
        
        V4= row['CLOSING']
        if int(rankAIR)-2000<= V4:
            college_names.append(college_name)
            Branch_names.append(Branch_name)
            Placement.append(PLA)
            coding.append(Co)
            campus.append(Ca)
            cultural.append(CU)
            entrupr.append(en)            
            
            Values.append(V6)
    
    return college_names,Branch_names,Values,Placement,coding,campus,cultural,entrupr


def get_branches_and_closing(college_name):
    college_data = df[df['College Name'] == college_name]
    if college_data.empty:
        return None, None  # Return None if college not found
    else:
        main_branches = college_data['Branch'].unique().tolist()
        closing_ranks = college_data[college_data['Branch'] == college_data['Parent Branch']]['CLOSING'].tolist()
        return main_branches, closing_ranks
First_one=[]
Second_one=[]
Name1=""
Name2=""
Para=['Placement','Coding Culture','Campus','Cultural Activity','Entrepreneurship Culture']
def comper(selected_data):
    ranks = [entry['rank'] for entry in selected_data]
    colleges = [entry['college'] for entry in selected_data]
    college_First=colleges[0]
    college_Second=colleges[1]
    a=int(ranks[0])-1
    b=int(ranks[1])-1
    First_one.clear()
    Second_one.clear()
    Name1=college_First
    Name2=college_Second
    print(Name1)
    
    print(a)
    print(b)
    for j in range(3,8):
        
        First_one.append(Final_List[a][j])
        Second_one.append(Final_List[b][j])


    First_one.append(Name1)
    Second_one.append(Name2)


    print(First_one)



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('./index.html')

Final_List = [[],[]]




 
@app.route('/process_selection', methods=['POST','GET'])
def process_selection():
    if request.method == "POST":    
        selected_data = request.json
        comper(selected_data) 
        return redirect('/compare') 
    print("zzz")
    return redirect('/compare') 






@app.route('/compare', methods=['POST','GET'])
def compare_page():
        print("hello")
        print(Name1)
        # return render_template('./compareresult.html')
        return render_template('./compareresult.html', First_one=First_one, Second_one=Second_one, Para=Para,Name1=Name1,Name2=Name2)
        
        


        
    
        

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
        college_names,Branch_names,Values,a,b,c,d,e=Value(rankAIR,df,placement_pref,coding_pref,campus_size_value,higher_studies_pref,states,culturalPref,preferences,tag_pref,startupPref)
        Final_List.clear()
        ctt = 1
        for i in range(len(college_names)):
            tempo = [ctt, college_names[i],Branch_names[i],Values[i],a[i],b[i],c[i],d[i],e[i]]
            Final_List.append(tempo)
            ctt+=1
        
        print(Final_List)      

        return redirect('/college')
    return render_template('/form.html')


@app.route('/college')
def college_page():
    my_list = Final_List
    return render_template('college.html', my_list=my_list)



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
        bot_response_temp = user_input(question)
        bot_response=bot_response_temp["output_text"]
        # Append the bot's response to the messages list
        messages.append({'sender': 'bot', 'content': bot_response})
    return render_template('aichatbot.html', messages=messages)


@app.route('/college/<college_name>', methods=['GET'])
def college_info(college_name):
    college_name = college_name.replace('_', ' ')
    # Find the college information based on the provided name
    branches, closing_ranks = get_branches_and_closing(college_name)
    if branches is None or closing_ranks is None:
        return render_template('college_not_found.html')
    else:
        branch_closing_list = list(zip(branches, closing_ranks))
        return render_template('college_page.html', college_name=college_name, branch_closing_list=branch_closing_list)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)