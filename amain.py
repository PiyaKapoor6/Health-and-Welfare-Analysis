import streamlit as st

pages=[
    st.Page("home.py",title="Home",icon='🏠'),
    st.Page("India_states.py",title="India Overview",icon='🇮🇳'),
    st.Page("Punjab_Analysis.py",title="Punjab Analysis",icon='📍'),
    st.Page("Rural_urban.py",title="Rural vs Urban",icon='⚖️'),
    st.Page("Disease_analysis.py",title="Disease Analysis",icon='🦠'),
    st.Page("trends.py",title="Trends & Forecast",icon='📈'),
    st.Page("ML_pred.py",title="ML Prediction",icon='🤖'),
    st.Page("zabout.py",title="About",icon='ℹ️')
]

nav=st.navigation(pages,position="top")
nav.run()