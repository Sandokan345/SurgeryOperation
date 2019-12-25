import sqlite3
con = sqlite3.connect("Veri_Tabanı.db")
cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS veriler (Doktor_adı TEXT, Uzmanlık_Alanı TEXT, "
                   "Unvanı TEXT, Calistigi_Sehir TEXT, Kullanıcı_Puanı INT, Fiyat INT )")
    con.commit()


def puanlama(ad, puan):
    cursor.execute("Select Kullanıcı_Puanı From veriler WHERE Doktor_adı = ?", (ad,))
    eskipuan = cursor.fetchall()
    yenipuan = (int(eskipuan[0][0])+int(puan))/2
    cursor.execute("UPDATE veriler SET Kullanıcı_Puanı = ? WHERE Doktor_adı = ?", (yenipuan, ad))
    con.commit()


def veri_silme(ad):
    cursor.execute("DELETE FROM veriler WHERE Doktor_adı = ?", (ad,))
    con.commit()


def veri_guncelle1(ad, unvan):
    cursor.execute("UPDATE veriler SET Unvanı = ? WHERE Doktor_adı = ?", (unvan, ad))
    con.commit()


def veri_guncelle2(ad, sehir):
    cursor.execute("UPDATE veriler SET Calistigi_Sehir = ? WHERE Doktor_adı = ?", (sehir, ad))
    con.commit()


def veri_guncelle3(ad, puan):
    cursor.execute("UPDATE veriler SET Kullanıcı_Puanı = ? WHERE Doktor_adı = ?", (puan, ad))
    con.commit()


def veri_guncelle4(ad, fiyat):
    cursor.execute("UPDATE veriler SET Fiyat = ? WHERE Doktor_adı = ?", (fiyat, ad))
    con.commit()


def veri_ekle2(isim, Alan, unvan, sehir, puan, fiyat):
    cursor.execute("INSERT INTO veriler VALUES( ?, ?, ?, ?, ?, ?)", (isim, Alan, unvan, sehir, puan, fiyat))
    con.commit()


