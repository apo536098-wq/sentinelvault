SentinelVault v1.0.0
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux-black?style=flat-square&logo=linux" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Crypto-AES--256-red?style=flat-square" />
</p>
Kali Linux ortamları için geliştirilmiş, ofansif sızıntı taraması ve defansif veri güvenliği (DLP) yeteneklerini tek çatı altında birleştiren Yerel Siber Güvenlik Kontrol Merkezi ve Akıllı Kasa.
SentinelVault; kriptografik şifre yönetimini, canlı ağ trafiği anomalilerini ve kaynak kod sızıntı analizlerini modüler bir mimariyle tek merkezden (CLI + Web Dashboard) yönetmenizi sağlar.
🎯 Mimari & Çekirdek Motorlar
Table
Modül	Teknoloji	Görev
🔐 Secure Vault	cryptography (AES-256-GCM)	Yerel şifrelenmiş veri kasası, master key ile kilit/açma
📡 Network Monitor	psutil + async I/O	Canlı giriş-çıkış trafiği izleme, anomali tespiti
🛡️ Intrusion Guard	IPTables / socket + regex	Brute-force & yetkisiz erişim algılama, otomatik IP kara listeleme
⚠️ Secret Scanner	Özel regex motoru + FP filtre	API Key, Slack Webhook, Private Key avlama, yalancı pozitif önleme
🌐 Cyber Dashboard	Flask + async JS (WebSocket)	Karanlık temalı, gerçek zamanlı tehdit ve trafik görselleştirme
📁 Proje Yapısı
plain
sentinelvault/
├── sentinelvault/
│   ├── __init__.py
│   ├── cli.py                    # Ana CLI (Click framework)
│   ├── core/
│   │   ├── config.py             # Sistem konfigürasyonu
│   │   └── database.py           # SQLite ORM katmanı
│   ├── crypto/
│   │   ├── engine.py             # AES-256-GCM kriptografi motoru
│   │   └── vault.py              # Kasa mantığı & şifre yönetimi
│   ├── guard/
│   │   └── intrusion.py          # Sızma engelleme & IP bloklama
│   ├── monitor/
│   │   └── network.py            # Canlı ağ trafiği izleme (async)
│   ├── scanner/
│   │   └── secrets.py            # Statik kod analizi & sızıntı tarayıcı
│   └── web/
│       ├── app.py                # Flask API & sunucu
│       └── templates/
│           └── dashboard.html    # Dark mode operasyon paneli
├── setup.py                      # Pip kurulum & entry points
├── requirements.txt              # Bağımlılıklar
└── .gitignore                    # Güvenli git muafiyet listesi
🚀 Kurulum & Kali Entegrasyonu
Not: Kali Linux'ta PEP 668 koruması aktiftir. Sanal ortam kullanımı zorunludur.
bash
# 1. Depoyu klonlayın
git clone https://github.com/kullaniciadi/sentinelvault.git
cd sentinelvault

# 2. Sanal ortam oluşturun
python3 -m venv venv
source venv/bin/activate

# 3. Bağımlılıkları yükleyin ve projeyi global komut olarak bağlayın
pip install -e .
💻 Operasyonel Kullanım (CLI)
bash
# Altyapıyı ilklendirin (veritabanı, log dizinleri)
sentinelvault init

# Kasa oluşturun ve master şifrenizi belirleyin
sentinelvault vault init

# Canlı ağ izleme motorunu arka planda başlatın
sentinelvault monitor start

# Kaynak kod sızıntı taraması (rekürsif)
sentinelvault scanner run ./proje-dizini

# Web operasyon merkezini canlıya alın
sentinelvault dashboard
Dashboard'a erişim: Tarayıcınızdan http://127.0.0.1:5000 adresine gidin.
🔧 Geliştirici Bilgisi
Table
Geliştirici	Abdulkadir Erkan
Bölüm	Siber Güvenlik Teknolojisi
Proje Türü	Bitirme Projesi
Lisans	MIT
"Güvenlik bir ürün değil, süreçtir." — SentinelVault felsefesi
İstersen aşağıdaki eklemeleri de yapabilirim:
📸 Ekran görüntüleri / GIF'ler için yer tutucular
🔬 API endpoint dokümantasyonu
🧪 Unit test komutları
🐳 Docker desteği talimatları
📊 Mimari diyagram (ASCII veya Mermaid)
Ne eklemek istersin?
H daha gúzenli halde ver
Edit
Copy
Share
İşte SentinelVault için çok daha etkileyici, profesyonel ve görsel ağırlıklı bir README:
<div align="center">
🛡️ SentinelVault
Yerel Siber Güvenlik Kontrol Merkezi & Akıllı Kasa
<p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" />
  <img src="https://img.shields.io/badge/AES--256-GCM-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>
Kali Linux ortamları için geliştirilmiş, ofansif sızıntı taraması ve defansif veri güvenliği (DLP) yeteneklerini tek çatı altında birleştiren modüler siber güvenlik platformu.
</div>
📸 Önizleme
plain
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
✨ Özellikler
<div align="center">
Table
🔐 Secure Vault	📡 Network Monitor	🛡️ Intrusion Guard
cryptography ile AES-256-GCM şifreleme	psutil ile asenkron canlı trafik izleme	Brute-force & yetkisiz erişim tespiti
Terminal tabanlı kilit/açma mekanizması	Gerçek zamanlı Sent/Recv analizi	Otomatik IP kara listeleme
Table
⚠️ Secret Scanner	🌐 Cyber Dashboard
API Key, Slack Webhook, Private Key avlama	Flask + async JS mimarisi
Gelişmiş False-Positive filtre katmanı	Karanlık tema, canlı tehdit analizi
</div>
🏗️ Mimari
plain
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
📁 Proje Yapısı
plain
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
🚀 Kurulum
⚠️ Kali Linux'ta PEP 668 koruması aktiftir. Sanal ortam kullanımı zorunludur.
bash
# 1. Depoyu klonlayın
git clone https://github.com/kullaniciadi/sentinelvault.git
cd sentinelvault

# 2. Sanal ortam oluşturun ve aktifleştirin
python3 -m venv venv
source venv/bin/activate

# 3. Projeyi kurun
pip install -e .
💻 Kullanım
bash
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
🌐 Dashboard: http://127.0.0.1:5000
🛠️ Teknik Detaylar
Table
Bileşen	Teknoloji	Versiyon
Şifreleme	cryptography (AES-256-GCM)	≥ 3.4
CLI Framework	Click	≥ 8.0
Web Framework	Flask	≥ 2.0
Ağ İzleme	psutil	≥ 5.9
Veritabanı	SQLite3	Built-in
Async	asyncio	Built-in
🧪 Komut Referansı
Table
Komut	Açıklama
sentinelvault init	Altyapıyı ilklendirir (DB, log dizinleri)
sentinelvault vault init	Yeni şifreli kasa oluşturur
sentinelvault vault unlock	Kasayı açar
sentinelvault monitor start	Ağ izleme motorunu başlatır
sentinelvault monitor status	İzleme durumunu gösterir
sentinelvault scanner run <path>	Dizinde sızıntı taraması yapar
sentinelvault dashboard	Web panelini başlatır
sentinelvault --version	Versiyon bilgisi
👤 Geliştirici
<div align="center">
Abdulkadir Erkan
Siber Güvenlik Teknolojisi Bölümü — Bitirme Projesi
</div>
<div align="center">
"Güvenlik bir ürün değil, süreçtir."
⬆ Yukarı Git | 🌟 Yıldız ver | 🍴 Forkla
</div>
