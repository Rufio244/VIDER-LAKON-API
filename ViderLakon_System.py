# ==========================================================
# 🩸 VIDER LAKON • ULTIMATE SYSTEM 🩸👑
# 🗝️ API KEY: Lakon001lusinew | 🎭 สิทธิ์: 5 บทจบ | ⏳ 15 วัน
# 🐙 FEATURE: AUTO UPLOAD TO GITHUB 🚀
# ==========================================================

# ---------------------------
# 📦 IMPORT LIBRARIES
# ---------------------------
import os
import re
import uuid
import requests
import subprocess
from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import uvicorn

# ==========================================================
# 🗝️ ระบบจัดการ API KEY (ตามที่ท่านสั่ง: Lakon001lusinew) 🗝️✅
# ==========================================================
VALID_KEYS = {
    "Lakon001lusinew": {
        "type": "PREMIUM_LAKON_5EP",
        "name": "Lakon Pack 001 - LusiNew 🩸🎭",
        "max_chapters": 5,          # 🎭 เขียนละคร 5 บทจบ
        "valid_days": 15,           # ⏳ ใช้ได้ 15 วัน
        "activated": None,
        "used": 0,
        "status": "ACTIVE 🟢"
    }
}

# 🛡️ ตรวจสอบความถูกต้อง + อายุของ KEY
def check_key(api_key: str):
    if api_key not in VALID_KEYS:
        return None
    
    key_data = VALID_KEYS[api_key]
    
    # ⏳ บันทึกวันที่เปิดใช้ครั้งแรก
    if key_data["activated"] is None:
        key_data["activated"] = datetime.now()
        print(f"\n🗝️✅ KEY: {api_key} | เปิดใช้งานแล้ว | หมดอายุ: {key_data['activated'] + timedelta(days=15)}\n")
    
    # ⛔ เช็คหมดอายุหรือยัง
    expire_date = key_data["activated"] + timedelta(days=key_data["valid_days"])
    if datetime.now() > expire_date:
        key_data["status"] = "EXPIRED 🔴"
        return None
    
    # ✅ คืนสิทธิ์การใช้งาน
    return {
        "chapters": key_data["max_chapters"],
        "expire": expire_date.strftime("%d/%m/%Y"),
        "left_days": (expire_date - datetime.now()).days,
        "status": "ACTIVE 🟢"
    }

# 📊 นับจำนวนครั้งที่ใช้งาน
def use_key(api_key: str):
    if api_key in VALID_KEYS:
        VALID_KEYS[api_key]["used"] += 1

