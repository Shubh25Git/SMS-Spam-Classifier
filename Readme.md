# 📩 SMS Spam Classifier

A machine learning project to analyze SMS messages and explore the differences between **Spam** and **Ham (Not Spam)** messages using Python and data analysis techniques.

## 🎯 Project Objective

The objective of this project is to explore an SMS dataset, understand its structure, and identify patterns that may help distinguish spam messages from legitimate messages.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Jupyter Notebook

## 📂 Current Progress

### 1. Data Loading and Cleaning
- Loaded the SMS dataset using Pandas.
- Removed unnecessary columns.
- Renamed important columns for better readability.
- Encoded the target labels.
- Removed duplicate messages.

### 2. Exploratory Data Analysis (EDA)
- Analyzed the distribution of spam and ham messages.
- Created a pie chart to visualize the percentage of spam and ham messages.

### 3. Text Feature Extraction
- Used NLTK to extract the number of characters, words, and sentences from each SMS message.

### 4. Message Length Analysis
- Created histograms to compare spam and ham messages based on the number of characters and words.
- Started investigating the relationship between message length and spam classification.

## 🚧 Future Work

- Complete the analysis of character, word, and sentence counts.
- Explore additional text patterns and visualizations.
- Apply text preprocessing techniques.
- Convert SMS text into numerical features using techniques such as Bag of Words or TF-IDF.
- Train and evaluate machine learning classification models.
- Compare model performance using suitable evaluation metrics.
- Develop a simple interface to classify new SMS messages.

## 📌 Project Status

**Currently in progress** — data cleaning, initial exploratory data analysis, and basic text feature extraction.

More features, analysis, and machine learning models will be added as the project develops.

---

*Built with Python as part of my Machine Learning learning journey.*