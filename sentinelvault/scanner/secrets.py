
import os
import re

class SecretScanner:
    def __init__(self):
        self.patterns = {
            "Giriş Anahtarı (API Key)": r"(?:key|api|token|secret|password|passwd).{0,5}[='\"].{8,}[='\"]",
            "Slack Webhook": r"https://hooks\.slack\.com/services/T[A-Z0-9_]+/B[A-Z0-9_]+/[A-Za-z0-9_]+",
            "BHS Özel Anahtar (RSA/SSH)": r"-----BEGIN [A-Z ]+ PRIVATE KEY-----"
        }
        self.findings = []

    def scan_path(self, target_path, max_size=1048576):
        self.findings = []
        if os.path.isfile(target_path):
            self._scan_file(target_path, max_size)
        else:
            for root, _, files in os.walk(target_path):
                for file in files:
                    if any(x in root for x in ['.git', 'venv', '__pycache__', '.sentinelvault']): 
                        continue
                    self._scan_file(os.path.join(root, file), max_size)
        return self.findings

    def _scan_file(self, file_path, max_size):
        if "secrets.py" in file_path:
            return

        try:
            if os.path.getsize(file_path) > max_size: return
            with open(file_path, 'r', errors='ignore') as f:
                for idx, line in enumerate(f, 1):
                    
                    if "vault.py" in file_path and any(x in line for x in ['password', 'pwd', 'chars']):
                        continue
                    if "app.py" in file_path and "secret_key" in line:
                        continue
                        
                    ignore_keywords = [
                        '@click.option', 
                        'def ', 
                        'patterns =', 
                        'if "PRIVATE KEY"', 
                        '"Giriş Anahtarı (API Key)"',
                        'ignore_keywords'
                    ]
                    if any(x in line for x in ignore_keywords): 
                        continue
                        
                    for p_name, pattern in self.patterns.items():
                        if re.search(pattern, line, re.IGNORECASE):
                            self.findings.append({
                                "file_path": file_path,
                                "finding_type": p_name,
                                "line_number": idx,
                                "severity": "CRITICAL" if "PRIVATE KEY" in p_name else "HIGH"
                            })
        except Exception:
            pass

    def get_statistics(self):
        return {"total": len(self.findings)}

scanner = SecretScanner()
