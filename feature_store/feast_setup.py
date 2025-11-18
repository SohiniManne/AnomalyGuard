from feast import Entity, FeatureView, Field, FileSource
from feast.value_type import ValueType
from feast.types import Float32, String
import pandas as pd
import os

sample_data = pd.DataFrame({
    "user_id": [1, 2, 3],
    "feature1": [0.1, 0.4, 0.3],
    "feature2": [0.5, 0.2, 0.8],
    "event_type": ["click", "view", "like"],
    "timestamp": pd.to_datetime([
        "2025-11-13 08:00:00", "2025-11-13 08:01:00", "2025-11-13 08:02:00"
    ]),
    "created": pd.to_datetime([
        "2025-11-13 08:00:00", "2025-11-13 08:01:00", "2025-11-13 08:02:00"
    ]),
})

os.makedirs("../data_ingestion", exist_ok=True)
sample_data.to_parquet("../data_ingestion/user_events.parquet", index=False)

user = Entity(name="user_id", join_keys=["user_id"], value_type=ValueType.INT64)
user_engagement_source = FileSource(
    path="../data_ingestion/user_events.parquet",
    event_timestamp_column="timestamp",
    created_timestamp_column="created"
)
user_engagement_features = FeatureView(
    name="user_engagement",
    entities=[user],
    ttl=None,
    schema=[
        Field(name="feature1", dtype=Float32),
        Field(name="feature2", dtype=Float32),
        Field(name="event_type", dtype=String),
    ],
    source=user_engagement_source,
)

if __name__ == "__main__":
    print("Sample data and Feast feature definitions are ready.")
