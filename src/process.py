import string

import pandas as pd  # type: ignore
from nltk.corpus import stopwords  # type: ignore
from nltk.stem import WordNetLemmatizer  # type: ignore


class Process:
    def __init__(self):
        self.punctuation = string.punctuation
        # https://cs.stanford.edu/people/sonal/gupta14jamia_supl.pdf
        medical_stopwords_list1 = [
            "disease",
            "diseases",
            "disorder",
            "symptom",
            "symptoms",
            "drug",
            "drugs",
            "problems",
            "problem",
            "prob",
            "probs",
            "med",
            "meds",
            "pill",
            "pills",
            "medicine",
            "medicines",
            "medication",
            "medications",
            "treatment",
            "treatments",
            "caps",
            "capsules",
            "capsule",
            "tablet",
            "tablets",
            "tabs",
            "doctor",
            "dr",
            "dr.",
            "doc",
            "physician",
            "physicians",
            "test",
            "tests",
            "testing",
            "specialist",
            "specialists",
            "side-effect",
            "side-effects",
            "pharmaceutical",
            "pharmaceuticals",
            "pharma",
            "diagnosis",
            "diagnose",
            "diagnosed",
            "exam",
            "challenge",
            "device",
            "condition",
            "conditions",
            "suffer",
            "suffering",
            "suffered",
            "feel",
            "feeling",
            "prescription",
            "prescribe",
            "prescribed",
            "over-the-counter",
            "otc",
            "contain",
            "contains",
        ]
        medical_stopwords_list2 = pd.read_csv(
            "https://raw.githubusercontent.com/kavgan/clinical-concepts/master/clinical-stopwords.txt"
        )["#regular stop words with clinical"].tolist()
        medical_stopwords = medical_stopwords_list1 + medical_stopwords_list2
        english_stopwords = ", ".join(stopwords.words("english"))
        english_stopwords = english_stopwords.split(",")
        self.total_stopwords = medical_stopwords + english_stopwords
        self.fields = ["Medical_Description", "Sample"]
        self.lemmatizer = WordNetLemmatizer()

    def process_data(self, df):
        df = self.drop_nans(df)
        for field in self.fields:
            # Lowercase
            df[field] = df[field].str.lower()
            # Stopwords Removal
            df[field] = df[field].apply(lambda text: self.remove_stopwords(text))
            # Text Lemmatization
            df[field] = df[field].apply(lambda text: self.lemmatize_words(text))
        return df

    def remove_stopwords(self, text):
        return " ".join(
            [word for word in str(text).split() if word not in self.total_stopwords]
        )

    def lemmatize_words(self, text):
        return " ".join([self.lemmatizer.lemmatize(word) for word in text.split()])

    def drop_nans(self, df):
        # if nan either field drop it
        for field in self.fields:
            df = df.loc[df[field].notna()]
        return df


if __name__ == "__main__":
    df = pd.read_csv("../data/raw/Case_Study_Data.csv")
    process = Process()
    processed_df = process.process_data(df)
    processed_df.to_csv("../data/interim/processed_data.csv", index=False)
