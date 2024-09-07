import streamlit as st
import requests


# This function return the location (lang and lat) and number of astronauts in ISS
def get_iss_details():
    if not st.session_state.function_called:  # This condition will be True only when button is pressed
        # Get the ISS current location and extract latitude and longitude from it
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        st.session_state.latitude = float(data["iss_position"]["latitude"])
        st.session_state.longitude = float(data["iss_position"]["longitude"])

        # Get the name of Astronauts in ISS
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        st.session_state.iss_people = [person['name'] for person in data['people'] if person['craft'] == 'ISS']
        st.session_state.function_called = True

    return st.session_state.latitude, st.session_state.longitude, st.session_state.iss_people


def display_footer():
    footer = """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            text-align: center;
            color: grey;
            padding: 10px 0;
        }
        </style>
        <div class="footer">
            Made with ❤️ by <a href="mailto:zeeshan.altaf@92labs.ai">Zeeshan</a>.
            Source code <a href='https://github.com/mzeeshanaltaf/streamlit-iss-tracker'>here</a>.</div> 
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
