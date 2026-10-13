import streamlit as st
from dotenv import load_dotenv
from PyPDF2  import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_ollama import ChatOllama








def get_pdf_text(pdf_docs):
   text=""
   for pdf in pdf_docs:
      pdf_reader = PdfReader(pdf)
      for page in pdf_reader.pages:
         text += page.extract_text()
   return text 

def get_text_chucks(raw_text):
   text_splitter = CharacterTextSplitter(
      separator="\n",
      chunk_size=1000,
      chunk_overlap=200,
      length_function=len
   )
   chunks = text_splitter.split_text(raw_text)
   return chunks
   
def get_vectorstore(text_chucks):
   embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
   vectorstore = FAISS.from_texts(texts=text_chucks, embeddings=embeddings)
   return vectorstore

def get_conversation_chain(vectorstore):
   llm = ChatOllama()
   memory = ConversationBufferMemory(memory_key='chat_histroy', return_messages=True)
   conversion_chain = ConversationalRetrievalChain.from_llm()




def main():
    load_dotenv()
    st.set_page_config(page_title="Chat With Multiple PDFs",page_icon=":books:")

    st.header("Chat With Multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
            #get pdf text
             raw_text = get_pdf_text(pdf_docs)
             st.write(raw_text)

            #get the text chunks
            text_chucks = get_text_chucks(raw_text)
            st.write(text_chucks)

            #create vector store

            vectorstore = get_vectorstore(text_chucks)

            #create vonversion chain
            conversion = get_conversation_chain(vectorstore)
            


if __name__ == "__main__":
    main()