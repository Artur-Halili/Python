import streamlit as st

def main():
    st.title("Hello, World!")

if st.button("Click Me"):
    st.write("Button Clicked!")
st.checkbox("Check me")
if st.checkbox("Check me to show some text"):
    st.write("You're seeing this because you checked the box")

user_input = st.text_input( "Enter text", "Sample text")
st.write( "You have entered: ",user_input)
age = st.number_input( "Enter youe age", min_value=0, max_value=100)
st.write(f"Your age is: {age}")

message = st.text_area("Enter a message")
st.write(f"Your message: {message}")

choice = st.radio ("Pick one", ["Choice 1", "Choice 2","Choice 3"])
st.write(f"You chose: {choice}")
if st.button("Success"):
    st.success("Operation was Successful")

if __name__ == "__main__":
        main()
