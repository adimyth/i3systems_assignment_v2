from pathlib import Path
from typing import List, Union

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from attrdict import AttrDict  # type: ignore
from pandas import DataFrame
from tensorflow.keras.utils import to_categorical  # type: ignore

from .dataset import BertDataset  # type: ignore
from .metrics import matthews_correlation  # type: ignore


class MedicalData:
    @staticmethod
    def describe_df(df: DataFrame, label: str) -> None:
        print(
            f"{label}\nShape: {df.shape}\nDistribution:\n{df['Package'].value_counts()}\n"
        )

    def get_df(self):
        train = pd.read_csv(self.path / "train.csv")
        valid = pd.read_csv(self.path / "valid.csv")
        return [train, valid]

    def __init__(self, path: Union[str, Path]):
        self.path = Path(path)
        self.traindf, self.valdf = self.get_df()
        self.x_train, self.y_train = (
            self.traindf["Medical_Description"],
            self.traindf["Package"].tolist(),
        )
        self.x_val, self.y_val = (
            self.valdf["Medical_Description"],
            self.valdf["Package"].tolist(),
        )
        self.y_train_enc = to_categorical(self.y_train)
        self.y_val_enc = to_categorical(self.y_val)

        print(f"\nData instantiated from path: {self.path}\n")
        self.describe_df(self.traindf, "Train Data")
        self.describe_df(self.valdf, "Val Data")

    def train(self, config: AttrDict, model, loss_fn, optimizer):
        self.config = config
        self.model = model
        self.loss_fn = loss_fn
        self.optimizer = optimizer

        train_data_obj = BertDataset(
            config.max_len, config.model_name, config.train_batch_size
        )
        train_dataset = train_data_obj.create(self.x_train.values, self.y_train_enc)

        valid_data_obj = BertDataset(
            config.max_len, config.model_name, config.eval_batch_size
        )
        valid_dataset = valid_data_obj.create(self.x_val.values, self.y_val_enc)

        self.model.compile(
            optimizer=self.optimizer,
            loss=self.loss_fn,
            metrics=["accuracy", matthews_correlation],
        )

        self.model.fit(
            train_dataset, epochs=config.epochs, validation_data=valid_dataset
        )
        return self
