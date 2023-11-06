import re
import docx
import cut


def get_text(path):
    text = ''
    doc = docx.Document(path)
    for paragraph in doc.paragraphs:
        text += paragraph.text
    chinese_pattern = re.compile(r"[\u4e00-\u9fa5]+")
    chinese_text = "".join(chinese_pattern.findall(text))
    return chinese_text


class Rule:
    def __init__(self, rule_id, name, category, path):
        self.rule_id = rule_id
        self.name = name
        self.category = category
        self.path = path
        self.text = get_text(path)
        self.words, self.word_count = cut.cut_words(self.text)
