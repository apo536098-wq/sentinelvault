# 🦞 SentinelVault v1.0.0

SentinelVault, Kali Linux ortamları için geliştirilmiş, hem ofansif sızıntı taraması yapabilen hem de defansif veri güvenliği (DLP) sağlayan **Yerel Siber Güvenlik Kontrol Merkezi ve Akıllı Kasa** projesidir.

Proje; kriptografik şifre yönetimini, canlı ağ trafiği anomalilerini ve kaynak kod sızıntı analizlerini tek bir merkezden (CLI ve Web Dashboard) yönetmek üzere modüler olarak tasarlanmıştır.

---

## 🎯 Temel Özellikler & Çekirdek Motorlar

* **🔐 Secure Vault:** `cryptography` kütüphanesi kullanılarak AES-256 ile şifrelenmiş, terminal üzerinden kilitlenip açılabilen yerel veri kasası.
* **📡 Network Monitor:** Arka planda (`psutil`) asenkron olarak çalışan, canlı veri giriş-çıkış (Sent/Recv) trafiğini izleyen DLP motoru.
* **🛡️ Intrusion Guard:** Brute-force ve yetkisiz erişim denemelerini tespit ederek şüpheli IP'leri kara listeye alan savunma kalkanı.
* **⚠️ Secret Scanner:** Kod kaynaklarında unutulan API Key, Slack Webhook ve Özel Anahtarları avlayan, gelişmiş False-Positive (Yalancı Pozitif) filtre katmanına sahip statik analizör.
* **🌐 Cyber Dashboard:** Flask backend ve asenkron JavaScript mimarisiyle tarayıcı üzerinden canlı trafik ve tehdit analizi sunan karanlık temalı (`Dark Mode`) kontrol paneli.

---

## 📁 Proje Yapısı

```text
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
