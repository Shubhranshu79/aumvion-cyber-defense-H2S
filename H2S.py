import streamlit as st
import random
import time
from datetime import datetime
import pandas as pd
import hashlib

# ==========================
# CONFIG & PAGE SETUP
# ==========================
st.set_page_config(page_title="AUMVION: The Unhackable Ecosystem", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0c0d12; color: #e0e0e0; font-family: 'Consolas', monospace; }
    .big-title { font-size: 42px; font-weight: bold; color: #00ffea; text-shadow: 0px 0px 15px #00ffea; }
    .sub-title { font-size: 24px; color: #ff007f; text-shadow: 0px 0px 10px #ff007f; }
    .metric-box {
        border: 2px solid #3d3d4b; border-radius: 8px; padding: 10px; margin-bottom: 10px;
        background-color: #1a1b24; text-align: center;
    }
    .metric-value { font-size: 28px; font-weight: bold; color: #00ffea; }
    .metric-label { font-size: 14px; color: #b0b0b0; }
    </style>
""", unsafe_allow_html=True)

# ==========================
# DATA & CORE LOGIC
# ==========================
threats = {
    "SQL Injection": {"type": "Web Attack", "description": "Attacker tried to manipulate a database query."},
    "DDoS Attack": {"type": "Network Attack", "description": "Massive traffic flood to overwhelm the server."},
    "Zero-Day Exploit": {"type": "Advanced Attack", "description": "Attack using a previously unknown software vulnerability."},
    "Phishing": {"type": "Social Engineering", "description": "User targeted with a fraudulent email."},
    "Insider Threat": {"type": "Internal Threat", "description": "Malicious activity from within the organization."},
    "Ransomware": {"type": "Malware Attack", "description": "Encrypted system files demanding a ransom."},
}

# Simulated AI reasoning for defense
def ai_analysis(threat_type, threat_desc):
    if threat_type == "Advanced Attack":
        return "AI Heuristic Analysis initiated. Automated code and binary diversification deployed to neutralize the exploit."
    elif threat_type == "Network Attack":
        return "Autonomous traffic shaping and network isolation activated. Geo-blocking of source IPs and a clean instance redeployed."
    else:
        # A simulated LLM-like response
        defense_action = f"Based on behavioral patterns, the AI platform has identified a {threat_type} threat. A playbook was autonomously executed. Defense: {threat_desc.split('.')[0]}."
        return defense_action

def calculate_metrics(ledger):
    resolved_count = len(ledger)
    total_time = sum(float(entry['Healing Time (s)']) for entry in ledger)
    mttr = total_time / resolved_count if resolved_count > 0 else 0
    return resolved_count, mttr

# Data for simulated locations (major Indian cities)
locations = {
    "Mumbai": {"lat": 19.0760, "lon": 72.8777},
    "Delhi": {"lat": 28.7041, "lon": 77.1025},
    "Bangalore": {"lat": 12.9716, "lon": 77.5946},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "Chennai": {"lat": 13.0827, "lon": 80.2707},
    "Kolkata": {"lat": 22.5726, "lon": 88.3639},
}

# Initializing session state
if "ledger" not in st.session_state:
    st.session_state.ledger = []
if "attack_in_progress" not in st.session_state:
    st.session_state.attack_in_progress = False
if "attack_counts" not in st.session_state:
    st.session_state.attack_counts = pd.DataFrame({'time': [], 'count': []})
if "auto_mode" not in st.session_state:
    st.session_state.auto_mode = False
if "current_attack_count" not in st.session_state:
    st.session_state.current_attack_count = 0.0

# ==========================
# STREAMLIT APP
# ==========================
st.markdown("<p class='big-title'>🛡️ AUMVION: The Unhackable Ecosystem</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Autonomous, Self-Healing Security Platform</p>", unsafe_allow_html=True)

# Create two columns for the dashboard
col1, col2 = st.columns([1.5, 2])

with col1:
    st.markdown("<h4 style='color:#00ffea; text-align: center;'>Performance Metrics</h4>", unsafe_allow_html=True)
    resolved_count, mttr = calculate_metrics(st.session_state.ledger)
    
    st.markdown(f"""
        <div class='metric-box'>
            <div class='metric-value'>{resolved_count}</div>
            <div class='metric-label'>Threats Automated</div>
        </div>
        <div class='metric-box'>
            <div class='metric-value'>{mttr:.2f}s</div>
            <div class='metric-label'>Avg. Time to Recovery</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h4 style='color:#00ffea; text-align: center;'>Real-time Threat Map</h4>", unsafe_allow_html=True)
    map_placeholder = st.empty()
    map_placeholder.map(pd.DataFrame({'lat': [20.5937], 'lon': [78.9629]}), zoom=4)
    
    st.markdown("---")
    st.header("⚙️ Controls")

    # Corrected and simplified logic for controls
    if st.session_state.auto_mode:
        if st.button("🔴 Disable Auto Mode", use_container_width=True, type="primary"):
            st.session_state.auto_mode = False
            st.session_state.attack_in_progress = False
            st.rerun()
        st.button("🚀 Launch Manual Attack", use_container_width=True, disabled=True)
    else:
        if st.button("🚀 Launch Manual Attack", use_container_width=True, type="primary"):
            st.session_state.attack_in_progress = True
            st.rerun()
        if st.button("🟢 Enable Auto Mode", use_container_width=True):
            st.session_state.auto_mode = True
            st.session_state.attack_in_progress = True
            st.rerun()

with col2:
    st.markdown("<h4 style='color:#00ffea; text-align: center;'>Live Threat Monitor</h4>", unsafe_allow_html=True)
    threat_line_chart = st.line_chart(st.session_state.attack_counts.set_index('time'))

    st.markdown("---")
    st.markdown("<h3 style='color:#00ffea;'>📑 Threat & Defense Ledger</h3>", unsafe_allow_html=True)
    ledger_placeholder = st.empty()

# The simulation loop
if st.session_state.attack_in_progress:
    threat_location_name, threat_coords = random.choice(list(locations.items()))
    threat_name, threat_details = random.choice(list(threats.items()))

    # New logic for "jick jack" graph
    st.session_state.current_attack_count += random.uniform(0.5, 1.5)
    if st.session_state.current_attack_count < 0:
        st.session_state.current_attack_count = 0.0

    new_attack_data = pd.DataFrame({'time': [datetime.now()], 'count': [st.session_state.current_attack_count]})
    st.session_state.attack_counts = pd.concat([st.session_state.attack_counts, new_attack_data]).tail(15)
    
    # 1. Threat Detected
    st.toast(f"🟥 ALERT! {threat_name} detected from {threat_location_name}!", icon="🚨")
    map_placeholder.map(pd.DataFrame({'lat': [threat_coords['lat']], 'lon': [threat_coords['lon']]}), zoom=6)
    threat_line_chart.add_rows(new_attack_data.set_index('time'))
    
    time.sleep(1)
    
    # 2. AI Analyzes & Defends
    start_time = time.time()
    defense_strategy = ai_analysis(threat_details["type"], threat_details["description"])
    st.toast(f"🟨 AUMVION AI is Defending...", icon="🛡️")
    
    time.sleep(1.5)
    
    # 3. System Healed
    end_time = time.time()
    healing_time = end_time - start_time
    st.toast(f"🟩 System Healed! Recovery Time: {healing_time:.2f}s", icon="✅")
    
    # Add to ledger
    entry_data = {
        "Time": datetime.now().strftime("%H:%M:%S"), 
        "Threat": threat_name, 
        "Location": threat_location_name,
        "Defense Strategy": defense_strategy, 
        "Healing Time (s)": f"{healing_time:.2f}",
        "Hash": hashlib.sha256(str(datetime.now()).encode()).hexdigest()[:8] + "..."
    }
    st.session_state.ledger.append(entry_data)
    
    # Update displays
    df_ledger = pd.DataFrame(st.session_state.ledger)
    ledger_placeholder.dataframe(df_ledger.set_index("Time"), use_container_width=True)
    
    # Rerun the app based on mode
    if st.session_state.auto_mode:
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.attack_in_progress = False
        st.rerun()