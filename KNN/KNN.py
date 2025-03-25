import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Streamlit App Title
st.title("K-Nearest Neighbors (KNN) Classifier")

# File Upload
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    # Load dataset
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview:")
    st.write(df.head())

    # Extract features and target variable
    X = df.iloc[:, [2, 3]].values  # Selecting 'Age' and 'Estimated Salary'
    y = df.iloc[:, 4].values  # 'Purchased' as target variable

    # Splitting dataset into training (75%) and test (25%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    # Feature Scaling (Standardization)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Sidebar Input for K Value
    k = st.sidebar.slider("Select Number of Neighbors (K)", min_value=1, max_value=15, value=5, step=1)

    # Train KNN classifier
    classifier = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=2)
    classifier.fit(X_train, y_train)

    # Predicting test results
    y_pred = classifier.predict(X_test)

    # Model Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Display Results
    st.write("### Model Performance")
    st.write(f"**Accuracy Score:** {accuracy:.2f}")
    st.write("**Confusion Matrix:**")
    st.write(conf_matrix)
    st.write("**Classification Report:**")
    st.text(report)

    # Visualization (Scatter Plot)
    st.write("### Test Set Predictions")
    fig, ax = plt.subplots(figsize=(8,6))
    scatter = ax.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k', alpha=0.8)
    ax.set_xlabel("Age (Scaled)")
    ax.set_ylabel("Estimated Salary (Scaled)")
    ax.set_title("KNN Classification Results")
    st.pyplot(fig)
