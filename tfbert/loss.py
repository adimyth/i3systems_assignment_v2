from tensorflow.keras.losses import CategoricalCrossentropy  # type: ignore

categorical_cross_entropy = CategoricalCrossentropy()


def cce(targets, logits):
    return categorical_cross_entropy(targets, logits)
