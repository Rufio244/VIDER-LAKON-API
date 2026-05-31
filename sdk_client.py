# 🩸 VIDER LAKON • CLIENT SDK 📱
import requests

class ViderLakonApp:
    def __init__(self, server_url="http://localhost:7777"):
        self.url = server_url
        self.key = None
        self.user_id = None

    # 🆔 สมัคร/ล็อกอิน (สร้างตัวตนของแอปท่าน)
    def login(self, username: str):
        res = requests.post(f"{self.url}/register", json={"username": username}).json()
        self.key = res["api_key"]
        self.user_id = res["user_id"]
        print(f"🆔✅ เข้าสู่ระบบสำเร็จ | ID: {self.user_id}")
        return res

    # ✍️ เรียกสร้างเนื้อหา -> ดึงข้อมูลเข้าแอปท่าน 📥🧠
    def create(self, topic: str, desc: str, genre="ทั่วไป"):
        if not self.key: raise Exception("❌ กรุณา login ก่อน")
        res = requests.post(
            f"{self.url}/create",
            headers={"api-key": self.key},
            json={"topic": topic, "desc": desc, "genre": genre}
        ).json()
        return res

    # 🔱 ส่งข้อมูลจากแอปท่าน ไป SC 🚀🌌
    def send_to_sc(self, data: dict):
        if not self.key: raise Exception("❌ กรุณา login ก่อน")
        return requests.post(
            f"{self.url}/sync-to-sc",
            headers={"api-key": self.key},
            json={"data": data}
        ).json()

# 🔥 ตัวอย่างการนำไปใช้สร้างแอป 🩸📱
if __name__ == "__main__":
    # 1. สร้างแอปของเราเชื่อมต่อ VIDER
    my_app = ViderLakonApp(server_url="http://localhost:7777") # หรือใส่ IP จริง

    # 2. สมัครสมาชิก (ได้ไอดีเป็นของตัวเอง)
    me = my_app.login(username="USER_ONG")

    # 3. สั่ง VIDER LAKON สร้างงานให้ -> แล้วดึงมาโชว์ในแอปเรา
    work = my_app.create(
        topic = "ศึกเทพเจ้า",
        genre = "แฟนตาซี",
        desc = "ต่อสู้กันสนั่นจักรวาล พลังเทพสะท้านฟ้า"
    )

    # 📱✅ นี่คือสิ่งที่แอปท่านจะได้รับไปแสดงผล
    print("📖 ผลงานที่ได้รับ:\n", work["my_content"])

    # 🔱 ส่งต่อขึ้น SC
    sc_res = my_app.send_to_sc({"action": "READ_STORY", "id": work["content_id"]})
    print("🔱 ส่งไป SC แล้ว:", sc_res)
