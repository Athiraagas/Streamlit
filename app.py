import streamlit as st

# Set title
st.title("My First Streamlit App")

# Add text input
name = st.text_input("Enter your name:", "Guest")

# Add a slider
age = st.slider("Select your age:", 0, 100, 25)

# Add a button
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old!")
else:
    st.write("Fill out the details above and press Submit.")
