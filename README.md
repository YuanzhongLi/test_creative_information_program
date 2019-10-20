# python_environment

## install pipenv
pythonでのnpmのような管理ツール
brewからinstall

```bash
brew install pipenv
```

## gitへのcommit
PipfileとPipfile.lockをコミットに含める

## jupyter notebook
work ディレクトリを作成しjupyterとjupytextをinstall
```bash
mkdir <directory_name>
cd <directory_name>
pipenv install jupyter jupytext
```

### 初回のみ行う手順
- pipenv run jupyter notebook --generate-configコマンドを実行し、~/.jupyter/jupyter_notebook_config.pyを作成します。

- echo 'c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"' >> ~/.jupyter/jupyter_notebook_config.pyコマンドを実行し、Jupytextを利用可能にします。

- echo 'c.ContentsManager.default_jupytext_formats = "ipynb,py"' >> ~/.jupyter/jupyter_notebook_config.pyコマンドを実行し、Jupyter NotebookとPythonスクリプトが連動するように設定します。

### 起動
```bash
pipenv run jupyter notebook
```
ブラウザ上でJupyter Notebookが開く

### 終了
Jupyter Notebookを起動しているターミナル上でCtrl+Cを押す

## nbextensionsを導入
```bash
pipenv install jupyter-contrib-nbextensions
pipenv install jupyter-nbextensions-configurator
```

### nbextensionsを有効化
```bash
pipenv run jupyter contrib nbextension install --user
pipenv jupyter nbextensions_configurator enable --user
```
nbextensionsのカスタマイズについてはこちら
http://pynote.hatenablog.com/entry/jupyter-notebook-nbextensions

#### yabfのinstall
```bash
pipenv install yapf
```

### syntax highlightの有効化
```bash
pipenv run jupyter nbextension enable highlight_selected_word/main
```

## テーマカスタマイズ
```bash
pipenv install jupyterthemes
pipenv run jt -t monokai -T -N -ofs 11 -f inconsolata -tfs 14 -cellw 80%
```

## numpy, pandasのinstall
```bash
pipenv install numpy pandas
```
