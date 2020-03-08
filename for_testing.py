from extract_topicword import ExtractTopicWord


text_for_test = [
'明日は元気に研究しに行く予定だ．',
'電気通信大学は良い大学だ．',
'数学の成績が良い．'
]

def main():
    #話題語抽出器の読み込み
    etw = ExtractTopicWord(corpus_choice='for_test', conditional_noun='all', format='binaryfile')

    #テスト
    for text in text_for_test:
        print(text)
        print(etw.getTopicWord(text))
        print('-----------------------------------------------')

if __name__ == '__main__':
    main()
