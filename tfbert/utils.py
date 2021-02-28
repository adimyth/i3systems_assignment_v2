import pandas as pd
from transformers import BertTokenizer

# function to decide `max_len` hyperparameter
def get_max_len(sentences):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
    max_len = 0
    for sent in sentences:
        # Tokenize the text and add `[CLS]` and `[SEP]` tokens.
        input_ids = tokenizer.encode(sent, add_special_tokens=True)
        # Update the maximum sentence length.
        max_len = max(max_len, len(input_ids))
    print('Max sentence length: ', max_len)


if __name__ == "__main__":
    df = pd.read_csv("../data/processed/train.csv")
    sentences = df["Medical_Description"].tolist()
    get_max_len(sentences)