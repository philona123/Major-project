import streamlit as st

from home_page import show_home_page
from searchjobs_page import show_searchjobs_page
from analysis_page import show_analysis_page
from recommendation_page import show_recommendation_page
from data_set_profile import show_overview
from app import shows_analysis


page = st.sidebar.radio("MENU", ["Home", "Search Jobs", "Job Recommendation", "Analysis Result","Dataset Overview"])

if page == "Home":
    show_home_page()
if page == "Search Jobs":
    show_searchjobs_page()
if page == "Job Recommendation":
    show_recommendation_page()
if page == "Analysis Result":
    shows_analysis()
if page == "Dataset Overview":
    show_overview()

    
