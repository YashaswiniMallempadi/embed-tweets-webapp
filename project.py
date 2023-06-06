import streamlit as st
import streamlit.components.v1 as components
import requests
import time
import webbrowser
from io import StringIO
import pandas as pd

from PIL import Image
st.set_page_config(page_title="embedder", page_icon=":baby_chick:", layout="wide")
#st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center;color:#FF0000;font-size:40px;">{"WOMEN HARRASMENT ”"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h2 style="text-align: center;color:#FF0000;font-size:36px;">{"&        "}</h2>', unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center;color:#FF0000;font-size:40px;">{"CYBER CRIME”"}</h1>', unsafe_allow_html=True)
link = '[gmail](https://mail.google.com/mail/u/0/#inbox?compose=CllgCKCDCHTfVxQfGzTQClmwZJWwrDnGnChCrjXKZWrCFXVMjcxNcsJWdSsFFFhBbmJpWcCPsGV)'
st.markdown(f'<h2 style="text-align: center;color:#FFFFFF;font-size:15px;">{"a streamlit based web app"}</h2>', unsafe_allow_html=True)

# Using object notation
add_selectbox = st.sidebar.selectbox(
    # "How would you like to be contacted?",
    "Contact Details : ",
    
    ("PrateekRajesh","Email : prateekrajesh000@gmail.com ", "phone no : 8639818783")

    
)
# add_selectboxz = st.sidebar.selectbox(
#     # "How would you like to be contacted?",
#     "Contact Details : ",
    
#     ("PrateekRajesh","Email : prateekrajesh000@gmail.com ", "phone no : 8639818783")

    
# )
with st.sidebar:
 add_radio = st.selectbox(
        "contact details: ",
        ("Yashaswini mallempadi", "Email : mallempadi.yashu@gmail.com","phone no : 8555929824")
    )
with st.sidebar:
 st.write("Mail Directly :")
 with st.sidebar:
     link = '[Prateek and yashaswini](https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRtswMzvchtsrrdWpHJrTMhmVzfTLBCZkkQXvDBlZZVWLbJZMcDnkWzVWKllxWlqxHJNLWl)'
 st.markdown(link, unsafe_allow_html=True)
 st.write("register complaints to govt:")
 with st.sidebar:
     link1 = '[cybercrime ](https://cybercrime.gov.in/)'
 
 
     link2 = '[women harrasment](http://ncw.nic.in/front-page-icon/register-complaint)'
 st.markdown(link1, unsafe_allow_html=True)
 st.markdown(link2, unsafe_allow_html=True)
# with st.sidebar:

# Using "with" notation

# st.write("Contact Us :")
# with st.sidebar:
#  add_radio = st.selectbox(
#         "contact details: ",
#         ("prateek rajesh", "yashaswini")
#     )
#st.markdown(f'<h1 style="color:#FF0000;font-size:px;">{"WOMEN HARSAMENT ”"}</h1>', unsafe_allow_html=True)

#    st.write("Contact Us")
#    st.write("mail :")
 
#    st.write("mallempadi.yashu@gmail.com")
#    st.write("prateekrajesh000@gmail.com")

img = Image.open("womanhars.jpg")
st.subheader("Women harrasment")
st.image(img,width=1025)


components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154584/"></script> <!-- end feedwind code -->',height=600)
st.subheader("Child abuse")
img = Image.open("cabuse.jpg")

st.image(img,width=1025)

components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154579/"></script> <!-- end feedwind code -->',height=600)
st.subheader("Cyber Bully")
img = Image.open("Cyberbullying.png")

st.image(img,width=1025)
components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154580/"></script> <!-- end feedwind code -->',height=600)
st.subheader("CyberCrime")
img = Image.open("cyber.jpg")

st.image(img,width=1025)
components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154585/"></script> <!-- end feedwind code -->',height=600)

#uploaded_file = st.file_uploader("share your experiences in .txt formate ")
#if uploaded_file is not None:
     # To read file as bytes:
  #   bytes_data = uploaded_file.getvalue()
 #    st.write(bytes_data)

     # To convert to a string based IO:
 #    stringio = StringIO(uploaded_file.getvalue().decode("utf-16"))
 #    st.write(stringio)

     # To read file as string:
 #    string_data = stringio.read()
     #st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
 #    dataframe = pd.read_csv(uploaded_file)
 #    st.write(dataframe)


# def theTweet(tweet_url):
#     api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
#     response = requests.get(api)
#     res = response.json()["html"]
#     print(res)
#     return f'<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="153967/"></script> <!-- end feedwind code -->'

# input = st.text_input("Enter your tweet url")
# if input:
#     res = theTweet(input)
 
#     components.html(res,height= 700
