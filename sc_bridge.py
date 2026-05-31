# 🩸 SC • STEPHEN • CHANI BRIDGE • SIMPLE 🩸
import os
import aiohttp
from dotenv import load_dotenv
load_dotenv()

SC_ENDPOINT = os.getenv("SC_URL", "wss://stephen-chani.io/gateway")
SC_KEY = os.getenv("SC_KEY", "SC_MASTER_777")

# 🚀 ส่งข้อมูลขึ้นระบบแม่
async def send_to_sc(data: dict, user_id: str):
    payload = {
        "from": "VIDER_LAKON", "user": user_id,
        "data": data, "timestamp": __import__("time").time()
    }
    try:
        async with aiohttp.ClientSession() as s:
            async with s.post(f"{SC_ENDPOINT}/send", json=payload,
                              headers={"X-SC-KEY": SC_KEY}) as r:
                return {"synced": True, "sc_status": r.status}
    except:
        return {"synced": False, "note": "SC Offline 🟡"}
