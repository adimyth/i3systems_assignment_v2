import pandas as pd  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.preprocessing import LabelEncoder  # type: ignore


def split_data(path):
    # Load Data
    df = pd.read_csv(path)
    # Stratified Split
    X_train, X_valid, y_train, y_valid = train_test_split(
        df["Medical_Description"],
        df["Package"],
        stratify=df["Package"].tolist(),
        random_state=42,
    )
    # Label Encode
    label_encoder = LabelEncoder()
    y_train = label_encoder.fit_transform(y_train)
    y_valid = label_encoder.transform(y_valid)
    # Save Data
    train_data = pd.DataFrame({"Medical_Description": X_train, "Package": y_train})
    valid_data = pd.DataFrame({"Medical_Description": X_valid, "Package": y_valid})
    train_data.to_csv("../data/processed/train.csv", index=False)
    valid_data.to_csv("../data/processed/valid.csv", index=False)


if __name__ == "__main__":
    split_data("../data/interim/processed_data.csv")
