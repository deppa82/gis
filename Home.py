import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.sidebar.title("Agri_tech")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)



st.title("Thinking about Possibility")
st.markdown(
    """
    This multipage app demonstrate the potential of today technology
    """
)



st.header("Welcome")




m = leafmap.Map(center=[45.2248192, 0.7732142], zoom=4,minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
