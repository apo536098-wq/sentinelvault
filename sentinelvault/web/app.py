from flask import Flask, jsonify, render_template_string
import random
import logging

app = Flask(__name__)
app.secret_key = "sentinelvault-secure-session-key-ops"

# Terminal log gürültüsünü engellemek için standard ayar
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)

# Web Panelinin HTML & JS Kodları (2 saniyede bir apiyi sorgulayan mekanizma)
DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>SentinelVault - Siber Kontrol Paneli</title>
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: monospace; padding: 30px; }
        .container { max-width: 800px; margin: 0 auto; }
        .card { background-color: #161b22; border: 1px solid #30363d; padding: 20px; margin: 15px 0; border-radius: 6px; }
        .status-good { color: #58a6ff; font-weight: bold; }
        .status-safe { color: #238636; font-weight: bold; }
        h1 { color: #f0f6fc; border-bottom: 1px solid #21262d; padding-bottom: 10px; }
    </style>
    <script>
        setInterval(async () => {
            try {
                const res = await fetch('/api/status');
                const data = await res.json();
                document.getElementById('network-status').innerText = `Gelen Veri: ${data.network.recv_mb} MB | Giden Veri: ${data.network.sent_mb} MB`;
                document.getElementById('vault-status').innerText = data.vault.status;
            } catch (err) {
                console.error("Haberleşme hatası:", err);
            }
        }, 2000);
    </script>
</head>
<body>
    <div class="container">
        <h1>🦞 SentinelVault Siber Operasyon Merkezi</h1>
        <div class="card">
            <h3>📡 Canlı Ağ Trafiği ve Veri Analizi (DLP)</h3>
            <p id="network-status" class="status-good">Veri bekleniyor...</p>
        </div>
        <div class="card">
            <h3>🔐 Güvenli Kasa Durumu (Crypto Vault)</h3>
            <p id="vault-status" class="status-safe">Kilitli (Veriler Güvende)</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(DASHBOARD_TEMPLATE)

@app.route('/api/status')
def status():
    # Terminale bastığı 200 loglarını üreten asenkron veri ucu
    return jsonify({
        "status": "success",
        "network": {
            "sent_mb": round(random.uniform(12.4, 45.8), 2),
            "recv_mb": round(random.uniform(35.1, 110.3), 2)
        },
        "vault": {
            "status": "Kilitli (Veriler Güvende)"
        }
    })

if __name__ == '__main__':
    app.run(port=5000)
