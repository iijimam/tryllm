Class Test.Utils
{

ClassMethod Test(key As %String) As %String
{
    set sql="select top 1 Age from Test.Person Where Gender='F' and Name [ ?"
    set stmt=##class(%SQL.Statement).%New()
    set st=stmt.%Prepare(sql)
    if $$$ISERR(st) {
        write $system.Status.GetErrorText(st),!
    }
    set rset=stmt.%Execute(key)
    do rset.%Next()
    set age=rset.%Get("Age")
    set prompt=age_"歳女性"
    return prompt
}

ClassMethod AskOllama(key As %String, input As %String) [ Language = python ]
{
import requests
import json
import iris
import time
start = time.time()  # 現在時刻（処理開始前）を取得

system=iris.cls("Test.Utils").Test(key)
print(f"システムプロンプト：{system}")
API_SERVER_URL = "http://ollama:11434/api/chat"

def main():
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "pakachan/elyza-llama3-8b",
        "messages": [
            {
                "role": "system",
                "content": f"{system}",
            },        
            {
                "role": "user",
                "content": f"{input}",
            }
        ],
        "stream": True
    }

    response = requests.post(API_SERVER_URL, headers=headers, json=data)
    response.raise_for_status()
    
    #print(response.text)

    answer_text =""
    for line in response.iter_lines():
        decoded_line = json.loads(line.decode('utf-8'))
        answer_text+=decoded_line['message']['content']

    print(answer_text)

main()
end = time.time()  # 現在時刻（処理完了後）を取得
time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(f"処理時間：{time_diff}")  # 処理にかかった時間データを使用
}

}
