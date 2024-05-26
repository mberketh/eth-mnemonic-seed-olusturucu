from hdwallet import HDWallet
from hdwallet.symbols import ETH as ETH_SYMBOL
from hdwallet.utils import generate_mnemonic
import os

def main() -> None:
    """
    Mnemonic kelime dizisi oluşturur ve bu diziden 5 Ethereum cüzdan bilgisi üretir ve bir .txt dosyasına kaydeder.
    """
    try:
        # Mnemonic kelime dizisini oluştur
        mnemonic: str = generate_mnemonic(language="english", strength=128)
        
        # HDWallet nesnesini oluştur ve mnemonic kelime dizisi ile başlat
        hd_wallet: HDWallet = HDWallet(symbol=ETH_SYMBOL)
        hd_wallet.from_mnemonic(mnemonic=mnemonic)

        # Root (master) private key'i al
        root_private_key: str = hd_wallet.private_key()

        # Çıktı içeriğini hazırla
        output: str = f"Mnemonic Kelime Dizisi: {mnemonic}\n\nRoot Private Key: {root_private_key}\n\n"

        # 5 veya belirlenen sayıda cüzdan türet ve bilgilerini yazdır
        for i in range(5):
            # Aynı root mnemonic'ten yeni bir cüzdan örneği oluştur
            wallet = HDWallet(symbol=ETH_SYMBOL)
            wallet.from_mnemonic(mnemonic=mnemonic)
            wallet.from_path(f"m/44'/60'/0'/0/{i}")

            # Cüzdanın özel anahtarı, genel anahtarı ve adresini al
            private_key: str = wallet.private_key()
            public_key: str = wallet.public_key()
            address: str = wallet.dumps()["addresses"]["p2pkh"]

            # Cüzdan bilgilerini çıktıya ekle
            output += (
                f"Wallet {i + 1}:\n"
                f"  Private Key: {private_key}\n"
                f"  Public Key: {public_key}\n"
                f"  Address: {address}\n\n"
            )

        # Çıktıyı bir metin dosyasına yaz
        output_file: str = "mnemonic_ethereum_cuzdan_bilgileri.txt"
        with open(output_file, "w") as file:
            file.write(output)

        print(f"Ethereum cüzdan bilgileri {output_file} dosyasina yazildi")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()