import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def show_home_page():
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    
    image= Image.open('logo.png')
    st.image(image)
    

    lottie_animation_1 = "https://assets1.lottiefiles.com/packages/lf20_lgk0wqey.json"
    lottie_anime_json = load_lottie_url(lottie_animation_1)


    col1, col2 = st.columns(2)
        

    with col1:
       
        st.write("Jobzy is an exclusive Job recommendation system which comes along with an Analyzer to give you job analysis results on various metrics in graphical format. This website allows you to search for jobs, and get industry recommendations based on skills and industry preference. The following features are available on this web application,")
        st.write(
            """    
            - Search Jobs
- Industry Recommendation
-  Analysis Result
- Datasetet Overwiew
            """
            )
        st.write("Please choose your desired version from the side menu and enjoy using the Web application..")
    with col2:
    
        st_lottie(lottie_anime_json, key = "hi")
        
st.markdown(
  """
  <style>
element.style {
    width: 30px;
    height: 30px;
    transform: translate3d(0px, 0px, 0px);
    content-visibility: visible;
}
</style>
""",
unsafe_allow_html=True
)
