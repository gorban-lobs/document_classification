import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


class MultiClassifier:
    def __init__(self, train_data, train_target, train_names):
        self.class_names = train_names
        self.vectorizer = TfidfVectorizer()
        self.vectorized_train_data = self.vectorizer.fit_transform(train_data)

        bayes_classifier = MultinomialNB(alpha=.01)
        bayes_classifier.fit(self.vectorized_train_data, train_target)

        self.classifiers_dict = self.create_classifiers(train_target)
    
    def create_classifiers(self, train_target):
        bayes_classifier = MultinomialNB(alpha=.01)
        bayes_classifier.fit(self.vectorized_train_data, train_target)
        return {
            'mn_naive_bayes': bayes_classifier,
        }

    def classify_text(self, text, classifier_name):
        classifier = self.classifiers_dict[classifier_name]
        text_data = np.array([text])
        vectorized_text = self.vectorizer.transform(text_data)
        result_indices = classifier.predict(vectorized_text)
        return self.class_names[result_indices[0]]


if __name__ == '__main__':
    train_dataset = fetch_20newsgroups(subset='train',
                                       remove=('headers', 'footers', 'quotes'))
    multiclassifier = MultiClassifier(train_dataset.data, train_dataset.target,
                                 train_dataset.target_names)

    result = multiclassifier.classify_text(
        'Pitcher. Championship. Nice strike. Great homerun.',
        'mn_naive_bayes')
    print(result)