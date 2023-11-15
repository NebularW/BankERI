import json
import os
from flask import Flask, request
from gensim import corpora, models, similarities
from process import get_external_rule, get_original_text, get_internal_rules
app = Flask(__name__)


@app.route('/')
def page():
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
    external_rule_slice = external_rule.split(': ')
    for i in range(len(external_rule_slice)):
        if 'text' in external_rule_slice[i]:
            return external_rule_slice[i + 1]
    return external_rule


@app.route('/cal')
def calculate():
    name = request.args.get('name')
    external_rule = get_external_rule(external_path, name).words
    external_rule_vec = dictionary.doc2bow(external_rule)
    sim = index[tfidf[external_rule_vec]]
    array = sorted(enumerate(sim), key=lambda item: -item[1])
    result = []
    for i in range(10):
        rule = internal_rules[array[i][0]]
        rule.sim = float(array[i][1])
        element = {'sim': rule.sim, 'name': rule.name, 'category': rule.category, 'text': rule.text}
        result.append(element)
    result_str = json.dumps(result, ensure_ascii=False)
    return result_str


if __name__ == '__main__':
    internal_path = './data/internal'
    external_path = './data/external'
    internal_rules = get_internal_rules(internal_path)
    internal_rule_list = [rule.words for rule in internal_rules]
    dictionary = corpora.Dictionary(internal_rule_list)
    corpus = [dictionary.doc2bow(doc) for doc in internal_rule_list]
    tfidf = models.TfidfModel(corpus)
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    app.run()
