import streamlit as st

# ==========================================
# CALCULATEUR DE DOSAGE DU BÉTON - APP STREAMLIT
# ==========================================

st.set_page_config(
    page_title="Calculateur de dosage du béton",
    page_icon="🧱",
    layout="centered"
)

st.title("🧱 Calculateur de Dosage du Béton")
st.markdown("Calculez les quantités de ciment, sable, gravier et eau nécessaires pour votre volume de béton.")

st.divider()

# --- Entrées utilisateur ---
st.subheader("Paramètres")

volume = st.number_input(
    "Volume de béton (m³)",
    min_value=0.0,
    value=1.0,
    step=0.1,
    format="%.2f"
)

# --- Paramètres fixes (non modifiables par l'utilisateur) ---
dosage_ciment = 350.0   # kg/m³
sable_par_m3 = 0.50     # m³/m³
gravier_par_m3 = 0.80   # m³/m³
eau_par_m3 = 175.0      # L/m³

st.divider()

# --- Calculs ---
if st.button("Calculer", type="primary", use_container_width=True) or volume > 0:
    ciment = volume * dosage_ciment
    sacs = ciment / 50
    sable = volume * sable_par_m3
    gravier = volume * gravier_par_m3
    eau = volume * eau_par_m3

    st.subheader("📊 Résultats")

    r1, r2 = st.columns(2)
    with r1:
        st.metric("Volume de béton", f"{volume:.2f} m³")
        st.metric("Ciment", f"{ciment:.2f} kg")
        st.metric("Sacs de 50 kg", f"{sacs:.2f} sacs")

    with r2:
        st.metric("Sable", f"{sable:.2f} m³")
        st.metric("Gravier", f"{gravier:.2f} m³")
        st.metric("Eau", f"{eau:.2f} L")

    with st.expander("Voir le détail du calcul"):
        st.write(f"- Ciment = Volume × Dosage = {volume:.2f} × {dosage_ciment:.1f} = **{ciment:.2f} kg**")
        st.write(f"- Sacs de 50 kg = Ciment ÷ 50 = {ciment:.2f} ÷ 50 = **{sacs:.2f} sacs**")
        st.write(f"- Sable = Volume × {sable_par_m3:.2f} = **{sable:.2f} m³**")
        st.write(f"- Gravier = Volume × {gravier_par_m3:.2f} = **{gravier:.2f} m³**")
        st.write(f"- Eau = Volume × {eau_par_m3:.1f} = **{eau:.2f} L**")

    # Export des résultats
    resultats_txt = f"""CALCULATEUR DE DOSAGE DU BÉTON
==========================================
Volume de béton : {volume:.2f} m³
Ciment          : {ciment:.2f} kg
Sacs de 50 kg   : {sacs:.2f} sacs
Sable           : {sable:.2f} m³
Gravier         : {gravier:.2f} m³
Eau             : {eau:.2f} litres
==========================================
"""
    st.download_button(
        label="📥 Télécharger les résultats (.txt)",
        data=resultats_txt,
        file_name="dosage_beton.txt",
        mime="text/plain"
    )
else:
    st.info("Entrez un volume supérieur à 0 ou cliquez sur **Calculer**.")

st.divider()
st.caption("Valeurs de référence données à titre indicatif ; adaptez-les selon la formulation souhaitée.")