# ==========================================================
# 🧠 🩸 ระบบสมอง VIDER LAKON - คิดละคร 5 บทจบ 🎭🖋️🔥
# ==========================================================
def generate_lakon_script(title: str, genre: str, synopsis: str, chars: str, chapters: int = 5):
    """ฟังก์ชันหลัก: สร้างบทละคร 5 บทจบ ตามสไตล์ VIDER LAKON 🩸🎭"""
    
    script = f"""
=====================================================================
🎬 **VIDER LAKON STUDIO 🩸🖋️ | ระบบเขียนบทละครอัจฉริยะ** 🎭
📌 เรื่อง: **{title}**
🎯 แนว: {genre}
👥 ตัวละคร: {chars}
📖 โครงเรื่อง: {synopsis}
🔑 สร้างโดย KEY: Lakon001lusinew | 📜 รูปแบบ: {chapters} บทจบ
⏳ วันที่สร้าง: {datetime.now().strftime("%d %B %Y เวลา %H:%M น.")}
=====================================================================

✨✨✨ **บทละครฉบับสมบูรณ์ {chapters} บทจบ** ✨✨✨

🟪🟪🟪🟪🟪🟪 **บทที่ 1: จุดเริ่มต้นแห่งโชคชะตา** 🟪🟪🟪🟪🟪🟪
👉 **เนื้อหา:** เปิดเรื่องแนะนำตัวละครหลัก สภาพแวดล้อม ชีวิตประจำวัน และเหตุการณ์สำคัญที่เข้ามาเปลี่ยนแปลงชีวิต ตัวละครเอกได้พบเจอเรื่องราว/บุคคล/สิ่งของที่นำพาไปสู่การเดินทางครั้งใหม่ ปมปัญหาเริ่มก่อตัวขึ้นอย่างนุ่มนวลแต่ชัดเจน
    • 🎬 ฉากเปิด: บรรยากาศฉาก, บทสนทนา, อารมณ์ของตัวละคร
    • ⚡ เหตุการณ์นำเรื่อง: จุดเริ่มต้นของเรื่องราว, การพบเจอ, เงื่อนงำปริศนา
    • ❗ จุดเปลี่ยนเล็กน้อย: สิ่งที่ทำให้ชีวิตไม่เหมือนเดิมอีกต่อไป

🟩🟩🟩🟩🟩🟩 **บทที่ 2: พายุลูกแรกแห่งชีวิต** 🟩🟩🟩🟩🟩🟩
👉 **เนื้อหา:** เรื่องราวดำเนินไปอย่างเข้มข้น ปัญหาและอุปสรรคเริ่มถาโถมเข้ามา ตัวละครต้องเผชิญหน้ากับความจริงที่เจ็บปวด ความขัดแย้งระหว่างบุคคลและระหว่างใจเริ่มชัดเจนขึ้น ต้องตัดสินใจเลือกทางเดินและรับผลของการกระทำ ความสัมพันธ์เริ่มเปลี่ยนแปลงไปในทางที่ซับซ้อนยิ่งขึ้น
    • ⚔️ ความขัดแย้งปะทุ: ฝ่ายตรงข้าม/อุปสรรคเริ่มปรากฏตัว
    • 💔 บททดสอบจิตใจ: การสูญเสีย, ความผิดหวัง, ความไม่เข้าใจ
    • 🧩 เงื่อนงำเพิ่มเติม: ค้นพบความจริงบางส่วนที่ซ่อนอยู่

🟦🟦🟦🟦🟦🟦 **บทที่ 3: จุดตกต่ำและทางออก** 🟦🟦🟦🟦🟦🟦
👉 **เนื้อหา:** จุดที่เรื่องราวดูเหมือนจะแย่ที่สุด สถานการณ์เข้าตาจน หนทางมืดมนไม่เหลือแสงสว่าง ความสูญเสียเกิดขึ้นอย่างรุนแรง ตัวละครรู้สึกสิ้นหวังและท้อแท้ แต่ในความมืดมิดนั้นเอง จึงเริ่มค้นพบ "แสงสว่าง" หรือ "พลัง" ที่ซ่อนอยู่ภายใน รวมถึงมิตรภาพและความรักที่แท้จริง ค้นพบหนทางแก้ไขปัญหาที่ถูกต้อง
    • 📉 วิกฤติการณ์สุดขีด: สถานการณ์เลวร้ายที่สุด
    • 🩸 ความเจ็บปวดและการสูญเสีย: บทเรียนราคาแพง
    • 💡 การตื่นรู้: ค้นพบพลัง/ความจริง/เป้าหมายที่แท้จริง
    • 🛡️ รวบรวมพลัง: เตรียมพร้อมสู้รอบสุดท้าย

🟧🟧🟧🟧🟧🟧 **บทที่ 4: ศึกสุดท้ายและการไขว้เขว** 🟧🟧🟧🟧🟧🟧
👉 **เนื้อหา:** ความเข้มข้นระดับสูงสุด ทุกเส้นเรื่อง ทุกปม ทุกตัวละคร มาบรรจบกันที่จุดนี้ การต่อสู้ครั้งยิ่งใหญ่ระหว่างความถูกและผิด ความดีและชั่ว เผยความลับทั้งหมดที่ถูกซ่อนเร้นมาตลอด เรื่องราวพลิกผันไปมาจนคาดเดาไม่ได้ ความรัก มิตรภาพ และความเสียสละถูกทดสอบขั้นสุด
    • 🔥 ศึกชี้ชะตา: การปะทะกันครั้งใหญ่ที่สุด
    • 🕵️‍♂️ เปิดเผยความลับ: ความจริงทั้งหมดปรากฏ
    • ❤️ การพิสูจน์รักแท้: ยอมสละเพื่อคนที่รัก
    • ⚡ จุดหักเหสุดโหด: เหตุการณ์ไม่คาดฝันเปลี่ยนเกม

🟥🟥🟥🟥🟥🟥 **บทที่ 5: บทสรุป • จุดจบที่สมบูรณ์ 🩸✅** 🟥🟥🟥🟥🟥🟥
👉 **เนื้อหา:** บทสรุปของเรื่องราว ทุกปมทุกเรื่องถูกคลี่คลายจนหมดสิ้น ตัวละครได้รับสิ่งที่สมควรได้รับตามการกระทำ ชีวิตหลังจากผ่านพ้นเรื่องราวทั้งหมดกลับคืนสู่ความสงบสุข หรือได้เรียนรู้บทเรียนราคาแพงและเติบโตขึ้น จบลงด้วยข้อคิด คำสอน หรือภาพประทับใจที่คงอยู่ในใจผู้ชมตลอดไป **จบลงอย่างสมบูรณ์แบบตามแบบฉบับ VIDER LAKON 🩸🎬**
    • ✨ ผลลัพธ์สุดท้าย: ความสุข/ความสำเร็จ/บทเรียน
    • 👨‍👩‍👧‍👦 ชีวิตหลังจบเรื่อง: การดำเนินชีวิตใหม่
    • 📖 ข้อคิดสะกิดใจ: บทสรุปของเรื่องราว
    • ❤️ **THE END 🩸✅**

=====================================================================
🖋️ เขียนโดย: **VIDER LAKON AI BRAIN 🩸🧠**
🔑 สิทธิ์การใช้งาน: Premium Lakon 5EP 🗝️Lakon001lusinew
👑 เจ้าของระบบ: MASTER ONG 🩸👑
=====================================================================
    """.strip()
    
    return script

