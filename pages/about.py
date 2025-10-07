import streamlit as st

st.title("About the Steam Sales Dashboard")
st.caption("Background, data sources and technology behind this project.")


st.markdown("""
### 📂 Data Source
The sales dataset is compiled from publicly available Steam game information
(e.g., [Kaggle Steam dataset](https://www.kaggle.com/) or other open sources).  
It includes fields like *game name, release date, genre, price, and total sales*.

### 🎯 Purpose
To give gamers, developers, and analysts a clear picture of:
- *Sales trends over time*
- *Genre popularity and revenue distribution*
- Insights that could help *publishers plan releases* or *players spot trends*.

### 🛠 Tech Stack
- *Python* for data cleaning & analysis  
- *Pandas & Plotly* for visualization  
- *Streamlit* for the web app  

---

💡 This project is for educational and analytical purposes only and is not affiliated with Valve or Steam.
""")