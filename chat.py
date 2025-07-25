import streamlit as st

st.set_page_config(page_title="Swahili Chatbot Test", page_icon="🤖")

st.title("Karibu kwenye Swahili Chatbot! 🤖")
st.subheader("Hii ni toleo la majaribio.")

st.write("Ikiwa unaona hii ujumbe, basi app yako ya Streamlit inafanya kazi vizuri kabisa! 🎉")

if st.button("Bonyeza hapa"):
    st.success("Umebonyeza kifungo! 🎉")

st.info("➡️ Unaweza sasa kuongeza mazungumzo ya chatbot au kuboresha mwonekano.")
