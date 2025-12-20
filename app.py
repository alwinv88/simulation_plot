import streamlit as st
import pandas as pd
from src import prepare_data, plot_graph, get_mean, read_file, apply_scaling
import io

st.title("Force Signal Visualization")

st.subheader("Load Data")
col_sim, col_paper = st.columns(2)
with col_sim:
    st.caption("Data from Simulation")
    file_sim = st.file_uploader(
        "Upload the file",
        type=["csv", "xlsx", "xls"],
        key="sim_file",
        label_visibility="collapsed"
    )

with col_paper:
    st.caption("Data from Paper")
    file_paper = st.file_uploader(
        "Upload the file",
        type=["csv", "xlsx", "xls"],
        key="paper_file",
        label_visibility="collapsed"
    )

df = None
data_mode = None
default_x = ["time"]
default_y = ["Force"]

if file_sim and not file_paper:
    df = read_file(file_sim)
    df = prepare_data(df)
    data_mode = "sim"

elif file_paper and not file_sim:
    df = read_file(file_paper)
    df = prepare_data(df)
    data_mode = "paper"

elif file_sim and file_paper:
    st.warning("Please upload only one file at a time.")


if data_mode == "sim":
    y_options = ['Fx', 'Fy', 'Fz']
elif data_mode == "paper":
    y_options = ['Force']


if df is not None:
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
            options=y_options if y_options else ["Select column"],
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
    for col, mean_val in means.items():
        st.write(f"Average {col}: {mean_val:.4f}")
