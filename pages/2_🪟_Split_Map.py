import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.sidebar.title("Agri_Performance")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)



st.title("Split-panel Map")



with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[45.224461, -0.773946], zoom=14)
        m.split_map(
            left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        )
        m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)
