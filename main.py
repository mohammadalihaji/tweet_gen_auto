#backend
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import os
os.environ['GOOGLE_API_KEY']="AIzaSyBz584xVGKvl6bzl4eA7Lv0CgoGX9Oy8Wk"

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model



#frontend

import streamlit as st

st.header("Tweet Generator")
st.subheader("Generate a tweet using Generative AI")

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1, max_value=1000, value=1, step=1)

if st.button("Generate"):
    tweet = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweet.content)

