from datetime import timedelta
from feast import Entity, FeatureView, Field, PushSource, FileSource
from feast.types import Float32, Int64

# 1. Define the Entity
user = Entity(name="user_id", join_keys=["user_id"])

# 2. Define the Push Source (Allows us to push from Kafka -> Feast)
user_stats_push_source = PushSource(
    name="user_stats_push_source",
    batch_source=FileSource(
        file_format="parquet",
        path="data/historical_data.parquet",
        timestamp_field="event_timestamp"
    )
)

# 3. Define the Feature View
user_activity_view = FeatureView(
    name="user_activity_view",
    entities=[user],
    ttl=timedelta(days=1),
    schema=[
        Field(name="clicks", dtype=Int64),
        Field(name="session_duration", dtype=Float32),
    ],
    online=True,
    source=user_stats_push_source,
)