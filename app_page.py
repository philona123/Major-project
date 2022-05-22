import streamlit as st

#----config function--------#
st.set_page_config(layout="wide", page_title='JOBZY', page_icon="logo.png")

#------------------------#

from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie


from home_page import show_home_page
from searchjobs_page import show_searchjobs_page
from analysis_page import show_analysis_page
from recommendation_page import show_recommendation_page
from data_set_profile import show_overview
from app import shows_analysis


#------------------sidebar menu------------------#
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Search Jobs", "Industry Recommendation", 'Analysis Result', "Dataset Overview"], 
        icons=['house', 'search', 'list-task', 'cloud-upload', 'gear'], menu_icon="cast", default_index=0)
    selected


st.markdown(
  """
  <style>
  .css-12oz5g7 {
    flex: 1 1 0%;
    width: 100%;
    padding: 1rem 1rem 10rem;`
    max-width: 46rem;
}
.css-18e3th9 {
    padding-left: 5rem;
    padding-right: 5rem;
}
b, strong {
    font-weight: 600;
     color: #28bdb5;
     font-size: 30px;
}

li {
    display: list-item;
    text-align: -webkit-match-parent;
    color: #28bdb5;
    font-weight: 600;


}
p, ol, ul, dl {
    margin: 0px 0px 1rem;
    padding: 0px;
    font-size: 18px;
    font-weight: 400;
}
em {
    font-style: italic;
    color: #28bdb5;
}

</style>
""",
unsafe_allow_html=True
)


#----------minimalize default features--------#
#hide_menu_style="""
#<style>
##MainMenu{visibility:hidden;}
#footer{visibility:hidden;}
#</style>
#"""
#st.markdown(hide_menu_style, unsafe_allow_html=True)


if selected == "Home":
    show_home_page()
if selected == "Search Jobs":
    show_searchjobs_page()
if selected == "Industry Recommendation":
    show_recommendation_page()
if selected == "Analysis Result":
    shows_analysis()
if selected == "Dataset Overview":
    show_overview()



