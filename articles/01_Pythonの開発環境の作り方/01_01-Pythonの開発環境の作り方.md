# Pythonの開発環境の作り方

機械学習モデルの開発で最も広く使われている言語はPythonであると思います(2022年6月現在)。
そのため、このレポジトリはPythonのコードをJupyter Notebookで動かしながら機械学習の基礎を学ぶことにします。

## Pythonのインストール
Pythonを動作させる環境がない人は、以下のサイトなどからOSに合わせてPythonをインストールしてください。
- https://www.python.org/downloads/

筆者自身は`pyenv`と`pyenv-virtualenv`を使って開発環境の管理をしていますが、各自が使いやすいツールを使うのがいいと思います。

- `pyenv`: 
    - https://github.com/pyenv/pyenv
- `pyenv-virtualenv`
    - https://github.com/pyenv/pyenv-virtualenv

## Poetryのインストール
PoetryはPythonのパッケージ管理ツールのひとつで、
簡単に仮想環境を作ることが出来るので筆者は愛用しています。

ルートディレクトリに用意した`Makefile`を使って、以下のコマンドでインストール出来るようにしています。

```
make install_poetry
```

## 仮想環境のセットアップ
Poetryをインストールしたら、以下のコマンドで仮想環境の構築ができます。

```
poetry install
```

## Jupyter Notebook の起動方法
以下のコマンドでJupyter Notebookを起動できます。
`./notebooks/`以下の各ノートブックを開いてコードを動かしながら機械学習モデルについて学ぶ記事を書く予定です。
