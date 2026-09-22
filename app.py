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
BUDGET_TIERS = ["<$100 HKD", "$100 - $250 HKD", "$250 - $500 HKD", "$500+ HKD"]

# Initialize Session State
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

if "group_budget" not in st.session_state:
    st.session_state.group_budget = 150  # Default HKD limit per person

if "max_travel_time" not in st.session_state:
    st.session_state.max_travel_time = 40  # Default max 40 mins


# Helper functions to add/remove members
def add_member():
    new_id = max([m["id"] for m in st.session_state.members], default=0) + 1
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


# --- GROUP CONSTRAINTS & BUDGET SECTION ---
st.subheader("💰 Group Constraints & Budget")

b_col1, b_col2, b_col3 = st.columns([2, 2, 2])

with b_col1:
    st.session_state.group_budget = st.slider(
        "Max Budget per Person (HKD)",
        min_value=50,
        max_value=1000,
        value=st.session_state.group_budget,
        step=50,
        format="HK$%d",
        help="Filters out spots and districts that exceed this price per head.",
    )

with b_col2:
    st.session_state.max_travel_time = st.slider(
        "Max Travel Time per Person (Mins)",
        min_value=15,
        max_value=60,
        value=st.session_state.max_travel_time,
        step=5,
        format="%d mins",
        help="Ensures nobody in the group travels longer than this threshold.",
    )

with b_col3:
    budget_preset = st.selectbox(
        "Quick Budget Preset",
        options=["Custom Slider", "Budget (<$100)", "Mid-Range ($100-$250)", "Splurge ($250+)"],
        index=0,
    )
    if budget_preset == "Budget (<$100)":
        st.session_state.group_budget = 100
    elif budget_preset == "Mid-Range ($100-$250)":
        st.session_state.group_budget = 200
    elif budget_preset == "Splurge ($250+)":
        st.session_state.group_budget = 400

st.divider()

# --- MEMBER INPUT LAYOUT ---
st.subheader("👥 Group Members & Preferences")

for i, member in enumerate(st.session_state.members):
    with st.container():
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
            st.write("")
            st.write("")
            if len(st.session_state.members) > 2:
                if st.button("🗑️", key=f"del_{member['id']}"):
                    remove_member(member["id"])
                    st.rerun()

        st.divider()

# Add Person Button
st.button("➕ Add Another Person", on_click=add_member)

# --- DEMO ALGORITHM / FILTERED RESULTS PREVIEW ---
st.subheader("⚡ Search & Filtered Recommendations")

if st.button("🔍 Find Fair Meeting Point", type="primary"):
    st.info(
        f"Filtering spots under **HK${st.session_state.group_budget}/person** and **<{st.session_state.max_travel_time} mins** travel time..."
    )

    # Mock District Scoring Demo based on constraints
    mock_districts = [
        {"district": "Mong Kok", "avg_time": 25, "est_cost": 120, "score": "High"},
        {"district": "Kowloon Tong", "avg_time": 20, "est_cost": 180, "score": "Medium"},
        {"district": "Admiralty / Central", "avg_time": 30, "est_cost": 280, "score": "Low"},
    ]

    # Filter based on group budget
    valid_districts = [
        d for d in mock_districts if d["est_cost"] <= st.session_state.group_budget
    ]

    if valid_districts:
        res_col1, res_col2 = st.columns(2)
        for d in valid_districts:
            with st.expander(f"📍 {d['district']} (Est. HK${d['est_cost']}/person)", expanded=True):
                st.write(f"⏱️ **Max Travel Time:** ~{d['avg_time']} mins")
                st.write(f"💸 **Estimated Cost:** HK${d['est_cost']} per head")
                st.write(f"✅ **Fits Group Budget:** Yes (HK${d['est_cost']} ≤ HK${st.session_state.group_budget})")
    else:
        st.warning(
            f"No districts match a budget of **HK${st.session_state.group_budget}**. Try raising your budget or expanding travel time limits."
        )

# --- DATA SUMMARY ---
with st.expander("📋 View Payload JSON"):
    payload = {
        "group_budget_hkd": st.session_state.group_budget,
        "max_travel_time_mins": st.session_state.max_travel_time,
        "members": st.session_state.members,
    }
    st.json(payload)
