import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

st.title("Steam Sales Trends and Insights")
st.caption("Interactive dashboard to explore Steam game sales, revenue growth and yearly trends.")

df = pd.read_csv("steam_sales.csv")





#1. Bar chart Top 10 Games by reviews

top10 = df.sort_values('#Reviews', ascending=False).head(10)
fig = px.bar(top10, x="Game Name", y="#Reviews",
             title= "Top 10 games by reviewsc",
             labels={"Game Name":"Game Name","#Reviews":"#Reviews"},
             color= "#Reviews",template="plotly_dark"
             )
st.plotly_chart(fig)





#2.Bar chart Top 10 Games by Rating

top10 = df.sort_values('Rating', ascending=False).head(10)
fig = px.bar(top10, x="Game Name", y="Rating",
             title= "Top 10 games by Rating",
             labels={"Game Name":"Game Name","Rating":"Rating"},
             color= "Rating",template="plotly_dark"
             )
st.plotly_chart(fig)




#3.Reviews vs Ratings

fig = px.scatter(df, x='Rating',y='#Reviews',
                 color='Game Name',
                 title='Reviews vs Rating',
                 labels={"Rating":"Rating","#Reviews":"#Reviews"},
                 template='plotly_dark')
st.plotly_chart(fig)




#4.Histogram - Distributioon of Ratings

fig = px.histogram(df, x="Rating",
                   nbins=10,
                   title="Distribution of Game Ratings",
                   labels={"Rating":"Rating(0-10)","Count":"Cout of Games"},
                   template="plotly_dark")
st.plotly_chart(fig)




#5.Scatter Plot - Rating vs Price(€)

fig = px.scatter(df,x='Price (€)',y='Rating',
                 color='Game Name',
                 title='Rating vs Price',
                 labels={"Rating":"Rating","Price":"Price"},
                 template='plotly_dark')
st.plotly_chart(fig)




#6.Histogram - Distribution of Discount%

fig = px.histogram(df, x="Discount%",
                   nbins=100,
                   title="Distribution of Discount%",
                   labels={"Discount%":"Discount(0 - 100%)","Count":"Cout of Games"},
                   template="plotly_dark")
st.plotly_chart(fig)




#7.Line Chart - Average Discount  over time 

fig = px.line(df, x="Fetched At", y="Discount%",
             title= "Average discount Percentage over time ",
             labels={"Fetched At":"Fetched At","Discount%":"Discount%"},
             color= "Discount%",template="plotly_dark"
             )
st.plotly_chart(fig)





#8.Line Chart - Average Price trend over time 

fig = px.line(df, x="Fetched At", y="Price (€)",
             title= "Average Price trend over time ",
             labels={"Fetched At":"Fetched At","Price (€)":"Price (€)"},
             color= "Price (€)",template="plotly_dark"
             )
st.plotly_chart(fig)






#9.Scatter Plot - Discount% vs Review 

fig = px.scatter(df,x='Discount%',y='#Reviews',
                 color='Game Name',
                 title='Discount% vs Review ',
                 labels={"#Reviews":"#Reviews","Discount%":"Discount%"},
                 template='plotly_dark')
st.plotly_chart(fig)





#10.Bar chart Top 10 Games With heighest Discount

top10 = df.sort_values('Discount%', ascending=False).head(10)
fig = px.bar(top10, x="Game Name", y="Discount%",
             title= "Top 10 games by Discount",
             labels={"Game Name":"Game Name","Discount%":"Discount%"},
             color= "Discount%",template="plotly_dark"
             )
st.plotly_chart(fig)




#11.L
