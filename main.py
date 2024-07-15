import pandas as pd
from util import *

page_title = "Seasonal Insights"
page_icon = "📊"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout='centered')
st.title(f'📊 {page_title}')
st.write(':blue[***Empower Your Trades with Seasonal Insights***]')
st.write(" Seasonal Insights is a powerful tool for traders, providing a comprehensive analysis of monthly seasonal "
         "trends for various trading pairs over the last 25 years. By identifying whether each month was bullish, "
         "bearish, or neutral, this app helps you understand the historical biases and make informed trading "
         "decisions. Visualize past performance and discover the monthly trends to gain an edge in the market.")

# Get the list of sheets present in the Excel file
excel_file = 'Trading_Seasonal.xlsx'
xls = pd.ExcelFile(excel_file)

# Get the sheet names
sheet_names = xls.sheet_names

# Select box widget to choose the trading pair
st.subheader('Trading Pair Selection:')
trading_pair = st.selectbox('Choose the Trading Pair', sheet_names, label_visibility='collapsed')

# Read the Excel file and make the first column ('Year') as the index
df = pd.read_excel(excel_file, sheet_name=trading_pair, index_col=0)

# Copy the last row ('Bias') into separate dataframe
df_bias = df.tail(1)

# Remove the last row ('Bias') from the dataframe as it is no more needed
df = df.drop(df.index[-1])

# Plot the heatmap of Seasonal Trend
st.subheader(f'Seasonal Trend of {trading_pair} ({df.index[0]}- {df.index[-1]}):')
plot_heatmap(df)

# Plot the heatmap of Overall Bias
st.subheader(f'Overall Bias of {trading_pair}:')
plot_heatmap(df_bias)

