import streamlit as st

st.title('Playround')
st.text_area('Input prompt', '')
st.button('Submit')
st.slider('Temperature', 0.00, 2.00, 1.00)
st.slider('Top P', 0.00, 1.00, 1.00)
st.slider('Maximum length', 1, 4000, 1)
st.checkbox('Show probabilities')
st.code('print("Hello, world!")', language='python', line_numbers = True)
