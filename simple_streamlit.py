import streamlit as st
import time
import matplotlib.pyplot as plt
# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
import pandas as pd
# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
import numpy as  np 
import altair as alt
import graphviz
import graphviz as graphviz
from PIL import Image
import io



st.snow()
st.markdown("<h1 style='color:blue;'>This is a blue heading</h1>", unsafe_allow_html=True)
st.write("🌟 Welcome to my Streamlit app! 🌟")
st.markdown(
    """
    # Heading
    ## Subheading
    **Bold Text**
    *Italic Text*
    ```
    Code Block
    ```
    - List Item
    """
)
st.title('HELLO................................')
st.subheader('wait until execution....................!')
with st.spinner('wait for it......'):
    time.sleep(3)
st.header("Hello World")
st.subheader("hiii.....!    prithvi")
st.code("print('prithvi')")
st.subheader("image")
st.image("IMG_20220626_095208.jpg")
st.caption("my image")
st.subheader("video")
st.video("Recording 2024-07-01 200441.mp4")
st.caption("recording video")
# st.audio("")
st.sidebar.subheader("Is This Your Lap")
st.sidebar.checkbox("yes")
st.sidebar.checkbox("no")
st.sidebar.radio('pick your gender',['male','female','transgender'])
st.sidebar.selectbox('pickup the gender',['male','female'])
st.sidebar.multiselect('select your area',['chennai','theni','selam','covai','trichy'])
st.sidebar.slider('pick',0,10)
st.sidebar.select_slider('pick a rating',['bad','good','excellent'])
st.sidebar.selectbox('pick',['bad','good','excellent'])
st.sidebar.balloons()
st.sidebar.subheader('progress bar')
st.sidebar.progress(50)
# To change the color of the background
# Define the color you want as the "background"
background_color = "#f0f0f0"  # Replace with your desired background color

# Use st.empty() to create a space for the background color
background_placeholder = st.empty()

# Use markdown to create a colored block
background_placeholder.markdown(
    f"""
    <div style="background-color: {background_color}; width: 100%; height: 100vh;">
        <!-- This div is for the background color -->
    </div>
    """,
    unsafe_allow_html=True
)

# Use st.container() to overlay content
with st.container():
    st.title('My Streamlit App')
    st.write('This is a sample Streamlit app with a simulated background color.')
    st.write("Here's some content on top of the background.")

# ///////////////////////////////////////////////////////////////////////////////////////    

st.sidebar.title('click it please............')     
st.sidebar.button('click it')

container=st.sidebar.container()
container.write('write inside the container')
st.sidebar.write('write outside the container')

st.success('Got it man...............!')
st.warning("No ,better you don't do it.......!")
st.error('oops....?')
st.info("it's easy to learn")
st.exception(RuntimeError('Runtime error eception'))

rand=np.random.normal(1, 2, size=40)
# This function creates a new figure (fig) 
# 'ax' represents a single subplot within that figure.
# 'fig' is an intance of matplotlib.figure.Figure.
# 'ax' is an instance of matplotlib.axes.Axes.
fig, ax = plt.subplots()
# This creates a histogram of the data in the rand array.
# rand: This is the data to be plotted.
# bins=15: This specifies the number of bins (intervals) to use for the histogram.
# In this case, the data will be divided into 15 bins.
ax.hist(rand, bins=15)
# st.pyplot(fig): This function call is part of Streamlit.
# It renders and displays the Matplotlib figure (fig) within a Streamlit application.
st.pyplot(fig)

df= pd.DataFrame(    
    np.random.randn(15, 2),    
    columns=['x', 'y'])
st.line_chart(df)

df= pd.DataFrame(    
    np.random.randn(15, 2),    
    columns=['x', 'y'])
st.bar_chart(df)

df= pd.DataFrame(    
    np.random.randn(15, 2),    
    columns=['x', 'y'])
st.area_chart(df)

dp = pd.DataFrame(   
    np.random.randn(50, 3),   
    columns=['x','y','z'])

c = alt.Chart(dp).mark_circle().encode(   
     x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])

st.altair_chart(c, use_container_width=True)


# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge("run", "intr")
graph.edge("intr", "runbl")
graph.edge("runbl", "run")
graph.edge("run", "kernel")
graph.edge("kernel", "zombie")
graph.edge("kernel", "sleep")
graph.edge("kernel", "runmem")
graph.edge("sleep", "swap")
graph.edge("swap", "runswap")
graph.edge("runswap", "new")
graph.edge("runswap", "runmem")
graph.edge("new", "runmem")
graph.edge("sleep", "runmem")

st.graphviz_chart(graph)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

df = pd.DataFrame(np.random.randn(20, 2) / [50, 50] + [10.22, 78.00],
columns=['lat', 'lon'])
st.map(df)



st.title("Fun with Streamlit")

if st.button("Celebrate!"):
    st.balloons()

if st.button("Let it Snow!"):
    st.snow()

if st.button("Simulate Loading"):
    with st.spinner("Loading..."):
        time.sleep(3)  # Simulating a long process
    st.success("Done!")