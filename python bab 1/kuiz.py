import random

soal_kuis = [
    {"pertanyaan": "Bendera NKRI warnanya?", "jawaban": "cuma dua aja"},
    {"pertanyaan": "Apakah yang dilakukan orang ketika sakit?", "jawaban": "pulang"},
    {"pertanyaan": "Yang sering mendapat nilai 100 saat ulangan yaitu?", "jawaban": "kertas"},
    {"pertanyaan": "Di rumah makan Padang, selain pakai sendok kita makan pakai?", "jawaban": "tenaga"},
    {"pertanyaan": "Senikmat-nikmatnya makan di luar lebih nikmat makan di?", "jawaban": "telan"},
    {"pertanyaan": "Ikan bernapas di air dengan?", "jawaban": "tenang"},
    {"pertanyaan": "Kita tidak bisa menelepon, kalau handphone-nya nggak ada?", "jawaban": "angka"},
    {"pertanyaan": "Seorang barber mencukur rambut pelanggan dengan?", "jawaban": "gantian"},
    {"pertanyaan": "Nasi yang enak buat sarapan, biasanya nasi yang?", "jawaban": "matang"},
    {"pertanyaan": "Cermin jika dilap jadi?", "jawaban": "cermin"}
]

aktif = True

while aktif:
    print("\n===== KUIS PEMROGRAMAN =====")
    score = 0
    
    random.shuffle(soal_kuis)

    for i, soal in enumerate(soal_kuis, start=1):
        print(f"\nSoal {i}: {soal['pertanyaan']}")
        jawaban_user = input("Jawaban Anda: ").strip().lower()

        if jawaban_user == soal["jawaban"]:
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
    print("\nTerima kasih sudah bermain kuis ini, see u")