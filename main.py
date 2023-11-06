from rule import Rule

if __name__ == '__main__':
    internal_path = './data/internal'
    rule_id = 1
    category = "三农业务部-制度"
    name = '《代收代付业务管理办法》'
    path = './data/internal/三农业务部-制度/《代收代付业务管理办法》.docx'
    rule = Rule(rule_id, name, category, path)
    print(rule.words)
    print(rule.word_count)
