import os
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App Config
    APP_NAME: str = "AnomalyGuard"
    DEBUG_MODE: bool = True
    
    # Kafka Configuration (Confluent Cloud)
    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_API_KEY: str
    KAFKA_API_SECRET: str
    KAFKA_TOPIC: str = "user_stream_v1"
    
    # Paths
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FEATURE_REPO_PATH: str = os.path.join(BASE_DIR, "feature_repo")
    MODEL_PATH: str = os.path.join(BASE_DIR, "services", "model.pkl")

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()