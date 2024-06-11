import streamlit as st
st.title("启动原神吗")
st.header("You need to play Genshin immediately")
st.subheader("eg, Visual Studio Code")
st.text("It's not that hard")

st.markdown("this is an image: \n \
            ![](https://img.yanlutong.com/uploadimg/ico/2022/1213/1670899773617316.jpg)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("这个阿贝多真帅:" ,
                  ('对',
                   '太对了'))
if status == '对':
    st.success("有品")
else:
    st.success("太有品了")

hobbies = st.multiselect("Hobbies:",
               ['达达利亚',
                '钟离',
                '阿贝多',
                '提纳里'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    
