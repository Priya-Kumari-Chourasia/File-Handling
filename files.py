import streamlit as st
import pandas as pd

st.subheader('Loading the CSV File')

df = st.file_uploader("Upload the CSV file : ",type =['csv','xlsx'])

#if df is not None:
#    st.dataframe(df)

df = pd.read_csv("Products.csv")

st.table(df.head())

st.subheader('Dealing with images')
st.image("img.jpg")

img_file = st.file_uploader("Upload the Image file : ",type = ['png','jpeg'])
if img_file is not None:
    st.image(img_file)


st.subheader('Working with Videos')
video_file = st.file_uploader("Upload the Video file : ",type = ['mkv','mp4'])
if video_file is not None:
    st.video(video_file,start_time=0)


st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload the Audio file : ",type = ['wav','mp3'])
if audio_file is not None:
    st.audio(audio_file,start_time=0)
