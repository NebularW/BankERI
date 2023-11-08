import os

from flask import Flask

from rule import Rule, get_rules

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/cut/')
def getCut():
    return rule.words




if __name__ == '__main__':
    internal_path = './data/internal'
    rules = get_rules(internal_path)
    rule = rules[0]
    print(len(rules))
    # print(rule.words)
    # print(rule.word_count)
    # app.run()
