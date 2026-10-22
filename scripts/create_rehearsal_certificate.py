"""Generate a local-only CA and leaf; never install a trust-store certificate."""
import ipaddress
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID

folder = Path(sys.argv[1]).resolve()
if not folder.is_dir() or any((folder / name).exists() for name in ("ca.pem", "server.pem", "server-key.pem")):
    raise SystemExit("Expected existing empty certificate destination")
now = datetime.now(timezone.utc)
ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "CPA B024 local rehearsal CA")])
ca = (x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(ca_key.public_key())
      .serial_number(x509.random_serial_number()).not_valid_before(now-timedelta(minutes=5)).not_valid_after(now+timedelta(days=7))
      .add_extension(x509.BasicConstraints(ca=True,path_length=0),critical=True)
      .add_extension(x509.KeyUsage(digital_signature=True,key_encipherment=False,key_cert_sign=True,crl_sign=True,
                                  content_commitment=False,data_encipherment=False,key_agreement=False,encipher_only=False,decipher_only=False),critical=True)
      .sign(ca_key, hashes.SHA256()))
key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
leaf = (x509.CertificateBuilder().subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME,"127.0.0.1")]))
        .issuer_name(ca.subject).public_key(key.public_key()).serial_number(x509.random_serial_number())
        .not_valid_before(now-timedelta(minutes=5)).not_valid_after(now+timedelta(days=7))
        .add_extension(x509.BasicConstraints(ca=False,path_length=None),critical=True)
        .add_extension(x509.SubjectAlternativeName([x509.IPAddress(ipaddress.ip_address("127.0.0.1")),x509.DNSName("localhost")]),critical=False)
        .add_extension(x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]),critical=False)
        .sign(ca_key,hashes.SHA256()))
(folder/'ca.pem').write_bytes(ca.public_bytes(serialization.Encoding.PEM))
(folder/'server.pem').write_bytes(leaf.public_bytes(serialization.Encoding.PEM))
(folder/'server-key.pem').write_bytes(key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption()))
# The CA signing key is intentionally not persisted; no global trust is changed.
print('Created seven-day loopback certificate; no trust-store changes')
