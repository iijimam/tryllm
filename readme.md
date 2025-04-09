# Open source LLMテスト

参考ページ：https://qiita.com/RyutoYoda/items/ecdfbef8c73aae64aa45

## ollama モデルのダウンロード

- コンテナ開始後、ollamaのコンテナにログインして以下実行
  ```
  docker exec -it ollama bash
  ollama pull gemma
  ollama pull llama3
  ```

- Web APIも用意があります。

  コンテナネットワーク内なら、ollamaのコンテナ名＝ollama　＋　ポート11434 でアクセスできます。
  ```
  curl http://ollama:11434/api/chat -d '{
    "model": "llama3",
    "messages": [
      { "role": "user", "content": "こんにちは" }
    ],
    "stream":true
  }'
  ```

## Web UI

http://localhost:3000/

適当な名称でアカウント登録した後、モデルを左上で選ぶと遅いですがチャットを楽しめます。（日本語で質問しても理解してくれますが回答は英語です）

## IRIS

IRISのUSERネームスペースにTest.Personテーブルを用意し、50件の適当なデータを入れています。

（[person.csv](/iris/data/persons.csv)をビルド時にインポートしてます）

ollamaにTest.Personからとった情報をプロンプトに追加して質問するは、以下メソッドで試せます。

> AskOllamaの第1引数を含むPersonを検索して年齢を取得し、システムプロンプトに年齢＋女性を設定してます。ユーザプロンプトに第２引数の情報指定して、ollamaにpost して回答を得てます。

```
docker exec -it iriscontainer1 bash
iris session iris
do ##class(Test.Utils).AskOllama("さゆり","一番かかりやすい病気")
```

実行例
```
USER>do ##class(Test.Utils).AskOllama("さゆり","一番かかりやすい病気")
システムプロンプト：51歳女性
As a 51-year-old woman, you may be more likely to develop certain health conditions due to your age and sex. Here are some of the most common ones:
1. **Hypertension** (High Blood Pressure): As you age, your blood pressure tends to rise, increasing your risk of heart disease, stroke, and kidney damage.
2. **Type 2 Diabetes**: Your risk of developing type 2 diabetes increases with age, especially if you're overweight or have a family history of the condition.
3. **Osteoporosis**: After menopause, bone density can decline, leading to an increased risk of osteoporosis and fractures.
4. **Migraines**: Migraines are more common in women than men, and they often worsen with age.
5. **Depression and Anxiety**: The stress of middle age, combined with hormonal changes after menopause, can increase your risk of depression and anxiety.
6. **Menopausal Symptoms**: Hot flashes, night sweats, and mood swings are common during the menopausal transition (around ages 45-55).
7. **Breast Cancer**: While breast cancer can occur at any age, it's more common in women over 50.
8. **Cardiovascular Disease**: Your risk of heart disease increases with age, especially if you have high blood pressure, high cholesterol, or a family history of heart problems.
9. **Cervical Dysplasia**: Human papillomavirus (HPV) can cause abnormal cell changes in the cervix, which are more common after age 50.
10. **Sleep Disorders**: As you age, sleep quality often declines, leading to insomnia, sleep apnea, and other sleep disorders.
Remember, it's essential to maintain a healthy lifestyle, including regular exercise, a balanced diet, and stress management techniques, to reduce your risk of developing these conditions.
```

