from pickletools import uint8
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import io
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf
import subprocess


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


st.text('draw a face or upload a sketch...')
st.text('and tinyMorph will transform your portrait into a photo!!!')
st.sidebar.title('Settings')

# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 0.1)
bg_image = None
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")

)
#radio button for model selection
selected_model = 'FastCUT'
selected_model = st.sidebar.radio('Model', ['FastCUT','pix2pix'])


realtime_update = st.sidebar.checkbox("Update in realtime", True)
st.subheader('upload a sketch here...')
img_file_buffer = st.file_uploader('')
img_was_loaded = False
if img_file_buffer is not None:
    img_was_loaded = True
    image = Image.open(img_file_buffer)
    st.image(image)
    img_array = np.array(image)
    #img_array = np.invert(img_array)


# Create a canvas component
st.subheader('or draw your own portrait here...')
canvas_result = st_canvas(
    fill_color="white",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color="black",
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,

    drawing_mode=drawing_mode,
    height=300,
    key="canvas",
)


# Do something interesting with the image data and paths
img_was_drawn = False
if canvas_result.image_data is not None:
    img_was_drawn = True
    canvas_image = canvas_result.image_data[:,:,-1]
    canvas_image = np.expand_dims(canvas_image, axis=2)
    canvas_image = np.invert(canvas_image)
    h_off = 0
    w_off = 150
    canvas_image = tf.image.crop_to_bounding_box(canvas_image, h_off, w_off, 300, 300)

# generator button to run model
if st.button('generate your face'):
    if img_was_loaded:
        input_image = img_array
        img_was_drawn = False
    if img_was_drawn:
        input_image = canvas_image

#np.zeros(input_image.shape)
#input_image.extend(np.zeros(input_image.shape))
    if selected_model == 'pix2pix':

        input_image = np.concatenate((input_image,np.ones(input_image.shape, dtype=int)*255), axis=1)


# radio button to select model
    if selected_model == 'FastCUT':
        in_path = 'fastCUT/datasets/streamlit_data/testA/img.png'
    else:
        in_path ='pix2pix/datasets/streamlit_data/test/img.png'
    tf.keras.utils.save_img(in_path, input_image)

# selecting correct bash commands
    if selected_model == 'FastCUT':
        bashCommand = "python fastCUT/test.py --dataroot fastCUT/datasets/streamlit_data --name sketch2face --gpu_ids -1 --checkpoints_dir fastCUT/checkpoints --results_dir fastCUT/results"
    else:
        bashCommand = "python pix2pix/test.py --dataroot pix2pix/datasets/streamlit_data --model pix2pix --name sketch2face --gpu_ids -1 --checkpoints_dir pix2pix/checkpoints --results_dir pix2pix/results --dataset_mode aligned"
    process = subprocess.Popen(bashCommand.split(), stdout= subprocess.PIPE)
    output, error = process.communicate()
    #st.markdown(output)

    if selected_model == 'FastCUT':
        output_path = 'fastCUT/results/sketch2face/test_latest/images/fake_B/img.png'
    else:
        output_path = 'pix2pix/results/sketch2face/test_latest/images/img_fake_B.png'
    output_image = tf.keras.utils.load_img(output_path)
    st.image(output_image)
