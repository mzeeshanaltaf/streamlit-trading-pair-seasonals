import folium
from streamlit_folium import st_folium
import pandas as pd
from util import *

# Session state variables so that values persist across reruns
if 'function_called' not in st.session_state:
    st.session_state.function_called = False
if 'latitude' not in st.session_state:
    st.session_state.latitude = False
if 'longitude' not in st.session_state:
    st.session_state.longitude = False
if 'iss_people' not in st.session_state:
    st.session_state.iss_people = False


# Initialize streamlit app
page_title = "ISS Tracker"
page_icon = "🛰️"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

# Application title
st.title('International Space Station (ISS) Tracker🛰️')
st.write(':blue[***"Tracking the ISS and its Astronauts in Real-Time! 🌌👨‍🚀***]')
st.write("This application is your window to the International Space Station! See its real-time location as it orbits "
         "Earth 🌍 and get an up-to-date list of the astronauts aboard 🛰️. Whether you’re a space enthusiast or just "
         "curious, explore the wonders of space and its crew from your screen! 🌟")

# Button for updating ISS location
button = st.button('Update ISS Location', type='primary')

# This logic will allow get_iss_details function to be called only when button is pressed
if button:
    st.session_state.function_called = False

# Get the details of ISS
iss_latitude, iss_longitude, iss_people = get_iss_details()

iss_tracker_col, astronauts_name_col = st.columns(2)
with iss_tracker_col:
    with st.container():
        st.subheader('ISS Location:')

        # Display the Map
        map = folium.Map(location=[iss_latitude, iss_longitude], zoom_start=2)
        # Define a custom icon for a satellite (satellite-dish)
        icon = folium.Icon(icon='satellite-dish', color='blue', prefix='fa')
        folium.Marker(location=[iss_latitude, iss_longitude], popup='ISS', tooltip='ISS', icon=icon).add_to(map)
        st_data = st_folium(map, use_container_width=True)

with astronauts_name_col:
    with st.container():
        # Display the name of Astronauts in tabular form
        st.subheader('Name of Astronauts in ISS:')
        df_iss_people = pd.DataFrame(iss_people, columns=['Astronauts Names'])
        df_iss_people.index = df_iss_people.index + 1  # Start the index from 1
        df_iss_people.index.name = 'Number'  # Update the index column name
        st.dataframe(df_iss_people, use_container_width=True)

# Display footer
display_footer()
