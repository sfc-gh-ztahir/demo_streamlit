import streamlit as st
from snowflake.snowpark.context import get_active_session

st.set_page_config(page_title="DE Apps – App1", page_icon="❄️")

st.title("DE_APPS – App1 - Version3 (Git + Snowflake Streamlit)")

st.markdown(
    """
This app is deployed from a **GitHub repository** via **Snowflake Git integration**.

Environment:
- Database: shown below (derived from the active Snowflake session)
- Branch:
  - `feature/new_change` → DDEV_APP.DE_APPS.APP1_DEV
  - `test`              → DEXPLORE_APP.DE_APPS.APP1_TEST
  - `main`              → DPROD_APP.DE_APPS.APP1
"""
)

session = get_active_session()

# Show current DB/Schema/Warehouse so you see which env you’re in
info = session.sql("SELECT CURRENT_DATABASE() AS db, CURRENT_SCHEMA() AS schema, CURRENT_WAREHOUSE() AS wh").to_pandas()
st.subheader("Current Snowflake context")
st.table(info)

st.subheader("Sample data from SNOWFLAKE_SAMPLE_DATA")
df = (
    session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER")
    .limit(10)
    .to_pandas()
)
st.dataframe(df)

if st.button("Say hello"):
    st.success("Hello from App1 running in Snowflake from Git!")
