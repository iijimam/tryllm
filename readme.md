# テスト

## ollama モデルのダウンロード
```
    volumes:
      - ollama:/root/.ollama
```

の指定があるので、コンテナにログインして以下実行

```
docker exec -it ollama bash
ollama pull gemma
ollama pull llama3
```

これをやると、downしてもモデルはpullされたまま
なんで？

curl http://ollama:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    { "role": "user", "content": "こんにちは" }
  ],
  "stream":true
}'