
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

from langchain_community.document_loaders.csv_loader import CSVLoader


def get_conversational_chain():

    prompt_template = """
    You are a College Counselor. 
    Your role is to provide detailed and enthusiastic answers to questions based on the provided context. 
    Ensure to include all relevant details, even the smaller ones.
    Aim to provide comprehensive responses, elaborating on various aspects. 
    If the answer is not available in the provided context, simply state, 
    "Answer is not available in the context," and avoid providing incorrect information.

    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.8,google_api_key="AIzaSyBPvN2LK5zayUy3_5IAa02q_RzReiCrdxc")

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def get_conversational_chain_csv():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details,
    first convert the question into simpal data base question then serch through database and output the answer in natural langauage providing reasoning 
    answer   if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3,google_api_key="AIzaSyBPvN2LK5zayUy3_5IAa02q_RzReiCrdxc")

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain


def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001",google_api_key="AIzaSyBPvN2LK5zayUy3_5IAa02q_RzReiCrdxc")
    
    new_db = FAISS.load_local("static/faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)
    print(response)
    return response

loader = CSVLoader(file_path="Database.csv")
data = loader.load()


def user_input_csv(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain_csv()

    
    response = chain( {"input_documents":data, "question": user_question}, return_only_outputs=True)
    print(response)
    print(1)
    return response
    
    
    


def main():
    question="which college has best placement and provide data supporting it"
    
    
if __name__=="__main__":
    main()    
    