import streamlit as st
import streamlit.components.v1 as stc 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("TkAgg")
import seaborn as sns
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
import numpy as np
import nltk

df_jobs = pd.read_csv("naukri.csv")


