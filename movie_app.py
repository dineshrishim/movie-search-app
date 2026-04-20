import streamlit as st
import requests

st.title("Movie Search App")

movie = st.text_input("Enter Any movie name:")

if movie:
    name = movie.lower()
    if name == "surya":
        st.write("This dude ain't straight")
        st.stop()
    elif name == "nicholas":
        st.write("This man? This man is the kind of statistical anomaly that makes researchers quietly close their laptops and choose a different career path. This man is so confidently engineered that if confidence were a building, he wouldn’t just live in it, he’d be the zoning law, the architect, and the reason the city gave up inspections entirely. " \
        "This man is walking proof that sometimes the universe just hits “randomize” and forgets to balance the stats. Charisma? Maxed. Presence? Unreasonably high. Self-awareness? Selectively installed, like a software update he keeps ignoring because “it’s working fine.”" \
        "People dont interact with him, they experience him. Like weather. Or a minor historical event. Something you dont argue with, you just adjust your plans around it." 
        "And yet, theres a flaw. A tragic, almost poetic contradiction running through the whole performance. Dinesh. Dinesh is there. Always there. The constant. The one who actually sees the man for what he is and still chooses appreciation like it’s a responsibility, not a reaction. Dinesh doesn’t admire from a distance, he invests. Emotionally. Consistently. Like he’s convinced loyalty is supposed to be a two-way system." \
        "And this man? This man treats it like background noise. Not out of malice. Not even effort. Worse. Indifference. The kind of indifference that doesnt even realize its being unfair, because its too busy being the main character in its own internal simulation." \
        "Dinesh offers recognition like its oxygen. Steady. Present. Unquestioned. And it just… drifts past. Not rejected. Not returned. Just unregistered. Like someone speaking in a room where the echo decided not to participate. If gratitude were physics, Dinesh would be exerting force, and this man would be politely refusing to accelerate." \
        "And the most ridiculous part? Dinesh still shows up. Still sees value. Still holds the line like emotional loyalty is something worth maintaining even when the return policy clearly says “no refunds, no acknowledgment, please try again later.”" \
        "So here we are. This man? This man is exceptional in all the loud ways. And Dinesh? Dinesh is the quiet reason that exception doesnt collapse under its own self-importance.")
        st.stop()
    elif name == "ansh":
        st.write("Oh HELL nah")
        st.stop()
    elif name == "dhanush":
        st.write("Let's forget about him")
        st.stop()
    
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
