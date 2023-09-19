from youtube import search_shorts
from instagram import upload_reel


def run():
    keyword = input("Youtubedan videolarni qidirish kalit so'zni kiriting: ")
    limit = input("Maksimum izlash miqdorini kiriting(Faqat raqam): ")
    shorts = search_shorts(keyword=keyword, max_results=limit)
    print("Kalit so'z bo'yicha videolar topildi: ")
    results = []
    for count, short in enumerate(shorts, start=1):
        print(f"{count}: {short['snippet']['title']}")
        answer = input("Ushbu videoni instagram yuklashni xohlaysizmi(N/Yes): ")
        if answer == 'N':
            print("Video bekor qilindi.")
        else:
            print("Video ro'yxatga qo'shildi.")
            results.append(short)
    input("Tanlangan videolarni Instagramga yuklash uchun xohlagan tugmani bosing.")
    upload_reel(results)
    print("Topshiriq bajarildi!")


if __name__ == '__main__':
    run()


