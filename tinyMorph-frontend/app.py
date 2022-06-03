import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import io


# editing the tab header on browser
st.set_page_config(
page_title = "tinyMorph",
page_icon = ":pencil:",
)
# editing the html code
hide_streamlit_style = """
                       <style>
                       #MainMenu {visibility: hidden;}
                       .css-1d391kg {padding-top:30px}
                       .css-12oz5g7 {padding-top:10px}
                       .css-12oz5g7 {padding-left: 33px}
                       .css-12oz5g7 {padding-right: 85px}

                       footer {visibility: hidden;}
                       </style>
                       """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title('tinyMorph')


st.text('draw anything you like...')
st.text('and tinyMorph will transform your drawing into a photo!!!')

st.sidebar.title('Settings')
# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
#stroke_color = st.sidebar.beta_color_picker("Stroke color hex: ")
#bg_color = st.sidebar.beta_color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")

)

realtime_update = st.sidebar.checkbox("Update in realtime", True)




# Create a canvas component
canvas_result = st_canvas(
    fill_color="black",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    #stroke_color=stroke_color,
    #background_color="" if bg_image else bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,

    drawing_mode=drawing_mode,
    height=300,
    key="canvas",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
   st.image(canvas_result.image_data, width=600, caption='your image will morph here')
if canvas_result.json_data is not None:
            objects = pd.json_normalize(canvas_result.json_data["objects"])
            for col in objects.select_dtypes(include=['object']).columns:
                objects[col] = objects[col].astype("str")
            st.dataframe(objects)

st.markdown(canvas_result.image_data)
st.markdown(canvas_result.image_data.shape)
st.markdown(canvas_result.image_data.ndim)
im = Image.fromarray(canvas_result.image_data)
st.markdown(type(im))
