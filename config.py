from attrdict import AttrDict  # type: ignore

configs_local = {
    "random_state": 42,
    "max_len": 64,
    "train_batch_size": 32,
    "eval_batch_size": 8,
    "epochs": 3,
    "lr": 3e-5,
    "model_name": "bert-base-uncased",
    "datapath": "data/processed/",
}

configs_local = AttrDict(configs_local)
