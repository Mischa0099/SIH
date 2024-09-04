import streamlit as st
import base64

# Function to set the background image with reduced opacity
def set_background(image_path, opacity=0.4):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, {opacity}), rgba(255, 255, 255, {opacity})), 
                        url(data:image/png;base64,{encoded_image});
            background-size: cover;
            background-position: center;
        }}
        .navbar a {{
            margin: 0 15px; 
            text-decoration: none; 
            color: white; 
            transition: color 0.3s;
        }}
        .navbar a:hover {{
            color: lightblue; /* Change color on hover */
        }}
        .chatbot-box {{
            background-color: grey; 
            color: white; 
            padding: 15px; 
            border-radius: 10px; 
            text-align: center; 
            transition: background-color 0.3s;
        }}
        .chatbot-box:hover {{
            background-color: darkgrey; /* Change color on hover */
            cursor: pointer; /* Change cursor to pointer */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Setting background image with reduced opacity
bg_image_path = "bg.png"
set_background(bg_image_path, opacity=0.4)

# Navbar with the logo
st.markdown(
    """
    <nav class="navbar" style="background-color: #333; padding: 10px;">
        <img src="logo.png" alt="Logo" style="height: 50px; float: left;">
        <div style="float: right; color: white;">
            <a href="#">Home</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
        </div>
        <div style="clear: both;"></div>
    </nav>
    """,
    unsafe_allow_html=True
)

# Main content
st.title("Welcome to Our Homepage")
st.markdown("### Explore our services and get in touch!")

# Chatbot box aligned to the bottom right corner
st.markdown(
    """
    <div style="position: fixed; bottom: 20px; right: 20px;">
        <a href="https://chatbot101.streamlit.app/" target="_blank" style="text-decoration: none;">
            <div class="chatbot-box">
                Chat with AI
            </div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
