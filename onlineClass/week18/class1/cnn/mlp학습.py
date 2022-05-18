from statistics import mode
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers, Sequential, Input
import tensorflow as tf
import os
from elice_utils import EliceUtils

elice_utils = EliceUtils()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


SEED = 2021


def load_cifar10_dataset():
    train_X = np.load("./dataset/cifar10_train_X.npy")
    train_y = np.load("./dataset/cifar10_train_y.npy")
    test_X = np.load("./dataset/cifar10_test_X.npy")
    test_y = np.load("./dataset/cifar10_test_y.npy")

    train_X, test_X = train_X / 255.0, test_X / 255.0

    return train_X, train_y, test_X, test_y


def build_mlp_model(img_shape, num_classes=10):
    model = Sequential()

    model.add(Input(shape=img_shape))

    # TODO: [지시사항 1번] 모델을 완성하세요.
    model.add(layers.Flatten())
    model.add(layers.Dense(4096, activation='relu'))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(num_classes, activation='softmax'))

    return model


def plot_history(hist):
    train_loss = hist.history["loss"]
    train_acc = hist.history["accuracy"]
    valid_loss = hist.history["val_loss"]
    valid_acc = hist.history["val_accuracy"]

    fig = plt.figure(figsize=(8, 6))
    plt.plot(train_loss)
    plt.plot(valid_loss)
    plt.title('Loss')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(['Train', 'Valid'], loc='upper right')
    plt.savefig("loss.png")
    elice_utils.send_image("loss.png")

    fig = plt.figure(figsize=(8, 6))
    plt.plot(train_acc)
    plt.plot(valid_acc)
    plt.title('Accuracy')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(['Train', 'Valid'], loc='upper left')
    plt.savefig("accuracy.png")
    elice_utils.send_image("accuracy.png")


def main(model=None, epochs=10):
    tf.random.set_seed(SEED)
    np.random.seed(SEED)

    train_X, train_y, test_X, test_y = load_cifar10_dataset()
    img_shape = train_X[0].shape

    # TODO: [지시사항 2번] Adam optimizer를 설정하세요.
    optimizer = Adam(learning_rate=0.001)

    mlp_model = model
    if model is None:
        mlp_model = build_mlp_model(img_shape)

    # TODO: [지시사항 3번] 모델의 optimizer, 손실 함수, 평가 지표를 설정하세요.
    mlp_model.compile(optimizer=optimizer,
                      loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # TODO: [지시사항 4번] 모델 학습을 위한 hyperparameter를 설정하세요.
    hist = mlp_model.fit(train_X, train_y, epochs=epochs,
                         batch_size=64, validation_split=0.2, shuffle=True, verbose=2)

    plot_history(hist)
    test_loss, test_acc = mlp_model.evaluate(test_X, test_y)
    print("Test Loss: {:.5f}, Test Accuracy: {:.3f}%".format(
        test_loss, test_acc * 100))

    return optimizer, hist


if __name__ == "__main__":
    main()
