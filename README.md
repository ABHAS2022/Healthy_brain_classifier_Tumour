# Healthy_brain_classifier_Tumour

This is a jupyter notebook made on google colab showing the steps in it to determine whether a mri scan has brain tumour or not

It is trained using the brain tummour classification dataset present on Kaggle
so it shows the complete process and another one file attached is the tensorflow model that i have saved from this jupyter notebook in .h5 format

To run this model kindly do install the libraries present in requirements.txt

1)
OR go to command Prompt do  " pip install requirement.txt"
2)
now download/clone the whole repository in your device 
3)
Open run.ipynb present
4) 
Now give the path of the downloaded model in .ipynb file
5) 
Now give the path image of the mri scan in the bracket of cv2.imread().  (inside the apostrophy) (if using personal machine do use double backslash "\"
between the branches)
"
img = cv2.imread('/content/OIP.jpg')
plt.imshow(img)

"
6)
Now run all the cells orderwise as set in the run.ipynb
7)
The Last cell will give you result




*********************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------------
*********************************************************************************************************************************************


This model have 92% validation accuracy and 96% percent train accuracy
