import os
import joblib
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

MODEL_PATH = env_var = os.environ["MODEL_PATH"]
mymodel = LinearRegression()


np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel.fit(train_x.reshape(-1,1), train_y.reshape(-1,1))

#mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
print("Model trained successfully")

pred = mymodel.predict(test_x.reshape(-1,1))

r2 = r2_score(test_y, pred)


print("Model Score:", r2)

joblib.dump(mymodel, MODEL_PATH)
