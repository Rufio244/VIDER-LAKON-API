# 🩸 DATABASE • SIMPLE 🩸
users_db = {}       # เก็บข้อมูลผู้ใช้
contents_db = {}    # เก็บผลงาน

# 🆔 สร้างผู้ใช้ใหม่
def create_user(username: str, app_id: str):
    import uuid
    user_id = f"VL_{uuid.uuid4().hex[:8]}"
    api_key = f"KEY_{uuid.uuid4().hex[:12]}"
    users_db[user_id] = {
        "id": user_id, "user": username, "app": app_id,
        "key": api_key, "space": [] # 📦 พื้นที่ส่วนตัว
    }
    return {"user_id": user_id, "api_key": api_key}

# 🔍 หาผู้ใช้จาก API KEY
def get_user_by_key(api_key: str):
    for u in users_db.values():
        if u["key"] == api_key: return u
    return None

# 💾 บันทึกผลงานลงพื้นที่ส่วนตัว
def save_content(user, data):
    import uuid
    cid = f"CON_{uuid.uuid4().hex[:6]}"
    contents_db[cid] = data
    user["space"].append(cid)
    return cid