def veri_ekle():
    cursor.execute("INSERT INTO veriler VALUES('İlker Kuzucu', 'Genel Cerrahi', 'Prof.', 'Ankara', 4, 1000 )")
    cursor.execute("INSERT INTO veriler VALUES('Oğuzhan Eyüpoğlu', 'Beyin Cerrahi', 'Doç.', 'Rize', 2, 500 )")
    cursor.execute("INSERT INTO veriler VALUES('Doğukan Kemer', 'Kalp Cerrahi', 'Uzm.', 'Kars', 3, 1500 )")
    cursor.execute("INSERT INTO veriler VALUES('Burak İn', 'Beyin Cerrahi', 'Prof.', 'Mersin', 5, 4500 )")
    cursor.execute("INSERT INTO veriler VALUES('Ömer Atak', 'Kalp Cerrahi', 'Yard.Doç.', 'Mardin', 4, 2500 )")
    cursor.execute("INSERT INTO veriler VALUES('Said Aydemir', 'Genel Cerrahi', 'Yard.Doç.', 'Ağrı', 1, 800 )")
    cursor.execute("INSERT INTO veriler VALUES('Yavuz Koray', 'Genel Cerrahi', 'Doç.', 'Kocaeli', 2, 1200 )")
    cursor.execute("INSERT INTO veriler VALUES('Erman Korkmaz', 'Kalp Cerrahi', 'Uzm.', 'İstanbul', 3, 3000 )")
    cursor.execute("INSERT INTO veriler VALUES('Mert Kulalı', 'Beyin Cerrahi', 'Prof.', 'İstanbul', 5, 1800 )")
    cursor.execute("INSERT INTO veriler VALUES('Berke Coşkuntuna', 'Kalp Cerrahi', 'Prof.', 'Bursa', 5, 3600 )")
    cursor.execute("INSERT INTO veriler VALUES('Arda Darıcı', 'Kalp Cerrahi', 'Prof.', 'Edirne', 3, 1500 )")
    cursor.execute("INSERT INTO veriler VALUES('Dursun Gümüşay', 'Genel Cerrahi', 'Doç.', 'Tokat', 2, 2000 )")
    cursor.execute("INSERT INTO veriler VALUES('Veysel Albayrak', 'Beyin Cerrahi', 'Uzm.', 'Ankara', 4, 2500 )")
    cursor.execute("INSERT INTO veriler VALUES('Mehmet Öz', 'Kalp Cerrahi', 'Prof.', 'Van', 5, 1000 )")
    cursor.execute("INSERT INTO veriler VALUES('Samet Yücedağ', 'Genel Cerrahi', 'Doç.', 'Bursa', 3, 900 )")
    cursor.execute("INSERT INTO veriler VALUES('Ahmet Kaplan', 'Beyin Cerrahi', 'Uzm.', 'İstanbul', 3, 1600 )")
    cursor.execute("INSERT INTO veriler VALUES('Yusuf Özvatan', 'Kalp Cerrahi', 'Prof.', 'Erzurum', 4, 3000 )")
    cursor.execute("INSERT INTO veriler VALUES('Mehmet Emin', 'Genel Cerrahi', 'Doç.', 'Sivas', 2, 15000 )")
    cursor.execute("INSERT INTO veriler VALUES('İsmail Kemikli', 'Beyin Cerrahi', 'Uzm.', 'Edirne', 4, 6000 )")
    cursor.execute("INSERT INTO veriler VALUES('Oğuzhan Yıldırım', 'Kalp Cerrahi', 'Prof.', 'Giresun', 5, 9000 )")
    cursor.execute("INSERT INTO veriler VALUES('Doğukan Şimşek', 'Genel Cerrahi', 'Doç.', 'Tekirdağ', 3, 2300 )")
    cursor.execute("INSERT INTO veriler VALUES('Sıla Aykut', 'Beyin Cerrahi', 'Uzm.', 'Trabzon', 1, 7000 )")
    cursor.execute("INSERT INTO veriler VALUES('Leyla Okul', 'Kalp Cerrahi', 'Prof.', 'Sivas', 3, 600 )")
    cursor.execute("INSERT INTO veriler VALUES('Sena Avcı', 'Genel Cerrahi', 'Doç.', 'Bolu', 4, 1800 )")
    cursor.execute("INSERT INTO veriler VALUES('Başak Kaplan', 'Beyin Cerrahi', 'Uzm.', 'İstanbul', 5, 2000 )")
    cursor.execute("INSERT INTO veriler VALUES('Beste Kaygın', 'Kalp Cerrahi', 'Prof.', 'Erzurum', 3, 3000 )")
    cursor.execute("INSERT INTO veriler VALUES('İrem Öztürk', 'Genel Cerrahi', 'Doç.', 'İzmir', 2, 2600 )")
    cursor.execute("INSERT INTO veriler VALUES('Deniz Yaren', 'Beyin Cerrahi', 'Yard.Doç.', 'İzmir', 5, 2700 )")
    cursor.execute("INSERT INTO veriler VALUES('Nisa Akın', 'Kalp Cerrahi', 'Uzm.', 'Afyonkarahisar', 4, 1500 )")
    cursor.execute("INSERT INTO veriler VALUES('Canan Karaaslan', 'Genel Cerrahi', 'Doç.', 'Erzurum', 3, 1500 )")
    cursor.execute("INSERT INTO veriler VALUES('Ezgi Kara', 'Beyin Cerrahi', 'Prof.', 'Ankara', 5, 1500 )")
    cursor.execute("INSERT INTO veriler VALUES('Melda Asil', 'Kalp Cerrahi', 'Yard.Doç.', 'Kayseri', 2, 2000 )")
    cursor.execute("INSERT INTO veriler VALUES('Aleyna Gül', 'Genel Cerrahi', 'Uzm.', 'İstanbul', 5, 3000 )")
    cursor.execute("INSERT INTO veriler VALUES('Selin Akpak', 'Beyin Cerrahi', 'Prof.', 'İstanbul', 5, 3500 )")
    cursor.execute("INSERT INTO veriler VALUES('Samet Serbest', 'Kalp Cerrahi', 'Doç.', 'Sakarya', 4, 2000 )")
    cursor.execute("INSERT INTO veriler VALUES('Fatih Ceylan', 'Genel Cerrahi', 'Doç.', 'Mardin', 4, 1000 )")
    cursor.execute("INSERT INTO veriler VALUES('Doğukan Bedirhanoğlu', 'Beyin Cerrahi', 'Uzm.', 'Mersin', 3, 1000 )")
    cursor.execute("INSERT INTO veriler VALUES('Mert Türedi', 'Kalp Cerrahi', 'Prof.', 'Ordu', 4, 1200 )")
    cursor.execute("INSERT INTO veriler VALUES('Berk Yılmaz', 'Genel cerrahi', 'Doç.', 'Kars', 4, 5000 )")
    cursor.execute("INSERT INTO veriler VALUES('Naz Ekşi', 'Beyin Cerrahi', 'Uzm.', 'Sinop', 2, 500 )")
    con.commit()
#tablo_olustur()
#veri_ekle()
#veri_ekle2()