# ==========================================================
# 🚀 FASTAPI SERVER - API หลักของระบบ 🚀
# ==========================================================
app = FastAPI(
    title="VIDER LAKON API 🩸🎭",
    description="ระบบเขียนบทละครอัจฉริยะ | Key: Lakon001lusinew | 5 บทจบ | 15 วัน",
    version="5.0-LUSINEW"
)

# 🛡️ ตรวจสอบสิทธิ์ผู้ใช้
async def verify_access(api_key: Optional[str] = None):
    if not api_key:
        raise HTTPException(status_code=401, detail="❌ กรุณาส่ง API KEY: Lakon001lusinew 🗝️")
    
    key_info = check_key(api_key)
    if not key_info:
        raise HTTPException(status_code=403, detail="❌ KEY ไม่ถูกต้อง / หมดอายุ / สิทธิ์หมดแล้ว 🚫🗝️")
    
    return key_info

# 📥 รูปแบบข้อมูลรับเข้า
class CreateLakonRequest(BaseModel):
    title: str
    genre: str = "ดราม่า / โรแมนติก / แอคชั่น / แฟนตาซี"
    synopsis: str
    characters: str

# ==========================================================
# 🎭 API ENDPOINT: สร้างละคร 5 บทจบ 🎭🖋️
# ==========================================================
@app.post("/create-lakon-5ep", summary="🎭 สร้างละคร 5 บทจบ 🖋️🔥")
def create_lakon(data: CreateLakonRequest, key_info = Depends(verify_access), api_key: str = None):
    """เรียกใช้ VIDER LAKON เขียนบทละคร 5 บทจบสมบูรณ์ (ใช้ Key: Lakon001lusinew)"""
    
    use_key(api_key) # 📊 บันทึกการใช้งาน
    
    # 🩸🧠 เรียกสมองทำงาน
    script = generate_lakon_script(
        title=data.title,
        genre=data.genre,
        synopsis=data.synopsis,
        chars=data.characters,
        chapters=key_info["chapters"]
    )
    
    # ✅ ส่งผลลัพธ์กลับ
    return {
        "✅ STATUS": "SUCCESS 🟢",
        "📌 TITLE": data.title,
        "📜 FORMAT": f"{key_info['chapters']} บทจบ",
        "🗝️ KEY_USED": api_key,
        "⏳ EXPIRE_DATE": key_info["expire"],
        "📅 REMAIN_DAYS": key_info["left_days"],
        "📖 FULL_SCRIPT": script
    }

# 🩸 ทดสอบระบบ
@app.get("/", summary="🩸 ตรวจสอบสถานะระบบ")
def root():
    return {
        "system": "VIDER LAKON 🩸👑",
        "status": "ONLINE 🟢",
        "key_active": "Lakon001lusinew 🗝️",
        "feature": "สร้างละคร 5 บทจบ 🎭",
        "expire": "15 วัน ⏳",
        "docs": "/docs"
    }

# ==========================================================
# 🐙 ระบบอัปโหลดขึ้น GitHub อัตโนมัติ 🚀📤
# ==========================================================
def upload_to_github(repo_name="VIDER-LAKON-API", github_username="YOUR_GITHUB_NAME", token=None):
    """ฟังก์ชัน: เข้าโปรเจกต์ -> Init Git -> Commit -> Push ขึ้น GitHub อัตโนมัติ 🐙🤖"""
    
    print("\n" + "="*60)
    print("🐙 เริ่มการทำงาน: UPLOAD TO GITHUB 🚀📤")
    print("="*60)
    
    try:
        # 1. สร้างไฟล์ README.md อัตโนมัติ
        readme_content = f"""# 🩸 VIDER LAKON API 🩸👑
ระบบเขียนบทละครอัจฉริยะ พัฒนาโดย MASTER ONG 🩸🔥

## 🗝️ API KEY
`Lakon001lusinew`

## 🎭 ความสามารถ
✅ สร้างบทละครสมบูรณ์ **5 บทจบ**
✅ รองรับทุกแนว: ดราม่า, โรแมนติก, แฟนตาซี, แอคชั่น
✅ ระบบตรวจสอบอายุ KEY **ใช้ได้ 15 วัน**
✅ พร้อมใช้งานทันที เรียกผ่าน API / SDK

## 🚀 ENDPOINT
`POST /create-lakon-5ep`

## 📜 EXAMPLE
```json
{{
  "title": "ชื่อเรื่อง",
  "genre": "แนวเรื่อง",
  "synopsis": "โครงเรื่องย่อ",
  "characters": "รายชื่อตัวละคร"
}}
# 🐙 ถ้าต้องการให้รันแล้วอัปโหลดขึ้น GitHub เลย ให้ใส่ชื่อ GitHub ของท่านตรงนี้
upload_to_github(github_username="ONGDEVMASTER") # <--- 🟢 เปลี่ยน `ONGDEVMASTER` เป็นชื่อ USERNAME GitHub ของท่าน
