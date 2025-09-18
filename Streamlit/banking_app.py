import streamlit as st

st.title("My Banking Website")
st.write("Welcome to your personal banking dashboard!")

# Example of a tile for a recommender message
st.subheader("Financial Recommendations")
with st.container(border=True):
    st.markdown("**Personalized Investment Suggestion:**")
    st.write("Based on your risk profile, we recommend exploring low-volatility index funds.")
    st.button("Learn More")
