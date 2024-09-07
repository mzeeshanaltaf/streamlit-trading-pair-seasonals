import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_heatmap(df):
    # Create a custom colormap
    colors = ["red", "gray", "green"]
    n_bins = [1, 1, 1]  # Discretize the interpolation into bins
    cmap_name = 'custom_heatmap'

    # Create the colormap
    cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=sum(n_bins))

    # Create the heatmap
    plt.figure(figsize=(10, len(df) / 2))
    sns.heatmap(df, annot=False, cmap=cm, linewidths=.5, cbar=False)

    # Display the heatmap
    st.pyplot(plt)


def display_footer():
    footer = """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            text-align: center;
            color: grey;
            padding: 10px 0;
        }
        </style>
        <div class="footer">
            Made with ❤️ by <a href="mailto:zeeshan.altaf@92labs.ai">Zeeshan</a>.
        </div> 
    """
    st.markdown(footer, unsafe_allow_html=True)
