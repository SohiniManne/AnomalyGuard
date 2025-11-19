import pandas as pd
import os

# Sample data for user engagement
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

print("Sample user engagement data saved.")
