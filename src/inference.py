import pandas as pd

def encode_features(features, encoders, columns=None):
    encoded = []
    if columns is None:
        columns = list(encoders.keys())

    for col in columns:
        val = features.get(col, "Unknown")

        try:
            val_encoded = encoders[col].transform([str(val)])[0]
        except:
            val_encoded = 0

        encoded.append(val_encoded)

    return pd.DataFrame([encoded], columns=columns)