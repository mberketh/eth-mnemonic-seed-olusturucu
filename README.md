# Ethereum HD - Mnemonic Cüzdan Oluşturucu

Bu script, `hdwallet` kütüphanesini kullanarak Ethereum için HD (Hierarchical Deterministic) cüzdan yani bir mnemonic kelime dizisi oluşturur.
Aynı mnemonic kelime dizisinden türetilmiş birden fazla cüzdan bilgisi üretir.
Mnemonic Kelimeler, Root Key ve üretilen N sayıda Ethereum cüzdanı (adres, genel anahtar ve özel anahtar) aynı dizinde bir `mnemonic_ethereum_cuzdan_bilgileri.txt` dosyasına kaydedilir.

### Gereksinimler

- Python 3.x
- hdwallet kütüphanesi

### Kurulum

1. Gerekli Python paketini Terminal'den yükleyin:
    ```sh
    pip3 install hdwallet
    ```

2. `eth_mnemonic_generator.py` dosyasını çalıştırın:
    ```sh
    python3 eth_mnemonic_generator.py
    ```

3. Çalıştırma sonucunda oluşturulan `mnemonic_ethereum_cuzdan_bilgileri.txt` dosyasını kontrol edin. Dosya, mnemonic kelimeler, root private key ve türetilen 5 Ethereum cüzdanı (adres, genel anahtar ve özel anahtar) içerecektir.

### Çıktı İçeriği

`mnemonic_ethereum_cuzdan_bilgileri.txt` dosyası aşağıdaki formatta bilgileri içerir:
Mnemonic Kelime Dizisi: ...
Root Private Key: ...
Wallet 1:
Private Key: ...
Public Key: ...
Address: ...
Wallet 2:
...
Wallet 3:
...
Wallet 4:
...
Wallet 5:
...

### Not

Scriptteki 24.satırdaki "5" sayısını değiştirerek daha fazla veya daha az sayıda hesap üretilebilir. Ayrıca, oluşturulan mnemonic kelime dizisini (seed) bir sağlayıcıya (provider) import ederek kullanılabilir oradan ek adresler oluşturulabilir.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.

## İletişim

Sorularınız veya geri bildirimleriniz için lütfen [mberketh](https://twitter.com/mberketh) Twitter hesabı üzerinden iletişime geçin.
