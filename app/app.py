import streamlit as st

def main():
    st.set_page_config(page_title="Smart parking predictor", page_icon="🚘", layout="centered")
    st.title("Smart parking predictor")
    st.write("This application estimates the probability of finding a parking spot.")
    st.header("Parking predction")

    location = st.selectbox("Select location", ["Centre", "Shopping mall", "Stadium", "Office area"])
    day = st.selectbox("Day of the week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    hour = st.slider("Hour of the day", 0, 23, 12)
    rain = st.checkbox("Is it raining?")

    if st.button("Predict"):
        st.success("Prediction incoming...")


if __name__ == "__main__":
    main()