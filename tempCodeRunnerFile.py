def get_conversational_chain_csv():

#     prompt_template = """
#     Answer the question as detailed as possible from the provided context, make sure to provide all the details,
#     first convert the question into simpal data base question then serch through database and output the answer in natural langauage providing reasoning 
#     answer   if the answer is not in
#     provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
#     Context:\n {context}?\n
#     Question: \n{question}\n

#     Answer:
#     """

#     model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3,google_api_key="AIzaSyBPvN2LK5zayUy3_5IAa02q_RzReiCrdxc")

#     prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
#     chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

#     return chain
