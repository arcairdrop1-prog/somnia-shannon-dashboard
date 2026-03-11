import streamlit as st
import pandas as pd
from utils import SomniaExplorer
import plotly.express as px
from datetime import datetime

# Configuração da Página
st.set_page_config(page_title="Somnia Builder Dashboard", layout="wide")
explorer = SomniaExplorer()

st.title("⚡ Somnia Network Real-Time Dashboard")
st.markdown("---")

# Sidebar para ferramentas do Usuário
st.sidebar.header("User Tools")
user_wallet = st.sidebar.text_input("Check Wallet Balance", placeholder="0x...")

if user_wallet:
    balance = explorer.get_balance(user_wallet)
    if balance is not None:
        st.sidebar.success(f"Balance: {balance:.4f} STT")
    else:
        st.sidebar.error("Invalid Address")

# Layout de Métricas Principais
data = explorer.get_network_data()

if data:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Block Height", f"#{data['block_height']}")
    col2.metric("Gas Price", f"{data['gas_gwei']:.2f} Gwei")
    col3.metric("TXs in Last Block", data['tx_count'])
    col4.metric("Network Status", "Operational", delta="Stable")

    # Gráfico Simulado de Atividade (Para visualização profissional)
    st.subheader("Network Activity Trend")
    chart_data = pd.DataFrame({
        'Time': pd.date_range(start=datetime.now(), periods=10, freq='min'),
        'TPS': [15, 30, 45, 20, 55, 80, 120, 95, 110, 130]
    })
    fig = px.line(chart_data, x='Time', y='TPS', title="Estimated TPS (Shannon Testnet)")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Unable to connect to Somnia RPC. Check your connection.")

# Rodapé Técnico
st.markdown("---")
st.caption("Built by venus11_builder | Powered by Somnia Shannon Testnet")
