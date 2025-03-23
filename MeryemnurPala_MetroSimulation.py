from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

# İstasyon sınıfı, metro istasyonlarını temsil eder
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyonun benzersiz kimliği
        self.ad = ad  # İstasyon adı
        self.hat = hat  # İstasyonun ait olduğu hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # Komşu istasyonlar ve aralarındaki süre bilgisi
    
    # Komşu istasyonu ekleme metodu
    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

# MetroAğı sınıfı, tüm metro hatlarını ve istasyonlarını içeren yapıdır
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}  # İstasyonları saklayan sözlük
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hatlara göre istasyonları saklayan sözlük
    
    # Yeni bir istasyon ekleme metodu
    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)  # İlgili hatta istasyonu ekler
    
    # İki istasyon arasında bağlantı ekleme metodu
    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    # En az aktarma ile istasyonlar arasındaki rotayı bulan BFS algoritması
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        # BFS için kuyruk (istasyon, yol) ve ziyaret edilen istasyonlar kümesi
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = {baslangic}
        
        while kuyruk:
            current, path = kuyruk.popleft()  # Kuyruktan bir istasyon al
            
            if current == hedef:
                return path  # Hedefe ulaşıldığında yolu döndür
                
            for komsu, _ in current.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    yeni_path = path + [komsu]
                    kuyruk.append((komsu, yeni_path))  # Kuyruğa ekle
                    
        return None  # Ulaşılacak istasyon yoksa None döndür

    # En hızlı rotayı bulan Dijkstra benzeri algoritma
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        # Öncelik kuyruğu (toplam süre, istasyonun benzersiz ID'si, istasyon, yol)
        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edildi = set()
        
        while pq:
            toplam_sure, _, current, path = heapq.heappop(pq)  # En kısa süredeki istasyonu al
            
            if current == hedef:
                return (path, toplam_sure)  # Hedefe ulaşıldığında yolu ve toplam süreyi döndür
                
            if current in ziyaret_edildi:
                continue  # Daha önce ziyaret edildiyse atla
                
            ziyaret_edildi.add(current)
            
            for komsu, sure in current.komsular:
                if komsu not in ziyaret_edildi:
                    yeni_sure = toplam_sure + sure
                    yeni_path = path + [komsu]
                    heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yeni_path))  # Yeni yolu öncelik kuyruğuna ekle
                    
        return None  # Ulaşılacak istasyon yoksa None döndür


# Test kodu
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))