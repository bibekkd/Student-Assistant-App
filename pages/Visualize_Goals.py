import streamlit as st
import pandas as pd

st.title("Visualize Goals")

# Example data
data = {
    'Goal': ['Exam 1', 'Exam 2', 'Career', 'Personal Life'],
    'Progress': [70, 50, 80, 60]
}
df = pd.DataFrame(data)

st.bar_chart(df.set_index('Goal'))