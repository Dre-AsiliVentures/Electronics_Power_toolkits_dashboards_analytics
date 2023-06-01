import streamlit as st

# Create a title
st.title('Streamlit App with st.expander')

# Create a sidebar
st.sidebar.markdown('This is the sidebar.')

# Create a main area
#st.main.markdown('This is the main area.')
st.markdown('This is the main area.')

# Create an expander
with st.expander('Expander'):
  st.markdown('This is the content of the expander.')
