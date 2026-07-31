import streamlit as st

st.title("App of Retribution!")

st.write("Good morrow, mortal! I am the App of Retribution, and I shall guide you through the trials of your day. But first, I must know your name.")



name = st.text_input("Enter thine name, mortal")

st.success("Ah yes. A wonderful name " + name + "! I hope you're ready.")



feeling = st.selectbox("How are you feeling this day?", ["Delighted", "Sorrowful", "Angered", "Apathetic"])

if feeling == "Delighted":
    st.balloons()
    st.write("Ah, a joyous soul! May your day be filled with laughter, and your night calm.")
elif feeling == "Sorrowful":
    st.balloons()
    st.write("Ah, a melancholic heart. May the morrow bring you solace and comfort.")
elif feeling == "Angered":
    st.write("Ah, a fiery spirit! May your anger be tempered with wisdom and understanding.")
elif feeling == "Apathetic":
    st.write("Your apathy is noted, mortal human. May the morrow bring the spirit of passion to your heart!")