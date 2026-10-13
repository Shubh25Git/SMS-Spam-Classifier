📩 SMS Spam Classifier

A machine learning project to analyze SMS messages and explore the differences between Spam and Ham (Not Spam) messages using Python and data analysis techniques.

🎯 Project Objective

The objective of this project is to explore an SMS dataset, understand its structure, and identify patterns that may help distinguish spam messages from legitimate messages.

🛠️ Technologies & Tools Used

Core Stack:

🐍 Python

🐼 Pandas

🔢 NumPy

📓 Jupyter Notebook

Visualization:

📊 Matplotlib

📈 Seaborn

☁️ WordCloud

Natural Language Processing (NLP):

🗣️ NLTK (Natural Language Toolkit)

🔡 Python string module

🚀 Project Pipeline

1️⃣ Data Loading and Cleaning

Loaded the SMS dataset using Pandas.

Removed unnecessary columns to streamline the data.

Renamed important columns for better readability.

Encoded the target labels (Spam/Ham) into numerical formats.

Removed duplicate messages to ensure model accuracy.

2️⃣ Exploratory Data Analysis (EDA)

Analyzed the distribution of spam and ham messages.

Visualized the dataset balance by creating a pie chart to show the exact percentage of spam vs. ham messages.

3️⃣ Text Preprocessing Pipeline

This phase is crucial for cleaning the raw SMS text data and converting it into a standardized format suitable for machine learning models.

Every message in the dataset passes through a custom preprocessing function (transform_text) that performs the following sequence of operations:

🔤 Lowercase Conversion:
Converts all characters in the text to lowercase to ensure consistency (e.g., "Hello" and "hello" are treated as the exact same word).

✂️ Tokenization:
Splits the sentences into individual words or tokens using NLTK's word_tokenize.

🚫 Removing Special Characters:
Iterates through the tokens and keeps only alphanumeric characters, cleanly filtering out special symbols and emojis.

🛑 Removing Stop Words and Punctuation:
Removes common English stop words (like "is", "the", "and") and standard punctuation marks. These generally do not contribute predictive value for spam classification and only add noise.

🌱 Stemming:
Applies the NLTK PorterStemmer to reduce words to their root or base form (e.g., "dancing", "dances", and "danced" all become "danc"). This dramatically reduces the overall vocabulary size.

Built with Python as part of my Machine Learning learning journey.