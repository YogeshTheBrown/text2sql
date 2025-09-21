from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from ingestion.loader import load_data



if __name__ == "__main__":
    docs = load_data() # loading data from json file
    # print(docs)
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

    context = []
    for r in results:
        # print(r.page_content)
        context.append(r.page_content)
    
    results

    # inject the retrieved docs into the prompt template

    llm = OllamaLLM(model="gemma3:4b", temperature=0.1)

    template = """
    You are an expert SQL/data assistant. 
    Use the following schema context to generate the sql query for the question. 
    If you cannot find an answer from the context, say "Not enough information."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    RAG_PROMPT = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type="stuff",  # simplest, dumps context as is
        chain_type_kwargs={"prompt": RAG_PROMPT},
        return_source_documents=True
    )

    query = "Which artist has most songs, I want result with artist name and which song was sung?"

    response = qa_chain.invoke(query)

    print("Answer:", response['result'])

    print("\n\nSource documents:")
    for doc in response['source_documents']:
        print(doc.page_content)
