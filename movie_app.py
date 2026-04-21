import streamlit as st
import requests

st.title("Movie Search App")

movie = st.text_input("Enter Any movie name:")

if movie:
    api_key = "7fa6ccf5"

    url = f"http://www.omdbapi.com/?t={movie}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "False":
        st.write("Movie ain't found bro")
    else:
        st.subheader(data["Title"])
        st.write("Year:", data["Year"])
        st.write("Rating:", data["imdbRating"])
        st.write("Plot:", data["Plot"])
        st.image(data["Poster"])