# X-ray-tube-classification-Webapp

### What is this Web App?

This is a Chest X-ray Catheter tube position classifier. When given a X-ray image, it predicts whether chest tubes are correctly positioned.
To be more specific, it provides probabilistic classification of chest tube positions using Machine Learning.

### The application provides classification for the following 11 labels:

ETT - Normal, ETT - Borderline, ETT - Abnormal, NGT - Abnormal
NGT - Borderline, NGT - Incompletely Image, NGT - Normal
CVC - Abnormal, CVC - Borderlin, CVC - Normal, Swan Ganz Catheter Present

![TUBE](https://github.com/salil-7295/Kaggle-RANZCR-Clip-Challenge/blob/main/Catheter%20Tube%20_Classes.jpg)

### Application UI

The app is built using Streamlit! A python tool to easily Deploy ML Models. 

![UI-FRONT](https://github.com/salil-7295/Kaggle-RANZCR-Clip-Challenge/blob/main/UI_Front.png) 

The functioning is as follows: 

_Upload an X-ray image from local system by clicking "Broswer files".

_Read the basic information from "ABOUT".

_Make the predictions using "PREDICT" and we can see the classification results (Confidence Scores for each class).When you click the "PREIDICT", it will run the predictions on 4 different models on the backend, for each model, it will return the probability of being True for all the 11 labels. The final prediction will be based on the average performance of 4 models

![Result](https://github.com/salil-7295/Kaggle-RANZCR-Clip-Challenge/blob/main/Predictions.png)

Notice the probabilities of 11 labels don't add up to 1. Because each label is predicted independently as 0 or 1.

### How it is done
The models are trained with CNNs using transfer learning.

### What about the data
The data comes from Kaggle: https://www.kaggle.com/c/ranzcr-clip-catheter-line-classification

Total dataset of 40,000 images, 12.23GB

Here you can only find the codes.The models have not been uploaded. 


