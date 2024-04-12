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
    # A List to store all the Values after addition
    totals = []
    # iterreting through dataframe by row 
    for index, row in df.iterrows():
        total = 0
        Placement_value = row['Placement ']
        Coding_Culture = row['Coding_Culture']
        Campus = row['Campus']
        Higher_Education_Value = row['Higher Education']
        
        
        Higher_Education_Pref=0
        if higher_studies_pref == 'y':
            Higher_Education_Pref += 100
        

        Location_Pref = 0
        States_Val = [100, 81, 64, 49, 36,25,16,9]
        for i in range(len(states)):
            if states[i] == row['STATE']:
                Location_Pref += States_Val[i]
                
        Cultural_Activity = row['Cultural_Activity'] 
        
        Branch= row['Parent Branch']
        Branch_Pref=0
        Branch_Priority=[100,88,76,64,52,40,28,16]
        
        for i in range(len(Branches)):
            if Branch== Branches[i]:
                Branch_Pref+=Branch_Priority[i]
                
        Brand_Value = row['Brand_Value']
        Entrepreneurship_Culture= row['Entrepreneurship_Culture']
        
                
        total += int(placement_pref) * Placement_value*3
        total += int(coding_pref) * Coding_Culture*2
        total += int(campus_size_value) * Campus*0.5
        total += int(Higher_Education_Value) * Higher_Education_Pref
        total += int(Location_Pref)
        total += int(Cultural_Activity)*int(Cultural_Pref)*2
        total += Branch_Pref*5
        total += Brand_Value*int(brand_value)*1
        total += Entrepreneurship_Culture*int(Entra)*4
        totals.append(total)
    #sorting DataFrame by Total
    df['Total'] = totals   
    sorted_df = df.sort_values(by='Total', ascending=False)
    # crating List which we want Latter
    Values=[]
    college_names=[]
    Branch_names=[]
    Placement=[]
    coding=[]
    campus=[]
    cultural=[]   
    Entrepreneurship=[]
    # Iterrating through the DataFrame 
    for index, row in sorted_df.iterrows():
        college_name = row['College Name']
        Branch_name = row['Branch']
        Placement_Value=row['Placement ']
        Coding_Culture=row['Coding_Culture']
        Campus=row['Campus']
        Cultural_Activity=row['Cultural_Activity']
        Entrepreneurship_Culture=row['Entrepreneurship_Culture']
        Total_sum= row['Total']
        Total_sum=Total_sum/500
        Total_sum=round(Total_sum,1)                
        Closing= row['CLOSING']
        
        # if its Closing rank is less than the canditaes AIR with some relaxation appending it to list
        if int(rankAIR)-2000<= Closing:
            college_names.append(college_name)
            Branch_names.append(Branch_name)
            Placement.append(Placement_Value)
            coding.append(Coding_Culture)
            campus.append(Campus)
            cultural.append(Cultural_Activity)
            Entrepreneurship.append(Entrepreneurship_Culture)                        
            Values.append(Total_sum)
    
    return college_names,Branch_names,Values,Placement,coding,campus,cultural,Entrepreneurship

# Funtion to get Closing Rank of Colleges 
def get_branches_and_closing(college_name):
    college_data = df[df['College Name'] == college_name]
    if college_data.empty:
        return None, None  # Return None if college not found
    else:
        main_branches = college_data['Branch'].unique().tolist()
        closing_ranks = college_data[college_data['Branch'] == college_data['Parent Branch']]['CLOSING'].tolist()
        return main_branches, closing_ranks

# Global Variabel For compare two colleges 
First_College=[]
Second_College=[]
Name1=""
Name2=""
Para=['Placement','Coding Culture','Campus','Cultural Activity','Entrepreneurship Culture']

# Function TO compare 2 colleges
def compare(selected_data):
    ranks = [entry['rank'] for entry in selected_data]
    colleges = [entry['college'] for entry in selected_data]
    First_college_name=colleges[0]
    Second_college_name=colleges[1]
    a=int(ranks[0])-1
    b=int(ranks[1])-1
    First_College.clear()
    Second_College.clear()
    
    #function to append values from Final List
    for j in range(3,8):
        
        First_College.append(Final_List[a][j])
        Second_College.append(Final_List[b][j])


    First_College.append(First_college_name)
    Second_College.append(Second_college_name)


    


#Home Route  
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('./index.html')

# Route to compare 2 colleges 
@app.route('/process_selection', methods=['POST','GET'])
def process_selection():
    if request.method == "POST":    
        selected_data = request.json
        compare(selected_data) 
        return redirect('/compare')     
    return redirect('/compare') 


#route to compare 2 colleges
@app.route('/compare', methods=['POST','GET'])
def compare_page():
        
        return render_template('./compareresult.html', First_one=First_College, Second_one=Second_College, Para=Para,Name1=Name1,Name2=Name2)
        
            
campus_size_value = None 
#floble LIST to acces it from any were
Final_List = [[],[]]
# form page to get values from user
@app.route('/form', methods=['GET', 'POST'])
def form():
    global campus_size_value 
    if request.method == "POST":
        #function to get values from form.html
        rankAIR = request.form.get("rankAIR")
        placement_pref = request.form.get("placementPref") 
        coding_pref = request.form.get("codingPref")
        campus_size_value = request.form.get("campusSize")
        higher_studies_pref = request.form.get("higherStudiesPref")
        tag_pref = request.form.get("codingPref")        
        culturalPref = request.form.get("culturalPref")  
        startupPref = request.form.get("startupPref")        

        states = []
        for i in range(1, 9):
            state = request.form.get(f'choice{i}')
            if state:
                states.append(state)
        
        preferences = [] 
        for i in range(1, 9):
            preference = request.form.get(f"preference{i}")
            if preference:
                preferences.append(preference)

        #function to add values to final list
        college_names,Branch_names,Values,a,b,c,d,e=Value(rankAIR,df,placement_pref,coding_pref,campus_size_value,higher_studies_pref,states,culturalPref,preferences,tag_pref,startupPref)
        Final_List.clear()
        ctt = 1
        for i in range(len(college_names)):
            tempo = [ctt, college_names[i],Branch_names[i],Values[i],a[i],b[i],c[i],d[i],e[i]]
            Final_List.append(tempo)
            ctt+=1        
             

        return redirect('/college')
    return render_template('/form.html')

#college route
@app.route('/college')
def college_page():
    my_list = Final_List
    return render_template('college.html', my_list=my_list)


# local storing ai chatbot messege
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