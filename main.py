import os

from flask import Flask, request

from rule import get_external_rule, get_original_text

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/external/list')
def external_list():
    file_names = [f.rsplit('.', 1)[0] for f in os.listdir(external_path) if
                  os.path.isfile(os.path.join(external_path, f))]
    return file_names


@app.route('/external/text')
def external_text():
    name = request.args.get('name')
    path = os.path.join(external_path, name + '.txt')
    external_rule = get_original_text(path)
    external_rule_slice = external_rule.split('.')
    for i in range(len(external_rule_slice)):
        if external_rule_slice[i] == 'text':
            return external_rule_slice[i+1]
    return external_rule


@app.route('/cal')
def calculate():
    name = request.args.get('name')
    external_rule = get_external_rule(external_path, name)
    return external_rule.word_count


if __name__ == '__main__':
    internal_path = './data/internal'
    external_path = './data/external'
    # internal_rules = get_internal_rules(internal_path)
    app.run(debug=True)
