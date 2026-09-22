import streamlit as st

# Page Configuration
st.set_page_config(page_title="MeetPoint HK", page_icon="📍", layout="wide")

st.title("📍 MeetPoint HK")
st.caption("Step 1: Group Member Setup & Preferences")

# Predefined list of popular HK locations for testing
HK_LOCATIONS = [
    "HKUST (Clear Water Bay)",
    "Central",
    "PolyU (Hung Hom)",
    "Causeway Bay",
    "Mong Kok",
    "Kwun Tong",
    "Shatin",
    "Tsuen Wan",
    "Tsim Sha Tsui",
    "TKO (Tseung Kwan O)",
]

ACTIVITIES = [
    "Dinner / Food",
    "Cafe / Coffee",
    "Board Games / Leisure",
    "Drinks / Bar",
    "Shopping / Walking",
]

TIMES = [
    "12:00 PM (Lunch)",
    "3:00 PM (Afternoon Tea)",
    "6:00 PM (Early Dinner)",
    "7:30 PM (Dinner)",
    "9:00 PM (Late Drinks)",
]

# Initialize Session State to keep track of dynamic members
if "members" not in st.session_state:
    st.session_state.members = [
        {
            "id": 1,
            "name": "Person A",
            "origin": "HKUST (Clear Water Bay)",
            "preference": "Dinner / Food",
            "time": "7:30 PM (Dinner)",
        },
        {
            "id": 2,
            "name": "Person B",
            "origin": "Central",
            "preference": "Dinner / Food",
            "time": "7:30 PM (Dinner)",
        },
        {
            "id": 3,
            "name": "Person C",
            "origin": "PolyU (Hung Hom)",
            "preference": "Cafe / Coffee",
            "time": "7:30 PM (Dinner)",
        },
    ]


# Helper functions to add/remove members
def add_member():
    new_id = (
        max([m["id"] for m in st.session_state.members], default=0) + 1
    )
    st.session_state.members.append(
        {
            "id": new_id,
            "name": f"Person {chr(64 + len(st.session_state.members) + 1)}",
            "origin": "Mong Kok",
            "preference": "Dinner / Food",
            "time": "7:30 PM (Dinner)",
        }
    )


def remove_member(member_id):
    if len(st.session_state.members) > 2:
        st.session_state.members = [
            m for m in st.session_state.members if m["id"] != member_id
        ]


# --- UI LAYOUT ---

st.subheader("👥 Group Members & Preferences")

# Display inputs for each member dynamically
for i, member in enumerate(st.session_state.members):
    with st.card() if hasattr(st, "card") else st.container():
        st.markdown(f"##### {member['name']}")
        col1, col2, col3, col4, col5 = st.columns([2, 3, 3, 3, 1])

        with col1:
            member["name"] = st.text_input(
                "Name", value=member["name"], key=f"name_{member['id']}"
            )

        with col2:
            member["origin"] = st.selectbox(
                "Starting Location",
                options=HK_LOCATIONS,
                index=HK_LOCATIONS.index(member["origin"])
                if member["origin"] in HK_LOCATIONS
                else 0,
                key=f"origin_{member['id']}",
            )

        with col3:
            member["preference"] = st.selectbox(
                "Preferred Activity",
                options=ACTIVITIES,
                index=ACTIVITIES.index(member["preference"])
                if member["preference"] in ACTIVITIES
                else 0,
                key=f"pref_{member['id']}",
            )

        with col4:
            member["time"] = st.selectbox(
                "Desired Meeting Time",
                options=TIMES,
                index=TIMES.index(member["time"])
                if member["time"] in TIMES
                else 0,
                key=f"time_{member['id']}",
            )

        with col5:
            st.write("")  # Alignment spacing
            st.write("")
            if len(st.session_state.members) > 2:
                if st.button("🗑️", key=f"del_{member['id']}"):
                    remove_member(member["id"])
                    st.rerun()

        st.divider()

# Add Person Button
st.button("➕ Add Another Person", on_click=add_member)

# --- DEBUG / CURRENT DATA SUMMARY ---
st.subheader("📋 Current Group Summary (Data)")
st.json(st.session_state.members)