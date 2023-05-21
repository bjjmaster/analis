import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt


kf = tf.keras
net = tf.keras.layers
num_words = 10000
max_review_len = 100



def CNN(x, y): # mx - это длиннаа сообщения
    print("CNN")
    model_cnn = kf.Sequential()
    model_cnn.add(net.Embedding(num_words, 64, input_length=max_review_len))
    model_cnn.add(net.Conv1D(250, 5, padding="valid", activation="relu"))
    model_cnn.add(net.Dense(128, activation="relu"))
    model_cnn.add(net.Dense(1, activation="softmax"))

    model_cnn.compile(optimizer="adam",
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
    model_cnn_fit = model_cnn.fit(x,y, epochs=9, batch_size=128, validation_split=0.3)

    print()

    plt.plot(model_cnn_fit.history['accuracy'],
             label='Доля верных ответов на обучающем наборе')
    plt.plot(model_cnn_fit.history['val_accuracy'],
             label='Доля верных ответов на проверочном наборе')
    plt.xlabel('Эпоха обучения CNN')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()

    return model_cnn_fit

def LSTM(x, y):
    print("LSTM")
    model_LSTM = kf.Sequential()
    model_LSTM.add(net.Embedding(num_words, 64, input_length=max_review_len))
    model_LSTM.add(net.LSTM(128))
    model_LSTM.add(net.Dense(1, activation="sigmoid"))

    model_LSTM.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])


    history = model_LSTM.fit(x,
                        y,
                        epochs=9,
                        batch_size=128,
                        validation_split=0.3)

    print()
    plt.plot(history.history['accuracy'],
             label='Доля верных ответов на обучающем наборе')
    plt.plot(history.history['val_accuracy'],
             label='Доля верных ответов на проверочном наборе')
    plt.xlabel('Эпоха обучения LSTM')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()

    return history

def GRU(x, y):
    print("GRU")
    model_GRU = kf.Sequential()
    model_GRU.add(net.Embedding(num_words, 64, input_length=max_review_len))
    model_GRU.add(net.GRU(128))
    model_GRU.add(net.Dense(1, activation="sigmoid"))

    model_GRU.compile(optimizer='adam',
                       loss='binary_crossentropy',
                       metrics=['accuracy'])

    history = model_GRU.fit(x,
                             y,
                             epochs=9,
                             batch_size=128,
                             validation_split=0.3)

    print()

    plt.plot(history.history['accuracy'],
             label='Доля верных ответов на обучающем наборе')
    plt.plot(history.history['val_accuracy'],
             label='Доля верных ответов на проверочном наборе')
    plt.xlabel('Эпоха обучения')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()

    return history

columns = ["target", "features"]
authentication_data = pd.read_csv("authentication.csv",  encoding='utf-8', sep=";",names=columns)
tokenize =  tf.keras.preprocessing.text.Tokenizer(num_words=num_words)# токинезатор для текста
tokenize.fit_on_texts(authentication_data["features"]) # без лемматизации
sequences = tokenize.texts_to_sequences(authentication_data["features"])# тут предлодения в числаах



x_train = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_review_len)# тут сразу происходит дополеннение нулями
y_train = authentication_data["target"]


LSTM(x_train, y_train)
CNN(x_train, y_train)
GRU(x_train, y_train)




