import streamlit as st
from datetime import date, time

from data.options import (
    HK_LOCATIONS,
    ACTIVITIES,
    DEFAULT_MAX_TRAVEL_TIME,
    DEFAULT_BUDGET,
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Create Meetup | MeetPoint HK",
    page_icon="📍",
    layout="wide",
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "members" not in st.session_state:
    st.session_state.members = [
        {
            "id": 1,
            "name": "Person A",
            "origin": "HKUST (Clear Water Bay)",
            "max_travel_time": DEFAULT_MAX_TRAVEL_TIME,
            "budget": DEFAULT_BUDGET,
            "activities": ["🍜 Dinner / Food"],
            "date": date.today(),
            "start_time": time(18, 30),
            "end_time": time(21, 0),
            "preferred_time": time(19, 30),
        },
        {
            "id": 2,
            "name": "Person B",
            "origin": "Central",
            "max_travel_time": DEFAULT_MAX_TRAVEL_TIME,
            "budget": DEFAULT_BUDGET,
            "activities": ["🍜 Dinner / Food"],
            "date": date.today(),
            "start_time": time(18, 30),
            "end_time": time(21, 0),
            "preferred_time": time(19, 30),
        },
        {
            "id": 3,
            "name": "Person C",
            "origin": "PolyU (Hung Hom)",
            "max_travel_time": DEFAULT_MAX_TRAVEL_TIME,
            "budget": DEFAULT_BUDGET,
            "activities": ["☕ Cafe / Coffee"],
            "date": date.today(),
            "start_time": time(18, 30),
            "end_time": time(21, 0),
            "preferred_time": time(19, 30),
        },
    ]


if "meetup_name" not in st.session_state:
    st.session_state.meetup_name = "Friday Dinner"


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def add_member():
    existing_ids = [
        member["id"]
        for member in st.session_state.members
    ]

    new_id = max(existing_ids, default=0) + 1

    st.session_state.members.append(
        {
            "id": new_id,
            "name": f"Person {chr(64 + new_id)}",
            "origin": HK_LOCATIONS[0],
            "max_travel_time": DEFAULT_MAX_TRAVEL_TIME,
            "budget": DEFAULT_BUDGET,
            "activities": [ACTIVITIES[0]],
            "date": date.today(),
            "start_time": time(18, 30),
            "end_time": time(21, 0),
            "preferred_time": time(19, 30),
        }
    )


def remove_member(member_id):
    if len(st.session_state.members) <= 2:
        return

    st.session_state.members = [
        member
        for member in st.session_state.members
        if member["id"] != member_id
    ]


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📍 Create a Meetup")
st.caption(
    "Tell us when and where everyone is available."
)

st.divider()


# --------------------------------------------------
# MEETUP INFORMATION
# --------------------------------------------------

st.subheader("🍜 Meetup Information")

st.session_state.meetup_name = st.text_input(
    "Meetup name",
    value=st.session_state.meetup_name,
    placeholder="e.g. Friday Dinner",
)

st.divider()


# --------------------------------------------------
# MEMBERS
# --------------------------------------------------

st.subheader("👥 Group Members")

st.caption(
    "Each person can set their own location, travel limit, "
    "budget, activities, and availability."
)


for member in st.session_state.members:

    member_id = member["id"]

    with st.container(border=True):

        header_col, delete_col = st.columns(
            [8, 1]
        )

        with header_col:
            st.markdown(
                f"### 👤 {member['name']}"
            )

        with delete_col:
            if len(st.session_state.members) > 2:
                if st.button(
                    "🗑️",
                    key=f"delete_{member_id}",
                    help="Remove this person",
                ):
                    remove_member(member_id)
                    st.rerun()

        # ------------------------------------------
        # BASIC INFORMATION
        # ------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            member["name"] = st.text_input(
                "Name",
                value=member["name"],
                key=f"name_{member_id}",
            )

            member["origin"] = st.selectbox(
                "Starting location",
                HK_LOCATIONS,
                index=(
                    HK_LOCATIONS.index(member["origin"])
                    if member["origin"] in HK_LOCATIONS
                    else 0
                ),
                key=f"origin_{member_id}",
            )

        with col2:

            member["max_travel_time"] = st.slider(
                "Maximum travel time",
                min_value=10,
                max_value=120,
                value=member["max_travel_time"],
                step=5,
                format="%d min",
                key=f"travel_{member_id}",
            )

            member["budget"] = st.number_input(
                "Budget per person (HK$)",
                min_value=0,
                max_value=5000,
                value=member["budget"],
                step=10,
                key=f"budget_{member_id}",
            )

        # ------------------------------------------
        # ACTIVITY
        # ------------------------------------------

        member["activities"] = st.multiselect(
            "What would you like to do?",
            ACTIVITIES,
            default=member["activities"],
            key=f"activities_{member_id}",
        )

        # ------------------------------------------
        # DATE
        # ------------------------------------------

        st.markdown("#### 📅 When are you available?")

        member["date"] = st.date_input(
            "Date",
            value=member["date"],
            key=f"date_{member_id}",
        )

        # ------------------------------------------
        # TIME RANGE
        # ------------------------------------------

        time_col1, time_col2, preferred_col = st.columns(
            3
        )

        with time_col1:

            member["start_time"] = st.time_input(
                "Available from",
                value=member["start_time"],
                key=f"start_{member_id}",
            )

        with time_col2:

            member["end_time"] = st.time_input(
                "Available until",
                value=member["end_time"],
                key=f"end_{member_id}",
            )

        with preferred_col:

            member["preferred_time"] = st.time_input(
                "Preferred meeting time",
                value=member["preferred_time"],
                key=f"preferred_{member_id}",
            )

        # ------------------------------------------
        # VALIDATION
        # ------------------------------------------

        if member["start_time"] >= member["end_time"]:
            st.warning(
                "⚠️ Your ending time must be later "
                "than your starting time."
            )

        if not member["activities"]:
            st.info(
                "💡 Select at least one activity."
            )


