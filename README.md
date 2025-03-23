# akbankproject
Metro Ağı Rota Bulma Algoritması
Bu proje, bir şehirdeki metro ağı için en az aktarmalı ve en hızlı rotayı bulmayı sağlayan bir Python uygulamasıdır.

📌 Özellikler
✅ Metro hatlarını ve istasyonlarını modelleme
✅ İstasyonlar arası bağlantıları ekleme
✅ En az aktarmalı rota bulma (BFS Algoritması)
✅ En hızlı rota bulma (Dijkstra / A* Algoritması)
✅ Örnek metro ağı ile test senaryoları

Dosya Yapısı
/metro-agi
│-- metro.py      # Ana kod dosyası
│-- README.md     # Proje açıklaması

Kullanım
1️⃣ Python ile Çalıştırma
Python'un yüklü olduğundan emin olun.
Proje klasörüne gidin:
cd MeryemnurPala_MetroSimulation
ve kodu çalıştırın
python MeryemnurPala_MetroSimulation.py

Örnek Kullanım
Program çalıştırıldığında, örnek metro ağı üzerinden aşağıdaki test senaryoları uygulanır:

🔹 Senaryo 1: AŞTİ'den OSB'ye rota bulma
🔹 Senaryo 2: Batıkent'ten Keçiören'e en iyi yol
🔹 Senaryo 3: Keçiören'den AŞTİ'ye en hızlı güzergâh

 Kullanılan Algoritmalar
🔹 En az aktarmalı rota için: Genişlik Öncelikli Arama (BFS)
🔹 En hızlı rota için: A Algoritması* (Öncelikli Kuyruk - heapq)

Örnek Çıktı:
![Ekran görüntüsü 2025-03-23 195852](https://github.com/user-attachments/assets/08646bca-5a9a-4f6a-815e-8faa9dee6864)
