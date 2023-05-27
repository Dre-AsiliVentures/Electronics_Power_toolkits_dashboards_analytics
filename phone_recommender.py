import streamlit as st

def main():
    # Create a checkbox
    checkbox_state = st.checkbox("Select Operating System!")

    # Display a message based on the checkbox state
    if checkbox_state:
        st.write("Checkbox is checked!")
    else:
        st.write("Checkbox is unchecked!")

if __name__ == '__main__':
    main()
