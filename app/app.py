import streamlit as st
import pandas as pd
import joblib

def main():
    st.set_page_config(page_title="Smart parking predictor", page_icon="🚘", layout="centered")
    st.title("Smart parking predictor")
    st.write("This application estimates the probability of finding a parking spot.")
    st.header("Parking predction")

    location = st.selectbox("Select location", ["Centre", "Shopping mall", "Stadium", "Office area"])
    day = st.selectbox("Day of the week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    hour = st.slider("Hour of the day", 0, 23, 12)
    rain = st.checkbox("Is it raining?")

    model = joblib.load("models/parking_model.pkl")

    if st.button("Predict"):

        location_office_area = 0
        location_shopping_mall = 0
        location_stadium = 0

        if location == "Office Area":
            location_office_area = 1
        elif location == "Shopping Mall":
            location_shopping_mall = 1
        elif location == "Stadium":
            location_stadium = 1

        input_data = pd.DataFrame({
            "hour": [hour],
            "day_of_the_week": [days[day]],
            "temperature": [15],
            "rain": [int(rain)],
            "event_nearby": [0],
            "location_office_area": [location_office_area],
            "location_shopping_mall": [location_shopping_mall],
            "location_stadium": [location_stadium]
        })

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        st.subheader("Prediction result")

        st.metric(
            "Chance of free parking",
            f"{probability * 100:.1f}%"
        )

        if probability > 0.6:
            st.success("Parking should be easy to find 🚗")
        elif probability > 0.4:
            st.warning("Parking might be limited ⚠️")
        else:
            st.error("Parking will likely be difficult ❌")


if __name__ == "__main__":
    main()