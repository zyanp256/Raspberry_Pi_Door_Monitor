import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1453919789876514990/rGgw61H2umu0fdjhO_eUrAlj_AWi-OnLQR_bd4n7x0auruX2bgo34dTtnPIM1Vr_A9SI"

def send_output(message, ts):
    data = {
        "content": f"{message} | {ts}"
    }
    requests.post(WEBHOOK_URL, json=data)

