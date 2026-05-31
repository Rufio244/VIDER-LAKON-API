# 🩸 VIDER LAKON API • SUPER SIMPLE VERSION 🩸👑
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import database as db
from sc_bridge import send_to_sc

# 🚀 เริ่มระบบ
app = FastAPI(title="VIDER LAKON 🩸", version="3.0-SIMPLE")

# 🛡️ ตรวจสอบสิทธิ์
async def get_current_user(api_key: Optional[str] = None):
    if not api_key: raise HTTPException(401, "❌ กรุณาส่ง API Key")
    user = db.get_user_by_key(api_key)
    if not user: raise HTTPException(403, "❌ Key ไม่ถูกต้อง")
    return user

# 📥 โครงสร้างข้อมูล
class RegisterData(BaseModel): username: str; app_id: str = "MY_APP"
class CreateData(BaseModel): topic: str; desc: str; genre: str = "ทั่วไป"

# 📝 1. สมัครสมาชิก -> ได้ไอดี+คีย์ส่วนตัว 🆔✅
@app.post("/register", summary="🆔 สมัครใช้งาน")
def register(data: RegisterData):
    return db.create_user(data.username, data.app_id)

# ✍️ 2. สร้างผลงานด้วยพลัง VIDER LAKON 🧠🔥
@app.post("/create", summary="✍️ สร้างเนื้อหา")
def create_content(data: CreateData, user = Depends(get_current_user)):
    # 🩸 สมอง VIDER LAKON ประมวลผล (ย่อๆ)
    result_text = f"""
📝 [ผลงานจาก VIDER LAKON 🩸]
📌 หัวข้อ: {data.topic}
🎯 แนว: {data.genre}
📖 เนื้อหา: {data.desc}
✨ สร้างโดย: {user['user']} | ระบบ: VIDER LAKON
    """.strip()

    # 💾 บันทึกลงพื้นที่ส่วนตัว
    cid = db.save_content(user, {**data.dict(), "result": result_text})

    # 🔱 ส่งขึ้น SC ทันที
    return {
        "ok": True,
        "content_id": cid,
        "my_content": result_text,
        "saved_in": f"SPACE_{user['id']} 🧱"
    }

# 🔱 3. สั่งซิงค์ข้อมูลไป SC 🚀🌌
@app.post("/sync-to-sc", summary="🔱 ส่งข้อมูลขึ้น SC")
async def sync_sc(data: dict, user = Depends(get_current_user)):
    res = await send_to_sc(data, user["id"])
    return res

# 👤 4. ดูข้อมูลส่วนตัว 🧱
@app.get("/my-space")
def my_space(user = Depends(get_current_user)):
    return {"my_id": user["id"], "my_works": user["space"]}

# 🚀 RUN SERVER
if __name__ == "__main__":
    import uvicorn
    print("🩸🔥 VIDER LAKON ONLINE :7777 🚀")
    uvicorn.run("main:app", host="0.0.0.0", port=7777, reload=True)
