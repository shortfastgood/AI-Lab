import argparse
from huggingface_hub import snapshot_download
from langchain.document_loaders import DirectoryLoader, PDFMinerLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from pathlib import Path
import os

# Download model from HuggingFace Hub
# @param model_id: The model id to download.
def dowload_model(model_id):
    model_dir = f"{Path.home()}/LLM/{model_id}"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    snapshot_download(model_id, revision="main", local_dir=model_dir, local_dir_use_symlinks=False)

# Check if the input is an existing readable directory.
# @param filepath: The path to the directory.
# @return: True if the directory exists and is readable, False otherwise.
def is_existing_readable_directory(filepath: str) -> bool:
    return os.path.isdir(filepath) and os.access(filepath, os.R_OK)


# Check if the input is an existing readable file.
# @param filepath: The path to the file.
# @return: True if the file exists and is readable, False otherwise.
def is_existing_readable_file(filepath: str) -> bool:
    return os.path.isfile(filepath) and os.access(filepath, os.R_OK)


# load configuration file
def load_config(config_path):
    properties = {}
    with open(config_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                properties[key] = value
    return properties

def load_split_and_vectorize(folder, target, embeddings):
    loader = DirectoryLoader(folder, recursive=True, loader_cls=PDFMinerLoader, show_progress=True)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    docs = text_splitter.split_documents(documents)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("opdf_index")
    return db

config_file = f"{os.getcwd()}/config.properties"
data_dir = "./data"
index_dir = "./index"
properties = {}
model_path = ""

if __name__ == "__main__":
    if is_existing_readable_file(config_file):
        properties = load_config(config_file)
    else:
        print(f"The configuration file '{config_file}' file is missing!")
        exit(1)

    # check data directory
    if (properties["data.default"] is not None) and (
        properties["data.default"] != ""
    ):
        data_dir = properties["data.default"]

    # check index directory
    if (properties["index.default"] is not None) and (
        properties["index.default"] != ""
    ):
        index_dir = properties["index.default"]

    # load database from disk, otherwise create
    embeddings = HuggingFaceEmbeddings()
    try:
        db = FAISS.load_local(index_dir, embeddings)
    except:
        print('no index on disk, creating new...')
        db = load_split_and_vectorize(data_dir, index_dir, embeddings)
        print('... index created successfully!')


    # select model
    if (properties["model.default"] is not None) and (
        properties["model.default"] != ""
    ):
        model_path = f"{Path.home()}/LLM/{properties['model.default']}"

    if not is_existing_readable_directory(model_path):
        print(f"The LLM model '{model_path}' is missing!, starting download...")
        dowload_model(properties["model.default"])
        print(f"Model '{properties['model.default']}' ... downloaded successfully!")