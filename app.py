import pylogix
import streamlit as st
import time

PLC_IP = "192.168.1.10"
TAGS = ["LightCurtain.Beam_Intensity_MedHigh",
        "LightCurtain.Beam_Intensity_Total"]

st.set_page_config(page_title="PLC Tag Monitor",
                   layout="centered")

st.title("PLC Tag Monitor")

placeholder = st.empty()

with pylogix.PLC(PLC_IP) as comm:
    while True:
        results = comm.Read(TAGS)
        data = []
        for result in results:
            data.append({"Tag":result.TagName,
                        "Value":result.Value})
            
        with placeholder.container():
            st.table(data)

        time.sleep(1)