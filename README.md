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
Edit:   31 August 2023
So after spending some time on thinking about making web app I finally made one. And here is its working.

I tried to make a live web app that could classify the tumor easily. I achieved this by using a robust library of Python named Streamlit; I created a personal server on my laptop.
Then adjust the location of my_model according to the PC config.
To run the web app, go to cmd prompt/windows Powershell and move the working directory to the folder in which this folder is located, and write the command 
"Streamlit run main.py"   this will enable a temporary live server over the PC and we can test it from there.

*********************************************************************************************************************************************


This model have 92% validation accuracy and 96% percent train accuracy
