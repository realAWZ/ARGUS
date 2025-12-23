import streamlit as st
import requests
import base64
import time

# --- PAGE CONFIG (Dark Mode / Wide) ---
st.set_page_config(page_title="ARGUS", page_icon="👁️", layout="wide")

# --- CUSTOM "ARGUS" TERMINAL STYLE ---
st.markdown("""
<style>
    .big-font { font-size:40px !important; font-family: 'Courier New'; font-weight: bold; color: #00ff00; }
    .stApp { background-color: #000000; color: #00ff00; }
    .stButton>button { border: 1px solid #00ff00; color: #00ff00; background-color: #0e1117; font-family: 'Courier New'; }
    .stButton>button:hover { background-color: #00ff00; color: black; border: 1px solid white; }
    .stTextInput>div>div>input { color: #00ff00; background-color: #0e1117; font-family: 'Courier New'; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([1, 4])
with col1:
    st.write("# 👁️")
with col2:
    st.markdown('<p class="big-font">ARGUS SYSTEM ONLINE</p>', unsafe_allow_html=True)

st.caption("A.R.G.U.S. // Advanced Reconnaissance & Ground Utility System // AUTH: ZOSCHE")
st.divider()

# --- SYSTEM TABS ---
tab1, tab2, tab3 = st.tabs(["📡 TACTICAL RADAR", "🔐 SECURE COMMS", "💪 BIO-METRICS"])

# ==================================================
# TAB 1: TACTICAL RADAR (Weather Intel)
# ==================================================
with tab1:
    st.markdown("### 🛰️ GLOBAL SECTOR SCAN")
    city = st.text_input("ENTER COORDINATES (CITY):", "Newton, NJ")
    
    if st.button("INITIATE SCAN"):
        try:
            # 1. Geocode
            geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
            if "results" in geo:
                lat = geo["results"][0]["latitude"]
                lon = geo["results"][0]["longitude"]
                
                # 2. Weather Scan
                w = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,rain").json()
                curr = w['current']
                
                # 3. Display HUD
                c1, c2, c3 = st.columns(3)
                c1.metric("THERMAL", f"{curr['temperature_2m']}°F")
                c2.metric("VELOCITY", f"{curr['wind_speed_10m']} MPH")
                c3.metric("PRECIP", f"{curr['rain']} MM")
                
                st.divider()
                
                # 4. Tactical Assessment
                if curr['temperature_2m'] < 32:
                    st.error("⚠️ ALERT: CRYOGENIC HAZARD DETECTED.")
                elif curr['wind_speed_10m'] > 20:
                    st.warning("⚠️ ALERT: HIGH VELOCITY WIND SHEAR.")
                else:
                    st.success("✅ SECTOR SECURE. OPERATIONS NORMAL.")
                    
            else:
                st.error("❌ TARGET LOST. COORDINATES INVALID.")
        except:
            st.error("❌ SATELLITE LINK SEVERED.")

# ==================================================
# TAB 2: SECURE COMMS (Encryption Relay)
# ==================================================
with tab2:
    st.markdown("### 🔐 CRYPTOGRAPHIC RELAY")
    
    mode = st.radio("SELECT PROTOCOL:", ["ENCRYPT (OUTBOUND)", "DECRYPT (INBOUND)"], horizontal=True)
    text_input = st.text_area("DATA STREAM INPUT:")
    
    if st.button("EXECUTE PROTOCOL"):
        if text_input:
            if "ENCRYPT" in mode:
                # Base64 Encoding
                encoded = base64.b64encode(text_input.encode("utf-8")).decode("utf-8")
                st.success("🔒 MESSAGE SECURED:")
                st.code(encoded, language="text")
                st.caption("TRANSMIT THIS KEY VIA SECURE CHANNEL.")
                
            else: # DECRYPT
                try:
                    decoded = base64.b64decode(text_input).decode("utf-8")
                    st.success(f"🔓 MESSAGE DECODED: {decoded}")
                except:
                    st.error("❌ DECRYPTION FAILED. KEY CORRUPTED.")

# ==================================================
# TAB 3: BIO-METRICS (The Grind)
# ==================================================
with tab3:
    st.markdown("### 🧬 OPERATOR STATUS")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**PHYSICAL PROTOCOLS**")
        task_1 = st.checkbox("Creatine Load (5g)")
        task_2 = st.checkbox("Hydration (1 Gallon)")
        task_3 = st.checkbox("Hypertrophy Training")
        
    with col2:
        st.write("**CEREBRAL PROTOCOLS**")
        task_4 = st.checkbox("Read 10 Pages")
        task_5 = st.checkbox("Skill Acquisition (Code)")
        task_6 = st.checkbox("No Sugar")
        
    # Progress Logic
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6]
    completed = sum(tasks)
    total = len(tasks)
    percent = completed / total
    
    st.divider()
    st.write(f"SYSTEM INTEGRITY: {int(percent*100)}%")
    st.progress(percent)
    
    if percent == 1.0:
        st.balloons()
        st.success("🚀 FULL SYSTEM OPTIMIZATION ACHIEVED.")
