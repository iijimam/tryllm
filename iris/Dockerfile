ARG IMAGE=containers.intersystems.com/intersystems/iris-community:2025.1
FROM $IMAGE

USER root
RUN apt update \
    && apt install git -y
WORKDIR /opt/src
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/src
USER ${ISC_PACKAGE_MGRUSER}

# ビルド中に実行したいスクリプトがあるファイルをコンテナにコピーしています
COPY iris/iris.script .
COPY iris/src .
COPY iris/data .
COPY iris/requirements.txt .

# IRISを開始し、IRISにログインし、iris.scriptに記載のコマンドを実行しています
RUN iris start IRIS \
    && pip install -r requirements.txt --break-system-packages \
    && iris session IRIS < iris.script \
    && iris stop IRIS quietly 