import streamlit as st

st.set_page_config(
    page_title="MeetPoint HK",
    page_icon="📍",
    layout="wide",
)

st.title("📍 MeetPoint HK")

st.markdown(
    """
    ## Find somewhere that works for everyone.

    MeetPoint helps groups find a meeting place by considering
    everyone's location, availability, travel time, budget,
    and activity preferences.
    """
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/1_Create_Meetup.py",
        label="+ Create a Meetup",
        icon="👥",
    )

with col2:
    st.info(
        "🔗 Joining a meetup will be added next."
    )