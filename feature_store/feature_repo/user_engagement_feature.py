from feast import Entity, FeatureView, Field, FileSource
from feast.value_type import ValueType
from feast.types import Float32, String

# Define the entity for joining
user = Entity(
    name="user_id",
    join_keys=["user_id"],
    value_type=ValueType.INT64
)

# Define your file source for the Parquet data, with explicit timestamp field
user_engagement_source = FileSource(
    path="../data_ingestion/user_events.parquet",      # path is relative to feature_store.yaml
    timestamp_field="timestamp",                       # specify only one timestamp field
    created_timestamp_column="created"
)

# Define the feature view
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
