import streamlit as st
import pandas as pd
from core.pile_reaction_plotter import generate_dxf_from_data
from core.utils import hex_to_aci


def the_why():
    with st.expander("Why?"):
        st.markdown(""" 
        ### Why?

        Representing pile reactions on a drawing has always been a unique challenge for me, especially after working with pile foundation design in **CSI Safe** and **Tekla Structural Designer**. While these two pieces of software allow the export of pile reactions as a table, they fall short in visualising the pile forces directly on the layout.

        In **Tekla**, even though you can export foundation reactions, pile forces are typically placed in a separate table and not superimposed on the pile layout, making it harder to visually identify piles exceeding the safe working loads.

        That's the reason I created this simple tool. Originally, I used it as a script for my work, but I recently decided to make it available to other engineers. It allows you to copy and paste the coordinates and reactions from an Excel table and download a **DXF** file at any scale. This file can then be easily superimposed on your pile layout for better visualization.

        #### Want to know how to export pile forces in Tekla TSD? Check out the guides below:
        - [Pile forces in Tekla Structural Designer](https://support.tekla.com/doc/tekla-structural-designer/2022/rel_2022sp3_new_pile_forces_report_table#:~:text=2022%20SP3:%20New%20Pile%20Forces%20Report%20Table.%20Tekla%20Structural)
        """)


def show_instructions():
    st.markdown("""
    ### Instructions:
    1. Enter the pile coordinates and Pile Reactions directly in the table (up to 100 rows).
    2. For larger datasets, upload an Excel file and select the column titles for the X, Y coordinates and the Pile loads. Ensure the excel files have a column header
    3. Download your generated DXF file.
    """)


MAX_ROWS = 100

st.title("Pile Reaction Plotter")

the_why()
show_instructions()

input_option = st.radio(
    "Choose input method",
    options=["Manual Input (up to 100 rows)", "Excel Upload (more than 100 rows)"],
    index=1,
)

scale_factors = {
    "1:1": 1,
    "1:20": 20,
    "1:25": 25,
    "1:30": 30,
    "1:50": 50,
    "1:100": 100,
    "1:200": 200,
    "1:500": 500,
    "1:1000": 1000,
}

# scale_factor_input = st.selectbox(
# "Select scale factor:", options=list(scale_factors.keys()), index=0
# )

text_height = st.slider("Text Height:", min_value=50, max_value=750, value=300)
text_color_hex = st.color_picker("Select text color:", value="#000000")

# Converting hex color to ACI
text_color_aci = hex_to_aci(text_color_hex)  # Converting hex to ACI value

if input_option == "Manual Input (up to 100 rows)":
    num_rows = st.number_input(
        "Number of rows (up to 100):", min_value=1, max_value=MAX_ROWS, value=5
    )

    # Creating a dataframe with empty columns
    manual_data = pd.DataFrame(
        {
            "X": [0.0] * num_rows,
            "Y": [0.0] * num_rows,
            "Pile Reaction": [0.0] * num_rows,
        }
    )

    manual_data.index = manual_data.index + 1

    edited_data = st.data_editor(manual_data, use_container_width=True)

    if st.button("Generate DXF"):
        try:
            # scale_factor = float(scale_factors[scale_factor_input])
            scale_factor = 1000

            dxf_file = generate_dxf_from_data(
                edited_data,
                scale_factor,
                text_height,
                text_color_aci,
                "X",
                "Y",
                "Pile Reaction",
            )
            st.success("DXF file generated successfully!")
            st.download_button(
                label="Download DXF",
                data=dxf_file,
                file_name="manual_reactions_scaled.dxf",
                mime="application/dxf",
            )

        except ValueError:
            st.error("Please enter valid input values.")

else:
    st.markdown("### Upload Excel File")
    uploaded_file = st.file_uploader(
        "Choose an Excel file", accept_multiple_files=False, type=["xlsx"]
    )

    if uploaded_file:
        data = pd.read_excel(uploaded_file)
        st.write("Uploaded Data:")
        st.write(data)

        # User selects column headers from uploaded data
        x_header = st.selectbox("Select X-coordinate column", data.columns, index=0)
        y_header = st.selectbox("Select Y-coordinate column", data.columns, index=1)
        reaction_header = st.selectbox(
            "Select Pile Reaction column", data.columns, index=2
        )

        if st.button("Generate DXF from Excel"):
            try:
                # scale_factor = float(scale_factors[scale_factor_input])
                scale_factor = 1000

                dxf_file = generate_dxf_from_data(
                    data,
                    scale_factor,
                    text_height,
                    text_color_aci,
                    x_header,
                    y_header,
                    reaction_header,
                )

                st.success("DXF file generated successfully!")

                st.download_button(
                    label="Download DXF",
                    data=dxf_file,
                    file_name="pile_reaction_drawing.dxf",
                    mime="application/dxf",
                )
            except ValueError:
                st.error("Please enter valid input values.")
