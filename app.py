nltk.download('punkt_tab')
nltk.download('stopwords')

import streamlit as st
import pickle
import string 
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# 1. Page Configuration
st.set_page_config(page_title="Spam Classifier", page_icon="🛡️", layout="centered")

# --- Custom CSS for Advanced Styling ---
st.markdown("""
<style>
    /* Gradient text for the main title */
    .title-text {
        font-size: 45px;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    /* Subtitle styling */
    .subtitle-text {
        font-size: 20px;
        color: #6c757d;
        margin-bottom: 20px;
    }
    /* Hide Streamlit default menu and footer for a cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

ps = PorterStemmer()

# 2. Text Preprocessing Function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)

# 3. Model Loading with Caching
@st.cache_resource
def load_models():
    # Make sure your paths are correct
    tfidf = pickle.load(open('Models/vectorizer.pkl', 'rb'))
    mnb = pickle.load(open('Models/model.pkl', 'rb'))
    return tfidf, mnb

tfidf, mnb = load_models()

# 4. Beautiful Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2855/2855013.png", width=120)
    st.markdown("## 🛡️ Secure Inbox")
    st.markdown("""
    Welcome to the **Spam Classifier!** 
    
    This tool uses advanced **Natural Language Processing (NLP)** and **Machine Learning** to detect malicious, promotional, or unwanted messages.
    """)
    st.markdown("---")
    st.markdown("### ⚙️ How it works:")
    st.markdown("1. **Tokenization:** Breaks down your sentence.")
    st.markdown("2. **Filtering:** Removes stop words & punctuation.")
    st.markdown("3. **Stemming:** Reduces words to root form.")
    st.markdown("4. **Vectorization:** Converts text to numbers (TF-IDF).")
    st.markdown("5. **Prediction:** Naive Bayes model decides!")
    st.markdown("---")
    st.caption("Made with ❤️ using Python & Streamlit")

# 5. Main App UI
# Custom Title using HTML/CSS defined above
st.markdown('<p class="title-text">Email & SMS Spam Classifier</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Keep your inbox safe from phishing and spam 🚀</p>', unsafe_allow_html=True)

# Main Container for Input
with st.container():
    input_message = st.text_area(
        "Enter your message below:", 
        height=180, 
        placeholder="e.g., Congratulations! You've won a $1000 Walmart gift card. Click here to claim now..."
    )
    
    # Optional: Show character count in a neat column
    col1, col2 = st.columns([4, 1])
    with col2:
        st.caption(f"Characters: {len(input_message)}")

# 6. Predict Button & Logic
if st.button('🔍 Analyze Message', type="primary", use_container_width=True):
    
    if not input_message.strip():
        st.warning("⚠️ Please enter some text before analyzing.")
    else:
        with st.spinner("🧠 AI is analyzing your message..."):
            
            # Processing
            transformed_message = transform_text(input_message)
            vectorized_input = tfidf.transform([transformed_message])
            result = mnb.predict(vectorized_input)[0]
            
            st.markdown("---")
            
            # 7. Engaging Result Output
            if result == 1:
                st.error("🚨 **THREAT DETECTED!**")
                st.markdown("### This message is classified as **SPAM**.")
                st.info("💡 **Tip:** Do not click on any links or share personal information if you receive this message.")
            else:
                st.balloons() # Fun animation for safe messages
                st.success("✅ **ALL CLEAR!**")
                st.markdown("### This message looks **SAFE** (Not Spam).")
            
            # 8. "Nerd Stats" Expander (Makes the app look highly professional)
            with st.expander("🛠️ View Analysis Details"):
                st.write("**Original Word Count:**", len(input_message.split()))
                st.write("**Processed Text (Root Words):**")
                st.code(transformed_message, language="text")
                st.write("*Note: The model analyzes this stripped-down version of your text to find spam patterns.*")