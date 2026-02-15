import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Title
st.title("📈Customer Segmentation App")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("customer_segmentation.csv", sep=",")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# Feature engineering
df["Age"] = 2025 - df["Year_Birth"]
df["Family_Size"] = df["Kidhome"] + df["Teenhome"]

df["Total_Spending"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)

features = ["Income", "Age", "Family_Size", "Recency", "Total_Spending"]
X = df[features].fillna(df[features].mean())

# Train model inside app
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)

# Sidebar inputs
income = st.sidebar.number_input("Income", 0, 200000, 50000)
age = st.sidebar.slider("Age", 18, 80, 30)
family = st.sidebar.slider("Family Size", 0, 5, 1)
recency = st.sidebar.slider("Recency", 0, 100, 50)
spending = st.sidebar.number_input("Total Spending", 0, 5000, 500)

# Prediction
input_data = scaler.transform([[income, age, family, recency, spending]])
cluster = kmeans.predict(input_data)[0]

st.subheader(f"Predicted Cluster: {cluster}")

# Business insights
if cluster == 0:
    st.success("Premium customer → Give exclusive offers")
elif cluster == 1:
    st.info("Budget customer → Discounts")
elif cluster == 2:
    st.warning("Potential customer → Targeted ads")
else:
    st.error("Family segment → Bundle products")

# Optional: Show data
st.subheader("Dataset Preview")
st.dataframe(df)
