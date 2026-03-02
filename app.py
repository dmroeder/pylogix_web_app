import config
import pylogix
import streamlit as st
import time


st.set_page_config(page_title="PLC Tag Monitor",
                   layout="centered")

st.title("PLC Tag Monitor")

placeholder = st.empty()

with pylogix.PLC(config.PLC_IP, config.PLC_SLOT) as comm:
    while True:
        results = comm.Read(config.TAGS)
        data = []
        for result in results:
            data.append({"Tag":result.TagName,
                        "Value":result.Value,
                        "Status":result.Status})

        with placeholder.container():
            st.table(data)

        time.sleep(config.POLL_RATE)
