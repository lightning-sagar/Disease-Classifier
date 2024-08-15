# Disease Prediction using Machine Learning

This project aims to predict diseases based on a given set of symptoms using machine learning techniques. The dataset consists of two CSV files: Train and Test. Each file has 133 columns, where 132 columns represent various symptoms, and the last column represents the prognosis (disease diagnosis).

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Modeling](#modeling)
- [Evaluation](#evaluation)

## Project Overview

In this project, we aim to build a machine learning model that can predict the disease a person may have based on their symptoms. The model will be trained on a dataset where each row corresponds to a patient's symptoms and the diagnosed disease. This can help in early diagnosis and better treatment planning.

## Dataset

- **Train.csv**: This file contains the training data used to train the machine learning model.
- **Test.csv**: This file is used to test the accuracy and performance of the model.

### Features

- **132 Symptom Columns**: Each column represents a symptom that the patient may exhibit (e.g., cough, fever, headache).
- **Prognosis Column**: This column represents the disease diagnosis.

## Data Preprocessing

Data preprocessing is a crucial step in machine learning as it ensures that the data is clean and suitable for model training. Here’s how we approached it:

1. **Cleaning the Data**:  
   - Removed any missing or irrelevant data.
   - Standardized the data format for consistency.

2. **Encoding Categorical Data**:  
   Since machine learning models require numerical input, categorical data (e.g., symptoms described as 'Mild', 'Moderate', 'Severe') was converted into numerical values using label encoding.

   For example, suppose we have a column `Height` in some dataset that has elements as Tall, Medium, and Short. To convert this categorical column into a numerical column, we would apply label encoding to this column. After applying label encoding, the `Height` column is converted into a numerical column with elements 0, 1, and 2, where:
   - Tall -> 0
   - Medium -> 1
   - Short -> 2

   Although this example uses "Height" for illustration, the actual encoding was applied to the symptom data in the project.

## Modeling

After cleaning and preprocessing the data, we trained various machine learning models to find the one that best predicts the disease based on the symptoms. The models considered include:

- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVM)
- Neural Networks

We fine-tuned the models by adjusting hyperparameters and selecting the best-performing model based on validation results.

## Evaluation

The performance of the model is evaluated using the following metrics:

- **Accuracy**: The percentage of correct predictions made by the model.
- **Precision**: The ratio of true positive predictions to the total positive predictions.
- **Recall**: The ratio of true positive predictions to the total actual positives.
- **F1-Score**: The harmonic mean of precision and recall.

---

This covers everything up to the Evaluation section!
