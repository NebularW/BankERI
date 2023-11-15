import os
import re
import docx
import cut


def get_internal_rules(root_dir):
    index = 0
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


def get_external_rule(root_dir, file_name):
    return Rule(0, file_name, "", os.path.join(root_dir, file_name + ".txt"))


def get_original_text(path):
    text = ''
    if path.endswith(".docx"):
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            text += paragraph.text
    elif path.endswith(".txt"):
        with open(path, 'r') as file:
            text += file.read()
    return text


def get_chinese_text(path):
    text = get_original_text(path)
    chinese_pattern = re.compile(r"[\u4e00-\u9fa5]+")
    chinese_text = "".join(chinese_pattern.findall(text))
    return chinese_text


class Rule:
    def __init__(self, rule_id, name, category, path):
        self.rule_id = rule_id
        self.name = name
        self.category = category
        self.path = path
        self.text = get_chinese_text(path)
        self.words = cut.cut_words(self.text)
        self.sim = 0.0
