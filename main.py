import time
print("🚀 تم تشغيل بوت طير شادي بنجاح!")
while True:
    print("✅ يجمع العملات الآن...")
    time.sleep(5)
nano tayrshadi_bot.py
import requests
import time
import random

WALLET_ADDRESS = "0x1f01bB5980BbA980462e4aC4AfC09Af0bAD3fB58"
INFURA_URL = "https://polygon-mainnet.infura.io/v3/3e3e109697b740b3b763ad06bbf4bbf5"

airdrops = [
    "https://zk-sync-airdrop.org/api/submit",
    "https://layerzero-drop.net/api/register",
    "https://freecrypto-airdrop.com/api/send",
    "https://cryptoearn.xyz/api/join",
]

headers = {
    "Content-Type": "application/json",
    "User-Agent": "TayrShadiBot/1.0"
}

def submit_airdrop(airdrop_url):
    data = {
        "wallet": WALLET_ADDRESS,
        "email": "mhmod093750@gmail.com"
    }
    try:
        response = requests.post(airdrop_url, json=data, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"✅ تم التسجيل بنجاح في {airdrop_url}")
        else:
            print(f"❌ فشل التسجيل في {airdrop_url} | الرمز: {response.status_code}")
    except Exception as e:
        print(f"⚠️ خطأ في الاتصال بـ {airdrop_url} | التفاصيل: {e}")

while True:
    for url in airdrops:
        submit_airdrop(url)
        time.sleep(5 + random.randint(1, 3))
