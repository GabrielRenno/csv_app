import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


OPENAI_API_KEY = "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"

# Set the title of the app
st.title("Dataset Exploration App")

llm = OpenAI(api_token=OPENAI_API_KEY, temperature=0.0)

pandas_ai = PandasAI(llm=llm)
def main():

   

    # Create a side bar
    st.sidebar.title("About")
    st.sidebar.info(
        "This app is a demo of the PandasAI library. It uses the OpenAI API to answer questions about your dataset."
    )
    st.sidebar.title("CSV File Reader")
    st.sidebar.write("Upload a CSV file and choose the separator.")
    

    # File upload
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")


    if uploaded_file is not None:

            # Separator selection
        separator = st.sidebar.selectbox("Select the separator", [",", ";", "\t"])
        
        # Read the CSV file
        try:
            df = pd.read_csv(uploaded_file, sep=separator)
            st.write("Head of the dataset:")
            st.write(df.head())
            # Space for the user to input a question
            st.header("Ask a question about your dataset")
            st.write(
                "You can ask any question about your dataset. For example: What is the name of the first column?"
            )
            st.sidebar.write("## What is this dataset about?")
            st.sidebar.write(pandas_ai.run(df, prompt="Give me a summary of this dataset."))

            # Promt is equal to the inputed question
            prompt = st.text_input("Question", "What is the name of the first column?")


            answer = pandas_ai.run(df, prompt=prompt)

            #Display the text answer
            st.write(answer)
    
            plt.plot()
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Your customized plot")

    
            plt.gcf().autofmt_xdate()
            st.pyplot(plt)

        except Exception as e:
            st.write("Error reading the CSV file:", str(e))

    

if __name__ == "__main__":
    main()