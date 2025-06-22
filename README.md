# Email Summarization

Bu projede, İngilizce e-posta metinlerinden anlamlı özetler çıkarmak için transformer tabanlı bir yapı kullandım.

## Kullanılan Teknolojiler

- **FastAPI**: API servisi oluşturmak için
- **Gradio**: API’yi test etmek için arayüz (opsiyonel)
- **SentenceTransformers**: Cümleleri vektörlemek için (`all-MiniLM-L6-v2`)
- **nltk**: Cümleleri ayırmak için (`sent_tokenize`)
- **scikit-learn**: Cümle vektörleri arasındaki benzerlik hesaplaması (cosine similarity)
- **langdetect**: Metnin İngilizce olup olmadığını tespit etmek için
- **Render**: API’yi canlıya almak için

## Nasıl Çalışır

1. E-posta metni cümlelere bölünür.
2. Her cümle `Sentence-BERT` ile vektörlenir.
3. Ortalama cümle vektörüne en yakın 3 cümle seçilerek özet oluşturulur.
4. FastAPI ile `/summarize` endpoint’inden sonuç döndürülür.

