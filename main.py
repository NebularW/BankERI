import os

from flask import Flask, request
from gensim import corpora,models,similarities

from rule import get_external_rule, get_original_text, get_internal_rules

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
    external_rule_slice = external_rule.split('.')
    for i in range(len(external_rule_slice)):
        if external_rule_slice[i] == 'text':
            return external_rule_slice[i+1]
    return external_rule


@app.route('/cal')
def calculate():
    name = request.args.get('name')
    external_rule = get_external_rule(external_path, name).words
    external_rule_vec = dictionary.doc2bow(external_rule)
    sim = index[tfidf[external_rule_vec]]
    result = sorted(enumerate(sim), key=lambda item: -item[1])
    
    print(result)
    return result


if __name__ == '__main__':
    internal_path = './data/internal'
    external_path = './data/external'
    internal_rules = get_internal_rules(internal_path)
    internal_rule_list = [rule.words for rule in internal_rules]
    dictionary = corpora.Dictionary(internal_rule_list)
    corpus = [dictionary.doc2bow(doc) for doc in internal_rule_list]
    tfidf = models.TfidfModel(corpus)
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    app.run(debug=True)
