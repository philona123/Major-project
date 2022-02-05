import streamlit as st

def show_searchjobs_page():
    st.subheader("Search Jobs")

    City = (
        
    )
    
    Industry = (
        
    )

    Experience = (
        
    )

    City = st.selectbox("City", City)
    Industry = st.selectbox("Industry", Industry)
    Experience = st.selectbox("Experience", Experience)
    vaccancies = st.slider("Vaccancies", 0, 50, 3)


