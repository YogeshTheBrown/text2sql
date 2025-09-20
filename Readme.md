Description:

This project is aiming to generate the sql query for the specific custom databases using natural language.

text2sql/
│── README.md                 # Project overview, setup, usage instructions
│── requirements.txt           # Python dependencies 
│── .env.example               # Environment variable template
│── config/
│   ├── settings.yaml          # General project configs
│   ├── retriever.yaml         # Retriever/vector DB configs
│   └── llm.yaml               # Model configs (API keys, params)
│
├── data/
│   ├── raw/                   # Unprocessed input documents
│   ├── processed/             # Cleaned/structured data
│   ├── embeddings/            # Serialized vector embeddings
│   └── examples/              # Example queries/responses for testing
│
├── src/
│   ├── __init__.py
│   ├── ingestion/             # Data loading & preprocessing
│   │   ├── loader.py
│   │   └── preprocessor.py
│   │
│   ├── retriever/             # Vector store & retriever logic
│   │   ├── vectorstore.py
│   │   ├── retriever.py
│   │   └── chunking.py
│   │
│   ├── llm/                   # LLM interface and RAG pipeline
│   │   ├── llm_client.py
│   │   ├── rag_pipeline.py
│   │   └── prompts.py
│   │
│   ├── evaluation/            # Evaluation scripts (BLEU, ROUGE, accuracy, human eval)
│   │   ├── metrics.py
│   │   └── eval_pipeline.py
│   │
│   ├── utils/                 # Shared utilities
│   │   ├── logger.py
│   │   ├── helpers.py
│   │   └── config_loader.py
│   │
│   └── app.py                 # Main entry point (can serve as FastAPI/Streamlit app)
│
├── notebooks/                 # Jupyter notebooks for exploration & prototyping
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_embedding_tests.ipynb
│   └── 03_rag_pipeline_demo.ipynb
│
├── tests/                     # Unit and integration tests
│   ├── test_retriever.py
│   ├── test_llm.py
│   └── test_pipeline.py
│
└── docker/                    # Containerization setup
    ├── Dockerfile
    └── docker-compose.yml

# create the virtual env
uv venv .venv
uv pip install -r requirements.txt

