from read_wordcount_corpus import read_wordcount_corpus
import MeCab

class ExtractTopicWord():
    #読み込み
    def __init__(self,corpus_choice='dialogue',format='binaryfile'):
        #mecab_parse用
        self.m = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

        #コーパスを何にしたかの記録
        self.corpus_choice = corpus_choice

        #指定したコーパスからwordCounterの読み込み
        self.wordCounter = read_wordcount_corpus(corpus=corpus_choice,format=format)


    #mecabFormatを作成
    def mecab_parse(self,text):
        mecabFormat = []
        for txt in self.m.parse(text).split('\n'):
            t = txt.split('\t')
            if len(t)==2:
                xt = t[1].split(',')
                mecabFormat.append([t[0],xt])
        return mecabFormat

    #テキストから話題語を抽出する
    def getTopicWord(self,text):
        nounList = []
        mecabFormat = self.mecab_parse(text)
        #テキスト中の名詞でwordCounterに入っている名詞を対象とする
        for word_format in mecabFormat:
            if word_format[1][0] == '名詞':
                if word_format[0] in self.wordCounter.keys():
                    nounList.append(word_format[0])

        #候補となる名詞がなければNoneを返す
        if nounList == []:
            return None

        #出現頻度の低い順に並び替えて話題語を出力
        rank = list(zip(nounList,map(self.wordCounter.get,nounList)))
        rank.sort(key=lambda x:x[1])
        #return rank[0][0]
        #テスト用
        return rank
