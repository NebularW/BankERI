import os
import re
import docx
import cut


def get_rules(root_dir):
    index = 1
    rules = []
    for dir_path, dir_names, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.docx') or filename.endswith('.doc'):
                category = dir_path.rsplit('/')[3]
                name = filename.rsplit('.', 1)[0]
                path = os.path.join(dir_path, filename)
                rule = Rule(index, name, category, path)
                rules.append(rule)
                index += 1
    return rules


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

    def __str__(self):
        return (f'Rule id:{self.rule_id}\n'
                f'name:{self.name}\n'
                f'category:{self.category}\n'
                f'text:{self.text}\n'
                f'word_count:{self.word_count}')
