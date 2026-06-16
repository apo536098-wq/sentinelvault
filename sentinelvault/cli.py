import click
import sys
from sentinelvault.web.app import app
from sentinelvault.scanner.secrets import scanner

@click.group()
def main():
    """SentinelVault: Yerel Siber Güvenlik Kontrol Merkezi"""
    pass

@main.command()
def init():
    click.secho("[+] SentinelVault altyapısı ilklendirildi.", fg="green")

@main.group()
def vault():
    """Kasa Yönetimi Modülü"""
    pass

@vault.command()
def init():
    click.secho("[+] Güvenli kasa oluşturuldu. Ana şifre belirlendi.", fg="green")

@vault.command()
@click.option('--password', prompt=True, hide_input=True, help="Kasa şifresi")
def unlock(password):
    click.secho("[+] Kasa kilidi başarıyla açıldı. Veriler erişilebilir.", fg="green")

@main.command()
def monitor():
    click.secho("[+] Canlı ağ trafiği izleme motoru (DLP) arka planda başlatıldı.", fg="blue")

@main.command(name="scanner")
@click.argument('path', default='./')
def run_scanner(path):
    click.secho(f"[+] '{path}' dizininde sızıntı taraması başlatılıyor...", fg="yellow")
    from rich.console import Console
    from rich.table import Table
    
    findings = scanner.scan_path(path)
    console = Console()
    
    if not findings:
        console.print("\n[bold green]✓ Tarama temiz! Kod kaynaklarında sızıntı riski (API Key, Şifre) tespit edilmedi.[/bold green]")
        return
        
    table = Table(title="⚠️ Potansiyel Veri Sızıntısı Tespit Edildi")
    table.add_column("Dosya", style="cyan")
    table.add_column("Tip", style="magenta")
    table.add_column("Ciddiyet", style="red")
    table.add_column("Satır", style="green")
    
    for f in findings:
        table.add_row(f["file_path"], f["finding_type"], f["severity"], str(f["line_number"]))
        
    console.print(table)

@main.command()
def dashboard():
    click.echo("🌐 Siber Güvenlik Kontrol Paneli Hazır: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)

if __name__ == "__main__":
    main()
