from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


# docs = [
#     "This is the test doc",
#     "We are testing the ollama embeddings",
# ]

# embedding = embedder.embed_documents(docs)

# print("Embedding shape : ", len(embedding), "x", len(embedding[0]))


from ingestion.loader import load_data

if __name__ == "__main__":
    docs = load_data() # loading data from json file
    print(docs)
    ### currently data chunking is not required will modify later ##
    
    # load the Ollama embedder
    embedder = OllamaEmbeddings(
        model="nomic-embed-text:latest"
        )
    
    # vectorstore = FAISS.from_texts(docs, embedder)
    # vectorstore.save_local("../data/embeddings/schema_index")
    # print("Vectorstore created and saved locally")

    vectorstore = FAISS.load_local("../data/embeddings/schema_index", embedder, 
                                   allow_dangerous_deserialization=True)

    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":3})

    query = "Which table has column name as title?"
    results = retriever.invoke(query)

    for r in results:
        print(r.page_content)
    

