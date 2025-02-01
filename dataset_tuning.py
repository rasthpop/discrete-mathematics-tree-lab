import pandas as pd

def dataset_tuning():
    weapons = {
        "Shahed-136/131": "Loitering Munition (Kamikaze Drones)",
        "Lancet": "Loitering Munition (Kamikaze Drones)",
        "Kub": "Loitering Munition (Kamikaze Drones)",
        "Orlan-10": "Reconnaissance UAVs",
        "ZALA": "Reconnaissance UAVs",
        "Supercam": "Reconnaissance UAVs",
        "Merlin-VR": "Reconnaissance UAVs",
        "Молнія": "Reconnaissance UAVs",
        "Фенікс": "Reconnaissance UAVs",
        "Orion": "Reconnaissance UAVs",
        "Eleron": "Reconnaissance UAVs",
        "Привет-82": "Reconnaissance UAVs",
        "Forpost": "Reconnaissance UAVs",
        "Картограф": "Reconnaissance UAVs",
        "Granat-4": "Reconnaissance UAVs",
        "Orlan-30": "Reconnaissance UAVs",
        "Reconnaissance UAV": "Reconnaissance UAVs",
        "Mohajer-6": "Combat UAVs",
        "Orlan-10 and ZALA and Supercam": "Reconnaissance UAV Combinations",
        "Orlan-10 and Orlan-30 and ZALA and Supercam": "Reconnaissance UAV Combinations",
        "Orlan-10 and ZALA": "Reconnaissance UAV Combinations",
        "Orlan-10 and Supercam": "Reconnaissance UAV Combinations",
        "Shahed-136/131 and Lancet": "Loitering & Reconnaissance Mix",
        "Unknown UAV": "Unknown UAV",
        'KAB': "Aerial Bomb",
        'Aerial Bomb': "Aerial Bomb",
        "Intercontinental ballistic missile": "Intercontinental ballistic missile",
        "Iskander-M": "Ballistic Missiles",
        "KN-23": "Ballistic Missiles",
        "Iskander-M/KN-23": "Ballistic Missiles",
        "Iskander-M and Iskander-K": "Ballistic Missiles",
        "Iskander-M/KN-23 and X-47 Kinzhal": "Ballistic Missiles",
        "X-101/X-555": "Cruise Missiles",
        "Kalibr": "Cruise Missiles",
        "X-59/X-69": "Cruise Missiles",
        "X-59": "Cruise Missiles",
        "X-69": "Cruise Missiles",
        "X-22/X-32": "Cruise Missiles",
        'X-22/X-31P': "Cruise Missiles",
        "X-22": "Cruise Missiles",
        "X-32": "Cruise Missiles",
        "X-35": "Cruise Missiles",
        "X-31P": "Cruise Missiles",
        "X-31PD": "Cruise Missiles",
        "X-31": "Cruise Missiles",
        "Iskander-K": "Cruise Missiles",
        "P-800 Oniks": "Cruise Missiles",
        "X-59MK2": "Cruise Missiles",
        "X-47 Kinzhal": "Hypersonic Missiles",
        "3M22 Zircon": "Hypersonic Missiles",
        "C-300": "Surface-to-Air Missiles (SAM)",
        "C-400": "Surface-to-Air Missiles (SAM)",
        "C-300/C-400": "Surface-to-Air Missiles (SAM)",
        "X-101/X-555 and Kalibr": "Cruise Missile Combinations",
        "X-101/X-555 and Kalibr and Iskander-K": "Cruise Missile Combinations",
        "X-101/X-555 and Kalibr and X-59/X-69": "Cruise Missile Combinations",
        "X-101/X-555 and X-22 and Kalibr": "Cruise Missile Combinations",
        "C-300/C-400 and Iskander-M": "Ballistic & SAM Combinations",
        "C-400 and Iskander-M": "Ballistic & SAM Combinations",
        "X-22 and X-32": "Other Combinations",
        "X-59 and X-35": "Other Combinations",
        "Unknown Missile": "Unknown Missile"
    }

    with open("missile_attacks_daily.csv", "r", encoding='utf-8') as file:
        result_file = [file.readline()]
        
        for line in file:
            line_list = line.strip().split(',')
            line_list[2] = weapons[line_list[2]]
            if not line_list[3]:
                line_list[3] = "Unknown"
            if not line_list[5]:
                line_list[5] = "Unknown"
            result_file.append(','.join(line_list) + '\n')
            

        with open("attack_data.csv", "w", encoding='utf-8') as output:
            output.writelines(result_file)

dataset_tuning()

# db = pd.read_csv("attack_data.csv")

# db["launch_place"].fillna("Unknown")
# db["carrier"].fillna("Unknown")

# print(db.model.unique())