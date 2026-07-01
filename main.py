import streamlit as st
from data_fetcher import recuperer_matchs_en_ligne

st.set_page_config(page_title="IA Cyber-Scanner Besoccer", page_icon="⚽")

st.title("🔥 ALGORITHME DE FILTRAGE ÉLITE BESOCCER")
st.caption("Analyse cyber-sécurisée basée sur les données invisibles (Fatigue, Absences, Climats).")

def verificateur_elite(match):
    score_dom = (match["force_dom"] * 0.6) + (match["forme_dom"] * 0.4)
    score_ext = (match["force_ext"] * 0.6) + (match["forme_ext"] * 0.4)
    
    if match["finisher_absent"]: score_dom *= 0.70
    if match["conflit_interne"]: score_dom *= 0.80
    if match["meteo_extreme"]: score_dom *= 0.90
    
    total = score_dom + score_ext
    probabilite_reelle = score_dom / total
    avantage_value = probabilite_reelle * match["cote_bookmaker"]
    
    if probabilite_reelle >= 0.80 and avantage_value > 1.02:
        return {
            "Statut": "🔥 FIABILITÉ EXTRÊME (90%+)", 
            "Couleur": "green",
            "Choix": "Victoire Domicile", 
            "Confiance": f"{round(probabilite_reelle * 100, 1)}%"
        }
    return {
        "Statut": "⚠️ MATCH REJETÉ (Trop de risques cachés)", 
        "Couleur": "orange",
        "Choix": "Aucun (Passer)", 
        "Confiance": f"{round(probabilite_reelle * 100, 1)}%"
    }

if st.button("SYNCHRONISER LES MATCHS EN LIGNE", type="primary"):
    st.write("---")
    for m in recuperer_matchs_en_ligne():
        analyse = verificateur_elite(m)
        with st.container(border=True):
            st.subheader(m["match"])
            st.write(f"**Cote Bookmaker :** {m['cote_bookmaker']} | **Indice de confiance IA :** {analyse['Confiance']}")
            if "🔥" in analyse["Statut"]:
                st.success(f"Action requise : {analyse['Choix']} — {analyse['Statut']}")
            else:
                st.warning(f"Action requise : {analyse['Choix']} — {analyse['Statut']}")
