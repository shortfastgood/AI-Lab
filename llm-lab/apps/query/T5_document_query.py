from langchain.document_loaders import OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.chains.question_answering import load_qa_chain

from pathlib import Path

def load_split_vectorize(url,embeddings):
    loader = OnlinePDFLoader(url)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 10)
    docs = text_splitter.split_documents(documents)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("opdf_index")
    return db

# load database from disk, otherwise create
embeddings = HuggingFaceEmbeddings()
try:
    db = FAISS.load_local("opdf_index", embeddings)
except:
    print('no index on disk, creating new...')
    url = "https://support.riverbed.com/bin/support/download?did=b42r9nj98obctctoq05bl2qlga&version=9.14.2a"
    db = load_split_vectorize(url,embeddings)

# initialize pipeline
model_dir = f"{Path.home()}/LLM/MBZUAI/LaMini-Flan-T5-248M"
llm = HuggingFacePipeline.from_model_id(model_id=model_dir,
                                        task = 'text2text-generation',
                                        model_kwargs={"temperature":0.60, "min_length":35, "max_length":500, "repetition_penalty": 5.0, "do_sample": True})

# define chain
chain = load_qa_chain(llm, chain_type="stuff")

# run chain against your question
query = "What does fail-to-block mean for SteelHeads?"
docs = db.similarity_search(query)
print(chain.run(input_documents=docs, question=query))