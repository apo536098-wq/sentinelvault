# 🦞SentinelVault v1.0.0
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
Modül
Teknoloji
Görev
🔐 Secure Vault
 cryptography  (AES-256-GCM)
Yerel şifrelenmiş veri kasası, master key ile kilit/açma
📡 Network Monitor
 psutil  + async I/O
Canlı giriş-çıkış trafiği izleme, anomali tespiti
🛡️ Intrusion Guard
IPTables /  socket  + regex
Brute-force & yetkisiz erişim algılama, otomatik IP kara listeleme
⚠️ Secret Scanner
Özel regex motoru + FP filtre
API Key, Slack Webhook, Private Key avlama, yalancı pozitif önleme
🌐 Cyber Dashboard
Flask + async JS (WebSocket)
Karanlık temalı, gerçek zamanlı tehdit ve trafik görselleştirme
📁 Proje Yapısı
sentinelvault/
├── sentinelvault/
│   ├── __init__.py
│   ├── cli.py               # Ana Komut Satırı Arayüzü (Click)
│   ├── core/
│   │   ├── config.py        # Sistem Konfigürasyonu
│   │   └── database.py      # SQLite Veritabanı Katmanı
│   ├── crypto/
│   │   ├── engine.py        # Kriptografi Motoru (AES-256)
│   │   └── vault.py         # Kasa Mantığı ve Şifre Yönetimi
│   ├── guard/
│   │   └── intrusion.py     # Sızma Engelleme ve IP Bloklama
│   ├── monitor/
│   │   └── network.py       # Canlı Ağ Trafiği İzleme
│   ├── scanner/
│   │   └── secrets.py       # Kod İçi Sızıntı Tarayıcı (Regex)
│   └── web/
│       ├── app.py           # Flask Web Sunucusu & API
│       └── templates/
│           └── dashboard.html # Siber Görsel Kontrol Paneli
├── setup.py                 # Sistem Entegrasyon Dosyası
└── .gitignore               # Güvenli Git Muafiyet Listesi

🚀 Kurulum ve Kali Entegrasyonu
Projenin kurulacağı dizine gidin ve Kali'nin Python korumasını (PEP 668) izole etmek için bir sanal ortam oluşturup aktifleştirin:

Bash
# Sanal ortamı kurun ve içine girin
python3 -m venv venv
source venv/bin/activate

# Projeyi sisteme küresel (global) bir komut olarak bağlayın
pip install -e .

💻 Operasyonel Kullanım (CLI Commands)
SentinelVault kurulduktan sonra terminalde doğrudan aşağıdaki komutlarla tetiklenebilir:

Bash
# 1. Altyapıyı ilklendirin
sentinelvault init

# 2. Kasayı oluşturun ve ana şifrenizi belirleyin
sentinelvault vault init

# 3. Canlı ağ izleme motorunu arka planda ateşleyin
sentinelvault monitor start

# 4. Kaynak kod sızıntı taramasını başlatın
sentinelvault scanner run ./

# 5. Görsel web panelini canlıya alın
sentinelvault dashboard
Sistem ayağa kalktıktan sonra tarayıcınızdan http://127.0.0.1:5000 adresine giderek siber operasyon merkezine erişebilirsiniz.

⚡ Geliştirici: Abdulkadir Erkan - Siber Güvenlik Teknolojisi Bölümü Projesi
