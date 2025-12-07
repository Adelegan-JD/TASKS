# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Sales Performance Dashboard", layout="wide")

@st.cache_data
def load_data(path="eletronic_sales.xlsx"):
    # Load and sanitize
    df = pd.read_excel(path, engine='openpyxl')
    # Ensure standardized columns
    df.columns = [c.strip() for c in df.columns]
    # Parse date
    date_col = [c for c in df.columns if 'date' in c.lower()]
    if date_col:
        df['Date'] = pd.to_datetime(df[date_col[0]], errors='coerce')
    else:
        # fallback: try first column
        df['Date'] = pd.to_datetime(df.iloc[:,0], errors='coerce')
    # Clean numeric columns
    df['Units'] = pd.to_numeric(df['Units'], errors='coerce').fillna(0).astype(int)
    # Remove currency symbols and convert to float
    df['Price'] = df['Price'].astype(str).str.replace('[^0-9.-]', '', regex=True).astype(float)
    # Revenue
    df['Revenue'] = df['Units'] * df['Price']
    # Derived cols
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['MonthName'] = df['Date'].dt.strftime('%b')
    df['Week'] = df['Date'].dt.isocalendar().week
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
years = sorted(df['Year'].dropna().unique().tolist())
sel_year = st.sidebar.selectbox("Year", options=["All"] + years, index=0)
branches = ["All"] + sorted(df['Branch'].dropna().unique().tolist())
sel_branch = st.sidebar.selectbox("Branch", options=branches, index=0)
products = ["All"] + sorted(df['Products'].dropna().unique().tolist())
sel_product = st.sidebar.selectbox("Product", options=products, index=0)
agents = ["All"] + sorted(df['Sales Agent'].dropna().unique().tolist())
sel_agent = st.sidebar.selectbox("Sales Agent", options=agents, index=0)

# Apply filters
dff = df.copy()
if sel_year != "All":
    dff = dff[df['Year'] == int(sel_year)]
if sel_branch != "All":
    dff = dff[dff['Branch'] == sel_branch]
if sel_product != "All":
    dff = dff[dff['Products'] == sel_product]
if sel_agent != "All":
    dff = dff[dff['Sales Agent'] == sel_agent]

# KPIs
total_units = int(dff['Units'].sum())
total_revenue = float(dff['Revenue'].sum())
avg_rev_unit = total_revenue / total_units if total_units else 0
num_products = int(dff['Products'].nunique())
num_agents = int(dff['Sales Agent'].nunique())

st.title("Sales Performance Dashboard")
st.markdown("**Company:** DADE Electronic Store Ltd")
# KPI metrics
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Units Sold", f"{total_units:,}")
k2.metric("Total Revenue", f"₦{total_revenue:.2f}")
k3.metric("Avg Revenue / Unit", f"₦{avg_rev_unit:.2f}")
k4.metric("Number of Products", f"{num_products}")
k5.metric("Number of Sales Agents", f"{num_agents}")

# Layout: left charts, right detail tables
col_left, col_right = st.columns((2,1))

with col_left:
    st.subheader("Monthly Revenue Trend")
    if 'Date' in dff:
        monthly = dff.groupby(pd.Grouper(key='Date', freq='ME'))['Revenue'].sum().reset_index()
        if not monthly.empty:
            fig = px.line(monthly, x='Date', y='Revenue', title="Monthly Revenue", markers=True)
            st.plotly_chart(fig, width='stretch')
        else:
            st.info("No monthly data for selected filters.")
    st.subheader("Revenue by Branch")
    rev_branch = dff.groupby('Branch')['Revenue'].sum().reset_index().sort_values('Revenue', ascending=False)
    fig2 = px.bar(rev_branch, x='Branch', y='Revenue', title="Revenue by Branch", text='Revenue')
    st.plotly_chart(fig2, width='stretch')
    st.subheader("Top Products by Revenue")
    rev_prod = dff.groupby('Products')['Revenue'].sum().reset_index().sort_values('Revenue', ascending=False).head(20)
    fig3 = px.bar(rev_prod, x='Products', y='Revenue', title="Top Products", text='Revenue')
    st.plotly_chart(fig3, width='stretch')

with col_right:
    st.subheader("Top Sales Agents")
    rev_agent = dff.groupby('Sales Agent')['Revenue'].sum().reset_index().sort_values('Revenue', ascending=False)
    st.dataframe(rev_agent.head(20).style.format({"Revenue":"₦{:.2f}"}))
    st.subheader("Download filtered data")
    csv = dff.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, file_name="filtered_sales.csv", mime="text/csv")

# Additional analytics
st.markdown("---")
st.subheader("Detailed Analysis")
# Weekly trend
if 'Week' in dff.columns:
    weekly = dff.groupby(['Year','Week'])['Revenue'].sum().reset_index()
    # plot last year if filter is all
    last_year = dff['Year'].max()
    weekly_last = weekly[weekly['Year']==last_year]
    if not weekly_last.empty:
        figw = px.line(weekly_last, x='Week', y='Revenue', title=f'Weekly Revenue Trend - {last_year}', markers=True)
        st.plotly_chart(figw, width='stretch')

# Moving averages (daily)
if 'Date' in dff.columns and not dff.empty:
    daily = dff.groupby('Date')['Revenue'].sum().reset_index().sort_values('Date')
    if not daily.empty:
        daily['7d_MA'] = daily['Revenue'].rolling(window=7, min_periods=1).mean()
        daily['30d_MA'] = daily['Revenue'].rolling(window=30, min_periods=1).mean()
        figm = px.line(daily, x='Date', y=['Revenue','7d_MA','30d_MA'], title="Daily Revenue + Moving Averages")
        st.plotly_chart(figm, width='stretch')

st.caption("Built with: Date, Branch, Sales Agent, Products, Units, Price → Revenue = Units * Price")
