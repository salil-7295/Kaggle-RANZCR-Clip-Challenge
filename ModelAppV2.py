import streamlit as st
from PIL import Image, ImageFont, ImageDraw
from functions import InitializeLoadedModel, PredictForWebApp, Evaluation, AddTextToImage, RocCurve
from functions import COLOR_GREEN, LABELS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MODEL_DICT = {'models/InceptionV3224_best_model.hdf5': 'InceptionV3',
              'models/MobileNet224_best_model.hdf5': 'MobileNet224',
              'models/EfficientNetB3224_best_model.hdf5': 'EfficientNetB3',
              'models/EfficientNetB7224_best_model.hdf5': 'EfficientNetB7'}

# Image Upload and Display from User
st.set_option('deprecation.showfileUploaderEncoding', False)  # Deprecating all Warnings
model_inceptionV3 = InitializeLoadedModel(model_path='models/InceptionV3224_best_model.hdf5',
                                          model_chosen='InceptionV3')
model_mobileNet = InitializeLoadedModel(model_path='models/MobileNet224_best_model.hdf5',
                                        model_chosen='MobileNet')
model_efficientNetB3 = InitializeLoadedModel(model_path='models/EfficientNetB3224_best_model.hdf5',
                                             model_chosen='EfficientNetB3')
model_efficientNetB7 = InitializeLoadedModel(model_path='models/EfficientNetB7224_best_model.hdf5',
                                                 model_chosen='EfficientNetB7')

if __name__ == '__main__':
    st.title("Chest X-ray Image classification")

    st.sidebar.title('Functionalities')
    if st.sidebar.button("ABOUT"):
        image_about1 = Image.open('images/Tube Classsification.jpg')
        image_about2 = Image.open('images/Tube Annotation.jpg')
        st.image(image_about1, caption="Different tubes", use_column_width=True)
        st.image(image_about2, caption="Tube annotation example", use_column_width=True)


    image = st.file_uploader('Upload the Image', type='jpg')  # IMAGE Feature
    preds = pd.DataFrame()
    if image:
        image = Image.open(image)


    if st.sidebar.button("PREDICT"):
        # make the predictions
        preds_inceptionV3 = PredictForWebApp(image, model_inceptionV3, model_name='InceptionV3',rescale=True)
        preds_mobileNet = PredictForWebApp(image, model_mobileNet, model_name='MobileNet', rescale=True)
        preds_efficientNetB3 = PredictForWebApp(image, model_efficientNetB3, model_name='EfficientNetB3', rescale=True)
        preds_efficientNetB7 = PredictForWebApp(image, model_efficientNetB7, model_name='EfficientNetB7', rescale=True)
        preds = pd.concat((preds_inceptionV3, preds_mobileNet, preds_efficientNetB3, preds_efficientNetB7), axis=1)
        # add text to images
        image = AddTextToImage(image, preds, size=100, color=COLOR_GREEN)


    label_curve = st.sidebar.selectbox("Choose the label for ROC curve",
                                       ['','ETT - Normal', 'ETT - Borderline', 'ETT - Abnormal', 'NGT - Abnormal',
                                        'NGT - Borderline', 'NGT - Incompletely Imaged',
                                        'NGT - Normal', 'CVC - Abnormal', 'CVC - Borderline', 'CVC - Normal',
                                        'Swan Ganz Catheter Present']
                                       )
    # model_descriptions = st.sidebar.selectbox("Check the description of the models", list(MODEL_DICT.values()))

    if image:
        st.image(image, use_column_width=True)
    if not preds.empty:
        fig, ax = plt.subplots()
        sns.heatmap(preds, annot=True)
        st.pyplot(fig)

        preds = preds.style.format(
            {'InceptionV3': '{:.2f}', 'MobileNet': '{:.2f}', 'EfficientNetB3': '{:.2f}',
             'EfficientNetB7': '{:.2f}'})
        st.dataframe(preds.applymap(lambda val: "background-color: oldlace" if val <= .20 else "background-color: wheat" if val <= .60 else "background-color:orange"))

    # if model_descriptions == 'InceptionV3':
    #     st.write('the description of InceptionV3')
    # elif model_descriptions == 'MobileNet224':
    #     st.write('the description of MobileNet224')
    # elif model_descriptions == 'EfficientNetB3':
    #     st.write('the description of EfficientNetB3')
    # elif model_descriptions == 'EfficientNetB7':
    #  st.write('the description of EfficientNetB7')

if label_curve:
    st.write('The ROC curve of',label_curve,'on 4 different models')
    fig, ax = RocCurve(test_size=0.1, valid_size= 0.08,random_state=1,
                       model_names=['InceptionV3', 'MobileNet', 'EfficientNetB3', 'EfficientNetB7'],
                       arrays=['predicts/InceptionV3224_best_model.npy', 'predicts/MobileNet224_best_model.npy', 'predicts/EfficientNetB3224_best_model.npy', 'predicts/EfficientNetB7224_best_model.npy'],
                       label_chosen=label_curve)
    st.pyplot(fig)

