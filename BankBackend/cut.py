import jieba


def cut_words(text):
    # jieba 默认启用了HMM（隐马尔科夫模型）进行中文分词
    seg_list = jieba.lcut(text, cut_all=True)
    word_list = remove_stopword(seg_list)
    return word_list


def remove_stopword(seg_list):
    word_list = []
    stop = open('./data/stopwords.txt', 'r+', encoding='utf-8')
    # 用'\n'去分隔读取，返回一个一维数组
    stopword = stop.read().split("\n")
    # 遍历分词表
    for word in seg_list:
        # 去除停用词, 去除单字
        if not (word.strip() in stopword) and (len(word.strip()) > 1):
            word_list.append(word)
    stop.close()
    return word_list
