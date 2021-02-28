from tensorflow.keras.optimizers import Adam  # type: ignore

from config import configs_local  # type: ignore
from tfbert.loss import cce  # type: ignore
from tfbert.medical_data import MedicalData  # type: ignore
from tfbert.models import BaseModel  # type: ignore

exp = MedicalData(configs_local.datapath)
exp.train(
    configs_local,
    BaseModel(configs_local.model_name),
    cce,
    Adam(learning_rate=configs_local.lr),
)
