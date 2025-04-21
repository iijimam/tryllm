from flask import Flask, render_template,request
import iris
import irisbuiltins
import json
import os
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route('/', methods=['GET'])
def meetup():
    name = "Hello FishDetector!"
    rset=iris.sql.exec("select FishDetector.Utils_t1('okok')")
    name=next(rset)[0]
    return name

#ファイルアップロード なぜか動かない
# iris.clsもだめ。以下エラーが出る
#  File "/src/wsgi/detector.py", line 30, in upload
#    fishinfo=iris.cls("FishDetector.Utils").searchVec(filefullpath)
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#RuntimeError: IRIS class allocation failed
#
# ストアド呼び出しも以下エラーが出る
# irisbuiltins.SQLError: SQL Function FISHDETECTOR.UTILS_SEARCHVEC failed with error:  SQLCODE=-400,%msg=エラー #5002: ObjectScript エラー:<PYTHON EXCEPTION> *<class 'TypeError'>: unsupported operand type(s) for +: '_NamespacePath' and 'list'

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['fish']
    filefullpath=os.path.join('/data/images/', file.filename)
    file.save(filefullpath)
    # ここから処理 クラスメソッドを直に呼べなくなった様子（2025.1GAから？）
    #fishinfo=iris.cls("FishDetector.Utils").searchVec(filefullpath)
    sql="select FishDetector.Utils_searchVec(?)"
    #statement=iris.sql.prepare(sql)
    #rs=statement.execute(filefullpath)
    rs=iris.sql.exec("select FishDetector.Utils_searchVec('/data/images/masaba.jpg')")
    fishinfo=next(rs)
    g=iris.gref("^iijima")
    g["afterquery"]=fishinfo
    contents=f"アップロードファイル：{file.filename} は、{fishinfo.split(",")[0]} です。"
    return contents


if __name__ == "__main__":
    app.run(debug=True)