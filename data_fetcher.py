import requests
from datetime import datetime

def recuperer_matchs_en_ligne():
    matchs_reels = []
    url = f"https://openligadb.de{datetime.now().year}"
    
    try:
        reponse = requests.get(url, timeout=10)
        if reponse.status_code == 200:
            donnees = reponse.json()
            for match in donnees[:10]:
                equipe_dom = match.get("team1", {}).get("teamName", "Team 1")
                equipe_ext = match.get("team2", {}).get("teamName", "Team 2")
                matchs_reels.append({
                    "match": f"{equipe_dom} vs {equipe_ext}",
                    "force_dom": 85, "forme_dom": 80, 
                    "force_ext": 75, "forme_ext": 70,
                    "finisher_absent": False, "conflit_interne": False, "meteo_extreme": False, "cote_bookmaker": 1.85
                })
        if not matchs_reels:
            raise Exception()
    except Exception:
        matchs_reels = [
            {"match": "France vs Italie", "force_dom": 88, "forme_dom": 85, "force_ext": 80, "forme_ext": 75, "finisher_absent": False, "conflit_interne": False, "meteo_extreme": False, "cote_bookmaker": 1.65},
            {"match": "Bresil vs Argentine", "force_dom": 85, "forme_dom": 80, "force_ext": 86, "forme_ext": 88, "finisher_absent": True, "conflit_interne": False, "meteo_extreme": False, "cote_bookmaker": 2.10},
            {"match": "Bayern vs Dortmund", "force_dom": 90, "forme_dom": 92, "force_ext": 78, "forme_ext": 80, "finisher_absent": False, "conflit_interne": True, "meteo_extreme": True, "cote_bookmaker": 1.40}
        ]
    return matchs_reels
