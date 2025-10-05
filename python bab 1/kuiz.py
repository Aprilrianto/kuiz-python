import random


soal_kuis = [
    {"pertanyaan": "Bahasa pemrograman untuk AI yang populer adalah?", "jawaban": "python"},
    {"pertanyaan": "Ekstensi file Python adalah?", "jawaban": ".py"},
    {"pertanyaan": "Fungsi untuk menampilkan output di Python adalah?", "jawaban": "print"},
    {"pertanyaan": "Operator logika 'dan' di Python ditulis dengan?", "jawaban": "and"},
    {"pertanyaan": "Konsep OOP yang berarti pewarisan sifat disebut?", "jawaban": "inheritance"},
    {"pertanyaan": "Bahasa pemrograman Java diciptakan oleh?", "jawaban": "james gosling"},
    {"pertanyaan": "Fungsi len() digunakan untuk menghitung apa?", "jawaban": "panjang"},
    {"pertanyaan": "Simbol komentar satu baris di Python adalah?", "jawaban": "#"},
    {"pertanyaan": "Struktur data Python yang pakai tanda [] disebut?", "jawaban": "list"},
    {"pertanyaan": "Bahasa pemrograman C diciptakan oleh?", "jawaban": "dennis ritchie"}
]

aktif = True

while aktif:
    print("\n===== KUIS PEMROGRAMAN 20 SOAL =====")
    score = 0
    
    random.shuffle(soal_kuis)

    for i, soal in enumerate(soal_kuis, start=1):
        print(f"\nSoal {i}: {soal['pertanyaan']}")
        jawaban = input("Jawaban Anda: ").strip().lower()

        if jawaban == soal["jawaban"]:
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah! Jawaban yang benar: {soal['jawaban']}")

    print("\n===== HASIL AKHIR =====")
    print(f"Skor Anda: {score}/10")

   
    if score == 10:
        print("Sempurna! Nilai A+ 🎉")
    elif score >= 8:
        print("Hebat! Nilai A")
    elif score >= 6:
        print("Bagus! Nilai B")
    elif score >= 4:
        print("Cukup! Nilai C")
    else:
        print("Perlu belajar lagi! Nilai D")

    
    main_lagi = input("\nMau main lagi? (y/n): ").lower()
    if main_lagi != "y":
        aktif = False

else:
    print("\nTerima kasih sudah bermain kuis ini! 👋")
