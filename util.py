import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def plot_heatmap(df):
    # Create the heatmap
    plt.figure(figsize=(10, len(df) / 2))
    sns.heatmap(df, annot=False, cmap='RdYlGn', linewidths=.5, cbar=False)

    # Display the heatmap
    st.pyplot(plt)
