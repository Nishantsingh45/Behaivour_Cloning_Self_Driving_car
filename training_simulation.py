## just for not getting error 
print('Setting UP')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from utilis import *
from sklearn.model_selection import train_test_split

path = ''
data = importdatainfo(path)
## step2
data = balanceData(data,display=False)

##step 3
imagePath, steering = loadData(path,data)
#print(imagePath[0], steering[0])

## splitting the data
X_train, X_val, y_train, y_val = train_test_split(imagePath,steering, test_size = 0.2,random_state=5)

## data augmentation
#augmentImage(imagePath, steering)

## batch generator


## model creation
model = createModel()
model.summary()

## model fitting
model.fit(batchGen(X_train,y_train,100,1),steps_per_epoch = 100,epochs=10,
          validation_data=batchGen(X_val,y_val,100,0),validation_steps=200)
model.save('model.h5')
print('Model Saved')

 # plt.plot(history.history['loss'])
 # plt.plot(history.history['val_loss'])
 # plt.legend(['Training', 'Validation'])
 # plt.title('Loss')
 # plt.xlabel('Epoch')
 # plt.show()