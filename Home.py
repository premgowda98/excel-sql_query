import streamlit as st
import pandas as pd

from sql.handle_query import show

st.header('Excel - SQL Query Builder')
st.divider()

uploaded_files = st.file_uploader("Upload Excel File", accept_multiple_files=True, type=['.csv', '.xlsx'])


if uploaded_files:
    all_tables = [f"Table_{i+1}" for i in range(len(uploaded_files))]

    for (ind_file, table_name) in zip(uploaded_files, all_tables):
        with st.expander(rf"$\sf{{\textcolor{{black}}{{\Large {table_name}}}}}$"):
            all_sheets = pd.ExcelFile(ind_file).sheet_names

            all_sheets_tabs = st.tabs(all_sheets)
            sheet_df_names = [f"{table_name}_{ind_sheet_name}" for ind_sheet_name in all_sheets]

            for sheet_tab, org_sheet_name, sheet_name in zip(all_sheets_tabs, all_sheets, sheet_df_names):
                globals()[sheet_name] = pd.read_excel(ind_file, sheet_name=org_sheet_name)

                with sheet_tab:
                    st.write(globals()[sheet_name])

    show(table_names=sheet_df_names)

else:
    st.markdown('#')

