import streamlit as st

# Page Configuration
st.set_page_config(page_title="MeetPoint HK", page_icon="📍", layout="wide")

st.markdown(
    """
    <style>
    /* ---------- Main app background ---------- */
    .stApp {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        background-attachment: fixed;
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #e0eafc 0%, #cfdef3 100%);
    }

    /* ---------- Hero Title ---------- */
    h1 {
        font-size: 3rem !important;
        font-weight: 800 !important;
        color: #4a3f8f !important;
        text-align: center;
        letter-spacing: 1px;
        padding-bottom: 8px;
        animation: fadeInDown 0.9s ease;
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-14px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ---------- Caption under the title ---------- */
    .stCaption, [data-testid="stCaptionContainer"] {
        text-align: center;
        color: #5a6b85 !important;
        font-size: 1rem;
        letter-spacing: 0.4px;
    }

    /* ---------- Subheaders ---------- */
    h3 {
        color: #2c4a6e;
        font-weight: 700;
        letter-spacing: 0.3px;
    }

    /* ---------- Dropdowns (Selectbox) ---------- */
    div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.75) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.25) !important;
        border-radius: 12px !important;
        transition: all 0.25s ease;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.08);
    }

    div[data-baseweb="select"] > div:hover {
        border-color: rgba(118, 75, 162, 0.6) !important;
        box-shadow: 0 6px 18px rgba(118, 75, 162, 0.22);
        transform: translateY(-1px);
    }

    /* Selected value text */
    div[data-baseweb="select"] span {
        color: #2c4a6e !important;
        font-weight: 500;
    }

    /* Dropdown popover menu */
    ul[data-testid="stSelectboxVirtualDropdown"],
    div[data-baseweb="popover"] ul {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(12px);
        border-radius: 12px !important;
        border: 1px solid rgba(102, 126, 234, 0.25) !important;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.2);
    }

    li[role="option"]:hover {
        background: linear-gradient(90deg, #eef1ff 0%, #f5e9ff 100%) !important;
    }

    /* ---------- Text inputs ---------- */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.75) !important;
        border: 1px solid rgba(102, 126, 234, 0.25) !important;
        border-radius: 12px !important;
        color: #2c4a6e !important;
        transition: all 0.25s ease;
    }
    .stTextInput input:focus {
        border-color: #764ba2 !important;
        box-shadow: 0 0 0 3px rgba(118, 75, 162, 0.15) !important;
    }

    /* ---------- Labels ---------- */
    label, .stSelectbox label, .stTextInput label {
        color: #3f5170 !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.3px;
    }

    /* ---------- Buttons ---------- */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.5rem 1.1rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px rgba(102, 126, 234, 0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(118, 75, 162, 0.45);
        filter: brightness(1.05);
    }
    .stButton > button:active {
        transform: translateY(0);
    }

    /* ---------- Divider ---------- */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.35), transparent);
    }

    /* ---------- Glassy member cards ---------- */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.55);
        backdrop-filter: blur(10px);
        border-radius: 18px !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 8px 28px rgba(102, 126, 234, 0.12);
        padding: 12px 16px;
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        box-shadow: 0 12px 34px rgba(118, 75, 162, 0.22);
        transform: translateY(-2px);
    }
    /* ---------- Subheaders (e.g. "👥 Group Members & Preferences") ---------- */
    h3 {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 60%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 0.5px;
        padding-bottom: 6px;
        display: inline-block;
        position: relative;
    }

    /* Subtle underline accent under subheaders */
    h3::after {
        content: "";
        position: absolute;
        left: 0;
        bottom: 0;
        height: 3px;
        width: 60%;
        background: linear-gradient(90deg, #667eea, #f093fb);
        border-radius: 3px;
        opacity: 0.7;
    }

    /* ---------- Member names (##### Person A) ---------- */
    h5 {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #4a3f8f !important;
        letter-spacing: 0.4px;
        padding: 4px 12px;
        display: inline-block;
        border-radius: 10px;
        background: linear-gradient(90deg, rgba(102,126,234,0.14) 0%, rgba(240,147,251,0.14) 100%);
        border-left: 4px solid #764ba2;
        transition: all 0.25s ease;
    }

    h5:hover {
        background: linear-gradient(90deg, rgba(102,126,234,0.28) 0%, rgba(240,147,251,0.28) 100%);
        transform: translateX(3px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
st.button("➕ Add Another Person", on_click=add_member)

# --- DEBUG / CURRENT DATA SUMMARY ---
st.subheader("📋 Current Group Summary (Data)")
st.json(st.session_state.members)
