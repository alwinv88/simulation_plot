import streamlit as st
import pandas as pd
from src import prepare_data, plot_graph, get_mean, read_file, apply_scaling
import io

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

    st.subheader("Plot")

    col_factor, col_x, col_y = st.columns([2, 2, 2])
    
    with col_factor:
        st.caption("Scale")
        factor = st.number_input(
            "Scale",
            value=1.0,
            step=0.1,
            format="%.4f",
            label_visibility="collapsed"
        )
    
    with col_x:
        st.caption("X-axis")
        x_col = st.selectbox(
            "X-axis",
            options=['time'],
            label_visibility="collapsed"
        )
    
    with col_y:
        st.caption("Y-axis")
        y_col = st.selectbox(
            "Y-axis",
            options=['Fx', 'Fy', 'Fz'],
            label_visibility="collapsed"
        )

    df = apply_scaling(df,factor=factor)
    
    col_plot, col_btn = st.columns([20, 1])  # wide plot, narrow button
    with col_plot:
        fig = plot_graph(df, x_col, y_col)
        st.pyplot(fig)
    
    with col_btn:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
        buffer.seek(0)
    
        st.download_button(
            label="⬇️",                # small icon button
            data=buffer,
            file_name=f"{y_col}_vs_{x_col}.png",
            mime="image/png"
        )



    st.subheader("Mean Values")
    means = get_mean(df)

    st.write(f"Average Fx: {means['Fx']:.4f}")
    st.write(f"Average Fy: {means['Fy']:.4f}")
    st.write(f"Average Fz: {means['Fz']:.4f}")
