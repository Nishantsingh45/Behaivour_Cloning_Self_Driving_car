# Behaivour_Cloning_Self_Driving_car

This project, titled above, has an objective to train a model to drive a car autonomously on a simulated track. The ability of the model to drive the car is learned from cloning the behaviour of a human driver. Training data is gotten from examples of a human driving in the simulator, then fed into a deep learning network which learns the response (steering angle) for every encountered frame in the simulation. In other words, the model is trained to predict an appropriate steering angle for every frame while driving. The model is then validated on a new track to check for generalization of the learned features for performing steering angle prediction.

## Data Collection :
The provided driving simulator had two different tracks. One of them was used for collecting training data, and the other one — never seen by the model — as a substitute for test set.
The driving simulator would save frames from three front-facing "cameras", recording data from the car's point of view; as well as various driving statistics like throttle, speed and steering angle. We are going to use camera data as model input and expect it to predict the steering angle in the [-1, 1] range.
we have used just only centre camera images for more simplicity.

## Image Augmentation
 We have perform image augmentation on the data to make it more suitable for our model.
 We have zoomed, flipped and rotated the images so that model also handles inlinearity in the data.
 
 ## Model
 The model was based on [Nvidia Paper](https://arxiv.org/abs/1604.07316). 
 
 
 
 ![image](https://user-images.githubusercontent.com/68099982/189867949-c3a5c937-cd06-40c7-af13-fdf1db0ea18d.png)
 
 
 
 ## Final Working :
 Overall the car was successfully able to simulate ,although the accuracy was not as good as it could have as we have less training data.
 Working demo can seen [here](https://youtu.be/v02acUNNKBM)
