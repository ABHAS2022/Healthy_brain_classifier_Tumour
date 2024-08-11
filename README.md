# Brain Tumor Classification

This repository provides a complete pipeline for classifying brain tumors using MRI scans. The project includes a Jupyter Notebook for model training and evaluation, as well as a Streamlit web app for live predictions.

## Project Overview

### Jupyter Notebook

1. **Training and Evaluation**: The notebook demonstrates the steps to train a brain tumor classification model using the Brain Tumor Classification dataset from Kaggle.
2. **Saved Model**: The trained TensorFlow model is saved in `.h5` format for easy deployment.

### How to Use

1. **Install Dependencies**:
   - Install the required libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Download and Set Up**:
   - Clone or download the repository to your local device.
   - Open the `run.ipynb` file in Jupyter Notebook.

3. **Configuration**:
   - Set the path to the saved model in the `.ipynb` file.
   - Update the path of the MRI scan image in the `cv2.imread()` function:
     ```python
     img = cv2.imread('/path/to/image.jpg')  # Use double backslashes "\\" for personal machines
     plt.imshow(img)
     ```

4. **Execution**:
   - Run all cells in order to process the MRI scan and obtain the classification result.

### Streamlit Web App

To make the model accessible via a web interface:

1. **Setup**:
   - Ensure that the required libraries are installed (same as above).
   - Adjust the path to the saved model in `main.py`.

2. **Run the Web App**:
   - Open Command Prompt or Windows PowerShell.
   - Navigate to the project directory.
   - Start the Streamlit app with:
     ```bash
     streamlit run main.py
     ```
   - This command will start a local server, and you can interact with the app through your web browser.

### Model Performance

- **Validation Accuracy**: 92%
- **Training Accuracy**: 96%
