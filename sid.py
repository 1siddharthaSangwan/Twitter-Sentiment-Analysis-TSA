import streamlit as st
from value import *
from graphical import *
from fetch import *
import datetime

from PIL import Image
import corpora
#Page Config
#st.set_page_config(page_title="ITSA")
st.title("TSA")
st.markdown("# Twitter Sentiment Analysis")
st.markdown("")
st.sidebar.markdown("# Navigation Pane")
show_page = st.sidebar.selectbox(label="Choose page", options=["Welcome", "Type Word/Sentence", "Fetch From Twitter"])



if show_page=="Welcome":
    '''
        ##### Welcome, TSA is a web applicaion is aimed for Twitter Sentimental Analysis
    '''
    #image = Image.open('Photos/photo-1523961131990-5ea7c61b2107.jpeg')
    #st.image(image)
    
    '''
        ---
    

        - ###### Polarity  
            - -1 being negative and
            - +1 being positive
        - ###### Subjectivity 
            - 0 being completely objective 
            - 1 being completely subjective 
        ---
    '''

elif show_page=="Type Word/Sentence":

    #image = Image.open("Photos/photo-1529236183275-4fdcf2bc987e.jpeg")
    #st.image(image)

    st.markdown("### Evaluate Your Text")

    txt = st.text_area(label="Enter text")
    corrspell = st.checkbox(label="Use spelling corrector")
    evaluate = st.button(label="Compute Sentiment")

    #main
    if evaluate and txt!="":
        
        with st.spinner("Computing Sentiment"):
            
            po,su = sentiment(txt, corrspell)
            #col1, col2 = st.columns([1, 1])

           # with col1:
            st.write("Polarity : ")
            st.write(po)
                
            #with col2:
            st.write("Subjectivity")
            st.write(su)
            
            chart(po, su)

else:

    #image = Image.open('Photos/sdfsf.png')
    #st.image(image)

    st.markdown("### Evaluate Twitter Fetched Data")
    txt = st.text_area(label="Enter what you want to search")
    tweetCount = st.slider(label="Choose no of tweets to fetch", min_value=1, value=10, max_value=100)
    
    
    #Date Picker
    #col1, col2 = st.columns([1, 1])
    #with col1:
    begin=st.date_input(label="Starting Date", value=datetime.date.today()-datetime.timedelta(days=1), min_value=datetime.date.today()-datetime.timedelta(days=100), max_value=datetime.date.today()-datetime.timedelta(days=1))
    
    #with col2:
    finish=st.date_input(label="Finishing Date", value=datetime.date.today(), min_value=datetime.date.today()-datetime.timedelta(days=90), max_value=datetime.date.today())
    
    #Ensure starting date before finishing date
    if finish<=begin:
        st.error("Error \nStarting date must be < Finishing Date") 
        #st.stop()
    get_tweet = st.button(label="Scrape and Analyze tweets")
    
    if get_tweet:

        if txt=="":
            st.error("Error \nEmpty search string")
            #st.stop()
    
        with st.spinner("Loading"):
            

            data, data_clean = scrape_tweets(txt, tweetCount, begin, finish)
            
            if len(data)==0:
                st.error("No data")
                #st.stop()

            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.markdown("## Result")
            st.markdown("---")
            
            tweetSentiment(data_clean)

           # with st.expander("Show scraped Twitter tweets"):
                                
            st.markdown("#### Raw")
            st.write(data)
                
            st.markdown("#### Processed")
            st.write(data_clean)
#st.write("Developed by *Sangwan*, **PCS 2210 TEAM** KIET Group of Institutions")


