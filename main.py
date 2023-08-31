import streamlit as st
from PIL import Image
import h5py
import tensorflow as tf
import numpy as np
import cv2



file = "C:\\Users\\ABHAS\\Downloads\\my_model.h5"
model = h5py.File(file,'r')
from keras.models import load_model
model = load_model(model)
st.title("This is a demostration of Classification of Normal Human brain and tumor affected human brain")

img = Image.open("C:\\Users\\ABHAS\\Downloads\\OIP.jpg")
# st.header("The image should be like")
st.image(img,caption="The image should be like this")


upload = st.file_uploader("Upload your file one at a time only")

if upload is not None:
    up = Image.open(upload)
    st.image(up,caption="Uploaded Image")

if st.button("Predict"):
    # im = cv2.imread(upload)
    im = Image.open(upload).convert('RGB') 
    open_cv_image = np.array(im) 
# Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    
    # im = Image.open(upload)
    # # im = cv2.imread(upload)
    # im1 = im.save()
    resize = tf.image.resize(open_cv_image,(256,256))
    yhat = model.predict(np.expand_dims(resize/255,0))
    if yhat < 0.5:
        st.header("No tumour present")
    else:
        st.header("Tumour Present")




#resizing
# resize = tf.image.resize()
#predicting

