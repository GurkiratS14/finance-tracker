import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Simple Finance App",page_icon="💰",layout="wide")

def load_transcations(file):
    pass


def main():
    st.title("Simple Finance Dashboard")
    uploaded_file=st.file_uploader("Upload your transcation CSV file", type=["csv"])

    if uploaded_file is not None:
        df=load_transcations(uploaded_file)