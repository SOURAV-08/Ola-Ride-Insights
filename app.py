import streamlit as st
import pandas as pd

# 1. Page Setup
st.set_page_config(page_title="Ola Insights", layout="wide")
st.title("🚖 Ola Ride Sharing Analysis")

# 2. Load the Cleaned Data 
@st.cache_data
def load_data():
    # Using the file name visible in your VS Code explorer
    return pd.read_csv("clean_ola_dataset.csv") 

df = load_data()

# 3. Sidebar Navigation
st.sidebar.title("Project Menu")
page = st.sidebar.radio("Navigate to:", ["Overview", "SQL Insights", "Dashboard"])

if page == "Overview":
    st.header("Project Problem Statement")
    st.write("Analyzing OLA’s ride-sharing data to derive actionable insights for operational efficiency and customer satisfaction[cite: 6, 8].")
    
    st.subheader("Business Use Cases")
    st.write("- Identifying peak demand hours [cite: 10]")
    st.write("- Analyzing customer behavior [cite: 11]")
    st.write("- Understanding pricing patterns [cite: 12]")

elif page == "SQL Insights":
    st.header("SQL Query Analysis")
    # This answers the specific SQL questions from your brief
    q_choice = st.selectbox("Select a Query Result:", [
        "Average Ride Distance per Vehicle Type",
        "Total Number of Cancelled Rides (Customers)",
        "UPI Payment Transactions",
        "Total Successful Booking Value"
    ])
    
    if q_choice == "Average Ride Distance per Vehicle Type":
        # SQL Question 2 Logic [cite: 41]
        res = df.groupby('Vehicle_Type')['Ride_Distance'].mean()
        st.bar_chart(res)
    elif q_choice == "Total Number of Cancelled Rides (Customers)":
        # SQL Question 3 Logic [cite: 42]
        cancelled = df[df['Booking_Status'].str.contains('Canceled by Customer', na=False)]
        st.metric("Cancelled by Customer", len(cancelled))
    elif q_choice == "Total Successful Booking Value":
        # SQL Question 9 Logic [cite: 48]
        success_val = df[df['Booking_Status'] == 'Success']['Booking_Value'].sum()
        st.metric("Total Success Revenue", f"₹{success_val:,.2f}")

elif page == "Dashboard":
    st.header("Power BI Performance Dashboard")
    st.info("Visualizing ride trends, revenue, and cancellations[cite: 28, 30].")
    # Take a screenshot of your Power BI and save it as dashboard.png in this folder
    st.image("dashboard.png", caption="Ola Ride Insights Dashboard")