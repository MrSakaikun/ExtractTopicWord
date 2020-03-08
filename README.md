#  ExtractTopicWord

コーパス内に出てくる頻度が低い単語が「話題語」になりやすいと仮定した場合の「話題語抽出器」のプログラムです．

与えられた文に対して，その文中に含まれている「話題語」を抽出し，提示します．

例：
```
明日は元気に研究しに行く予定だ．
研究
-----------------------------------------------
電気通信大学は良い大学だ．
電気通信大学
-----------------------------------------------
数学の成績が良い．
数学
-----------------------------------------------
```


### 話題語抽出について

以下の論文を参考にしてこのプログラムを作成しました．（特に話題語抽出に関する部分，ただし厳密には論文で採用している手法と少し異なる部分があります）


[1]Sugiyama H., Meguro T., Higashinaka R., and Minami Y.: Open-domain Utterance Generation for Conversational Dialogue Systems using Web-scale Dependency Structures, in Proceedings of the Special Interest Group on Discourse and Dialogue 2013 Conference, Metz, France, pp.334-338, 2013.

[[1]の論文参照](https://www.semanticscholar.org/paper/Open-domain-Utterance-Generation-for-Conversational-Sugiyama-Meguro/35d6117e582825dd3467c6106047eb50704e03e1)


[2]三上，萩原: 対話システムにおけるランダム性を考慮した話題展開手法,日本感性工学会論文誌 Vol.17 No.3, pp. 365-373, 2018

[[2]の論文参照](https://www.jstage.jst.go.jp/article/jjske/17/3/17_TJSKE-D-17-00084/_article/-char/ja)




## 動作環境

### 確認した動作環境
* Python 3.6.9 (anaconda3-5.0.0)

### 使用したパッケージ
* MeCab
* collections
* pickle
* csv


MeCab 以外は標準で入っているパッケージのはずです．MeCabのインストールの仕方は以下のページなどを参照してください．（インターネット検索をかけたほうが早いかもしれません）

公式サイト：

https://taku910.github.io/mecab/

【これ1本でOK】MeCabをインストールしてPythonで形態素解析する方法【Mac】：

https://tech-diary.net/how-to-install-mecab/




## 使い方
0. （必要な人は）MeCabをインストールし，Pythonから使える状態にする．

1. このレポジトリをクローンする
```bash
git clone https://github.com/MrSakaikun/ExtractTopicWord.git
cd ExtractTopicWord
```

2. 以下のコマンドを実行する
```bash
python for_testing.py
```

実行結果は先ほどの例をご覧ください．


## コーパスについて
今回はテスト用のコーパスを準備していますが，テスト用のため精度はかなり悪いです．精度の良い「話題語抽出器」を作成したい場合は，以下の手順で単語出現頻度コーパスを作成し，クローンしたフォルダにコピーしてください．

1. コーパスとなる文書をテキストファイルで準備してください．

2. [MakeWordCountFromDocument](https://github.com/MrSakaikun/MakeWordCountFromDocument)のプログラムを用いて，word_count.binaryfile （単語出現頻度コーパス）を作成してください．（詳細は[リンク先の README.md ](https://github.com/MrSakaikun/MakeWordCountFromDocument/blob/master/README.md)をご覧ください）

3. 作成したword_count.binaryfile をExtractTopicWordフォルダにコピーしてください．

4. ExtractTopicWordフォルダに移動し，以下のコマンドで実行してください
```bash
python for_testing.py
```

## プログラム作成者
Yuya Sakai

GitHub:[MrSakaikun](https://github.com/MrSakaikun)

E-Mail:
yuyasakai1002[at]gmail.com

↑[at]を@に変えてください


## LICENSE
Please check [here]()

MIT License



Copyright (c) 2020 Yuya Sakai
