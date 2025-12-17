import streamlit as st
import pandas as pd
from src import prepare_data, plot_graph, get_mean, read_file, apply_scaling


st.title("Force Signal Visualization")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    df = prepare_data(df)

    st.subheader("Scaling Factor")

    factor = st.number_input(
        "Enter multiplication factor",
        value=1.0,        # default
        step=0.1,
        format="%.4f"
    )

    df = apply_scaling(df, factor)

    # Select force component
    y_col = st.selectbox("Select Y Component", ['Fx', 'Fy', 'Fz'])
    x_col = st.selectbox("Select X Component", ['time']) 

    fig = plot_graph(df, x_col, y_col)
    st.pyplot(fig)

    st.subheader("Mean Values")
    means = get_mean(df)

    st.write(f"Average Fx: {means['Fx']:.4f}")
    st.write(f"Average Fy: {means['Fy']:.4f}")
    st.write(f"Average Fz: {means['Fz']:.4f}")
