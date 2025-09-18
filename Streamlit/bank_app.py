import streamlit as st
import pandas as pd
from streamlit_tile import streamlit_tile

# --- Set Up Page Configuration ---
st.set_page_config(
    page_title="FinanSight - Your Personal Banking Hub",
    page_icon="🏦",
    layout="wide"
)

# --- Top Navigation Bar with a Custom CSS approach ---
st.markdown("""
<style>
.main-header {
    font-size:30px;
    font-weight: bold;
    color: #0072C6;
    padding: 10px 0;
    text-align: center;
}
.st-emotion-cache-1pxpx5d { # targets main content style
    padding-top: 2rem;
    padding-bottom: 5rem;
}
</style>
<div class="main-header">
    FinanSight
</div>
""", unsafe_allow_html=True)

# --- Account Summary Section ---
st.header("Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Checking Account", value="$15,200.50", delta="+$250")
with col2:
    st.metric(label="Savings Account", value="$45,750.80", delta="+$1,000")
with col3:
    st.metric(label="Credit Card Balance", value="$-1,200.00", delta="+$50")

st.markdown("---")

# --- Transaction History Section ---
st.subheader("Recent Transactions")
transactions = pd.DataFrame({
    'Date': ['2025-09-15', '2025-09-14', '2025-09-13', '2025-09-12'],
    'Description': ['Online Purchase', 'Grocery Store', 'ATM Withdrawal', 'Salary Deposit'],
    'Amount': ['-$75.25', '-$120.50', '-$200.00', '+$3,500.00']
})
st.dataframe(transactions, use_container_width=True, hide_index=True)

# --- Recommender Output Tile Section ---
st.markdown("---")
st.subheader("Personalized Recommendations")

# Use streamlit_tile for a prominent, professional-looking message
recommendation_tile_clicked = streamlit_tile(
    title="Smart Savings Tip",
    description="Based on your spending, we recommend investing $500 monthly into a high-yield savings account to reach your goal faster.",
    icon="savings", # Uses a Material UI icon
    color_theme="green", # Theme color
    key="recommender_tile" # Unique key for the tile
)

# Optional: Add an action for when the tile is clicked
if recommendation_tile_clicked:
    st.balloons()
    st.info("Great choice! Click here to set up your investment plan.")

# --- Customizing the tile's appearance with CSS ---
st.markdown("""
<style>
/* Adjust spacing and center the icon */
.streamlit-tile-container .card-icon {
    display: flex;
    justify-content: center;
    align-items: center;
}
.streamlit-tile-container .card-icon .material-symbols-outlined {
    font-size: 40px;
}
</style>
""", unsafe_allow_html=True)