# --------------------------------------------------
# ADD MEMBER
# --------------------------------------------------

st.button(
    "➕ Add Another Person",
    on_click=add_member,
    use_container_width=True,
)


st.divider()


# --------------------------------------------------
# GROUP SUMMARY
# --------------------------------------------------

st.subheader("📋 Meetup Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.markdown(
        f"### {st.session_state.meetup_name}"
    )

    st.write(
        f"👥 **{len(st.session_state.members)} people**"
    )

with summary_col2:

    dates = [
        member["date"]
        for member in st.session_state.members
    ]

    if len(set(dates)) == 1:
        st.write(
            f"📅 **{dates[0].strftime('%A, %B %d, %Y')}**"
        )
    else:
        st.write(
            "📅 Members have selected different dates."
        )


# --------------------------------------------------
# MEMBER SUMMARY CARDS
# --------------------------------------------------

for member in st.session_state.members:

    st.markdown(
        f"""
        **👤 {member['name']}**

        📍 {member['origin']}  
        🚇 Max travel: {member['max_travel_time']} min  
        💰 Budget: HK${member['budget']}  
        🍽️ {", ".join(member['activities'])}  
        📅 {member['date'].strftime('%a, %b %d')}  
        🕐 {member['start_time'].strftime('%I:%M %p').lstrip('0')}
        –
        {member['end_time'].strftime('%I:%M %p').lstrip('0')}  
        ⭐ Preferred:
        {member['preferred_time'].strftime('%I:%M %p').lstrip('0')}
        """
    )

    st.divider()


# --------------------------------------------------
# FIND MEETING PLACE
# --------------------------------------------------

if st.button(
    "📍 Find a Meeting Place",
    type="primary",
    use_container_width=True,
):

    invalid = False

    for member in st.session_state.members:

        if member["start_time"] >= member["end_time"]:
            invalid = True

        if not member["activities"]:
            invalid = True

    if invalid:

        st.error(
            "Please fix the highlighted preferences "
            "before continuing."
        )

    else:

        st.success(
            "✅ Preferences collected! "
            "The meeting-place recommendation engine "
            "will go here."
        )

        st.session_state.show_results = True