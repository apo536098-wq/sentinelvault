

readme_content = """<div align="center">

<img src="https://raw.githubusercontent.com/abdulkadirerkan/sentinelvault/main/assets/logo.png" width="120" alt="SentinelVault Logo">

# 🛡️ SentinelVault

### Yerel Siber Güvenlik Kontrol Merkezi & Akıllı Kasa

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" />
  <img src="https://img.shields.io/badge/AES--256-GCM-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

> **Kali Linux ortamları için geliştirilmiş, ofansif sızıntı taraması ve defansif veri güvenliği (DLP) yeteneklerini tek çatı altında birleştiren modüler siber güvenlik platformu.**

</div>

---

## 📸 Önizleme

```
┌─────────────────────────────────────────────────────────────┐
│  🛡️ SENTINELVAULT v1.0.0                                    │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │  🔐 VAULT   │  │ 📡 MONITOR  │  │ 🛡️ GUARD    │          │
│  │   Secure    │  │   Active    │  │   Alert     │          │
│  │   12 items  │  │  ↑ 2.4 MB/s │  │  0 threats  │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│                                                             │
│  ⚠️ Secret Scanner: 3 API keys detected in ./src          │
│  🌐 Dashboard: http://127.0.0.1:5000  [LIVE]               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ✨ Özellikler

<div align="center">

| 🔐 **Secure Vault** | 📡 **Network Monitor** | 🛡️ **Intrusion Guard** |
|:---|:---|:---|
| `cryptography` ile AES-256-GCM şifreleme | `psutil` ile asenkron canlı trafik izleme | Brute-force & yetkisiz erişim tespiti |
| Terminal tabanlı kilit/açma mekanizması | Gerçek zamanlı Sent/Recv analizi | Otomatik IP kara listeleme |

| ⚠️ **Secret Scanner** | 🌐 **Cyber Dashboard** |
|:---|:---|
| API Key, Slack Webhook, Private Key avlama | Flask + async JS mimarisi |
| Gelişmiş False-Positive filtre katmanı | Karanlık tema, canlı tehdit analizi |

</div>

---

## 🏗️ Mimari

```
                    ┌─────────────────┐
                    │   SentinelVault │
                    │     (CLI/API)   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  🔐 Crypto    │    │  📡 Monitor   │    │  🛡️ Guard     │
│   Engine      │    │   Network     │    │   Intrusion   │
│  (AES-256)    │    │   (psutil)    │    │   Detection   │
└───────────────┘    └───────────────┘    └───────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────┴────────┐
                    │  🌐 Dashboard   │
                    │  (Flask + JS)   │
                    └─────────────────┘
```

---

## 📁 Proje Yapısı

```
sentinelvault/
│
├── sentinelvault/
│   ├── __init__.py
│   ├── cli.py                    # Ana CLI (Click)
│   │
│   ├── core/
│   │   ├── config.py             # Sistem konfigürasyonu
│   │   └── database.py           # SQLite veritabanı katmanı
│   │
│   ├── crypto/
│   │   ├── engine.py             # AES-256-GCM kriptografi motoru
│   │   └── vault.py              # Kasa mantığı & şifre yönetimi
│   │
│   ├── guard/
│   │   └── intrusion.py          # Sızma engelleme & IP bloklama
│   │
│   ├── monitor/
│   │   └── network.py            # Canlı ağ trafiği izleme (async)
│   │
│   ├── scanner/
│   │   └── secrets.py            # Statik kod analizi & sızıntı tarayıcı
│   │
│   └── web/
│       ├── app.py                # Flask API & sunucu
│       └── templates/
│           └── dashboard.html      # Dark mode operasyon paneli
│
├── setup.py                      # Pip kurulum & entry points
├── requirements.txt              # Bağımlılıklar
└── .gitignore                    # Güvenli git muafiyet listesi
```

---

## 🚀 Kurulum

> **⚠️ Kali Linux'ta PEP 668 koruması aktiftir. Sanal ortam kullanımı zorunludur.**

```bash
# 1. Depoyu klonlayın
git clone https://github.com/kullaniciadi/sentinelvault.git
cd sentinelvault

# 2. Sanal ortam oluşturun ve aktifleştirin
python3 -m venv venv
source venv/bin/activate

# 3. Projeyi kurun
pip install -e .
```

---

## 💻 Kullanım

```bash
# Altyapıyı ilklendirin
sentinelvault init

# Kasa oluşturun ve master şifrenizi belirleyin
sentinelvault vault init

# Canlı ağ izleme motorunu başlatın
sentinelvault monitor start

# Kaynak kod sızıntı taraması (rekürsif)
sentinelvault scanner run ./proje-dizini

# Web operasyon merkezini canlıya alın
sentinelvault dashboard
```

> 🌐 **Dashboard:** `http://127.0.0.1:5000`

---

## 🛠️ Teknik Detaylar

| Bileşen | Teknoloji | Versiyon |
|:---|:---|:---|
| Şifreleme | `cryptography` (AES-256-GCM) | ≥ 3.4 |
| CLI Framework | `Click` | ≥ 8.0 |
| Web Framework | `Flask` | ≥ 2.0 |
| Ağ İzleme | `psutil` | ≥ 5.9 |
| Veritabanı | `SQLite3` | Built-in |
| Async | `asyncio` | Built-in |

---

## 🧪 Komut Referansı

| Komut | Açıklama |
|:---|:---|
| `sentinelvault init` | Altyapıyı ilklendirir (DB, log dizinleri) |
| `sentinelvault vault init` | Yeni şifreli kasa oluşturur |
| `sentinelvault vault unlock` | Kasayı açar |
| `sentinelvault monitor start` | Ağ izleme motorunu başlatır |
| `sentinelvault monitor status` | İzleme durumunu gösterir |
| `sentinelvault scanner run <path>` | Dizinde sızıntı taraması yapar |
| `sentinelvault dashboard` | Web panelini başlatır |
| `sentinelvault --version` | Versiyon bilgisi |

---

## 👤 Geliştirici

<div align="center">

**Abdulkadir Erkan**

*Siber Güvenlik Teknolojisi Bölümü — Bitirme Projesi*

</div>

---

<div align="center">

> *"Güvenlik bir ürün değil, süreçtir."*

**[⬆ Yukarı Git](#)** | 🌟 Yıldız ver | 🍴 Forkla

</div>
"""

with open('/mnt/agents/output/README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md oluşturuldu!")
print(f"Dosya boyutu: {len(readme_content)} karakter")
