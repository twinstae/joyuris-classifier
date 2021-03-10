import os
from keras.models import load_model
import numpy as np
checkpoint_dir = os.getcwd()+"/model/"
model = load_model(checkpoint_dir+"weight_1.hdf5")

target_x = 224
target_y = 224
CATEGORIES = ["최예나", "조유리", "김채원"]


def predict(img):
    img = img.convert("RGB")
    img = img.resize((target_x, target_y))
    data = np.asarray(img)
    raw_x = np.array(data)
    float_x = raw_x.astype("float") / 256
    x = float_x.reshape(-1, target_x, target_y, 3)
    pred = model.predict(x)
    print(pred)
    result = [np.argmax(value) for value in pred]  # 예측 값중 가장 높은 클래스 반환

    return CATEGORIES[int(result[0])], {
            "최예나": int(pred[0][0] * 100),
            "조유리": int(100 * pred[0][1]),
            "김채원": int(100 * pred[0][2])
        }
