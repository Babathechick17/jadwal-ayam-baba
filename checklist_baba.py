from datetime import datetime
import json

DATA_FILE = "data_baba.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def checklist_baba():
    today = datetime.now().strftime("%Y-%m-%d")

    checklist = {
        "tanggal": today,
        "nama": "Baba",
        "usia_minggu": 3.5,
        "fase": "Anak ayam (grower awal)",
        "kondisi": {
            "bulu_mulai_tumbuh": False,
            "mata_cerah": False,
            "nafsu_makan_baik": False,
            "aktif_dan_responsif": False,
            "tidak_diare": False,
            "kaki_kuat_dan_tegap": False,
            "tidak_ngorok": False
        },
        "lingkungan": {
            "suhu_cukup_hangat": False,
            "kandang_kering": False,
            "air_minum_bersih": False
        },
        "catatan": ""
    }

    data = load_data()
    data.append(checklist)
    save_data(data)

    print("Checklist Baba dibuat")

if __name__ == "__main__":
    checklist_baba()
