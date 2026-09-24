import os
from pathlib import Path

from pydantic_settings import BaseSettings

current_dir = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


class Settings(BaseSettings):
    AUTH_TYPE: str | None = None  # simple_jwt, session_jwt, or None
    LLM_PROVIDER: str = "docsgpt"
    LLM_NAME: str | None = (
        None  # if LLM_PROVIDER is openai, LLM_NAME can be gpt-4 or gpt-3.5-turbo
    )
    EMBEDDINGS_NAME: str = "huggingface_sentence-transformers/all-mpnet-base-v2"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"
    MONGO_URI: str = "mongodb://localhost:27017/docsgpt"
    MONGO_DB_NAME: str = "docsgpt"
    LLM_PATH: str = os.path.join(current_dir, "models/docsgpt-7b-f16.gguf")
    DEFAULT_MAX_HISTORY: int = 150
    LLM_TOKEN_LIMITS: dict = {
        "gpt-4o-mini": 128000,
        "gpt-3.5-turbo": 4096,
        "claude-2": 1e5,
        "gemini-2.5-flash": 1e6,
    }
    DEFAULT_AGENT_LIMITS: dict = {
        "token_limit": 50000,
        "request_limit": 500,
    }
    UPLOAD_FOLDER: str = "inputs"
    PARSE_PDF_AS_IMAGE: bool = False
    PARSE_IMAGE_REMOTE: bool = False
    VECTOR_STORE: str = (
        "faiss"  #  "faiss" or "elasticsearch" or "qdrant" or "milvus" or "lancedb"
    )
    RETRIEVERS_ENABLED: list = ["classic_rag"]
    AGENT_NAME: str = "classic"
    FALLBACK_LLM_PROVIDER: str | None = None  # provider for fallback llm
    FALLBACK_LLM_NAME: str | None = None  # model name for fallback llm
    FALLBACK_LLM_API_KEY: str | None = None  # api key for fallback llm

    # Google Drive integration
    GOOGLE_CLIENT_ID: str | None = (
        None  # Replace with your actual Google OAuth client ID
    )
    GOOGLE_CLIENT_SECRET: str | None = (
        None  # Replace with your actual Google OAuth client secret
    )
    CONNECTOR_REDIRECT_BASE_URI: str | None = (
        "http://127.0.0.1:7091/api/connectors/callback"  ##add redirect url as it is to your provider's console(gcp)
    )

    # GitHub source
    GITHUB_ACCESS_TOKEN: str | None = None # PAT token with read repo access

    # LLM Cache
    CACHE_REDIS_URL: str = "redis://localhost:6379/2"

    API_URL: str = "http://localhost:7091"  # backend url for celery worker

    API_KEY: str | None = None  # LLM api key
    EMBEDDINGS_KEY: str | None = (
        None  # api key for embeddings (if using openai, just copy API_KEY)
    )
    OPENAI_API_BASE: str | None = None  # azure openai api base url
    OPENAI_API_VERSION: str | None = None  # azure openai api version
    AZURE_DEPLOYMENT_NAME: str | None = None  # azure deployment name for answering
    AZURE_EMBEDDINGS_DEPLOYMENT_NAME: str | None = (
        None  # azure deployment name for embeddings
    )
    OPENAI_BASE_URL: str | None = (
        None  # openai base url for open ai compatable models
    )

    # elasticsearch
    ELASTIC_CLOUD_ID: str | None = None  # cloud id for elasticsearch
    ELASTIC_USERNAME: str | None = None  # username for elasticsearch
    ELASTIC_PASSWORD: str | None = None  # password for elasticsearch
    ELASTIC_URL: str | None = None  # url for elasticsearch
    ELASTIC_INDEX: str | None = "docsgpt"  # index name for elasticsearch

    # SageMaker config
    SAGEMAKER_ENDPOINT: str | None = None  # SageMaker endpoint name
    SAGEMAKER_REGION: str | None = None  # SageMaker region name
    SAGEMAKER_ACCESS_KEY: str | None = None  # SageMaker access key
    SAGEMAKER_SECRET_KEY: str | None = None  # SageMaker secret key

    # prem ai project id
    PREMAI_PROJECT_ID: str | None = None

    # Qdrant vectorstore config
    QDRANT_COLLECTION_NAME: str | None = "docsgpt"
    QDRANT_LOCATION: str | None = None
    QDRANT_URL: str | None = None
    QDRANT_PORT: int | None = 6333
    QDRANT_GRPC_PORT: int = 6334
    QDRANT_PREFER_GRPC: bool = False
    QDRANT_HTTPS: bool | None = None
    QDRANT_API_KEY: str | None = None
    QDRANT_PREFIX: str | None = None
    QDRANT_TIMEOUT: float | None = None
    QDRANT_HOST: str | None = None
    QDRANT_PATH: str | None = None
    QDRANT_DISTANCE_FUNC: str = "Cosine"

    # PGVector vectorstore config
    PGVECTOR_CONNECTION_STRING: str | None = None
    # Milvus vectorstore config
    MILVUS_COLLECTION_NAME: str | None = "docsgpt"
    MILVUS_URI: str | None = "./milvus_local.db"  # milvus lite version as default
    MILVUS_TOKEN: str | None = ""

    # LanceDB vectorstore config
    LANCEDB_PATH: str = "/tmp/lancedb"  # Path where LanceDB stores its local data
    LANCEDB_TABLE_NAME: str | None = (
        "docsgpts"  # Name of the table to use for storing vectors
    )

    FLASK_DEBUG_MODE: bool = False
    STORAGE_TYPE: str = "local"  # local or s3
    URL_STRATEGY: str = "backend"  # backend or s3

    JWT_SECRET_KEY: str = ""

    # Encryption settings
    ENCRYPTION_SECRET_KEY: str = "default-docsgpt-encryption-key"

    ELEVENLABS_API_KEY: str | None = None

path = Path(__file__).parent.parent.absolute()
settings = Settings(_env_file=path.joinpath(".env"), _env_file_encoding="utf-8")
