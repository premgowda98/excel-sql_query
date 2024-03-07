import streamlit as st
import pandas as pd
import duckdb


def show(table_names: list):
    my_contanier = st.container()
    with st.sidebar:
        st.markdown('### Build Query')
        st.divider()

        st.markdown('#### List of tables avaliable')
        for table in table_names:
            st.write(table)

        sql_query = st.text_area('', placeholder="Write you query here")
        exec_button = st.button('Execute')

    if exec_button:
        my_contanier.markdown('#### Results')

        try:
            out = duckdb.sql(sql_query).df()
            my_contanier.write(out)

            st.download_button(label="Download Results", data=out.to_csv().encode('utf-8'),file_name="Results.csv", mime='text/csv')
        except Exception as e:
            my_contanier.error(e)