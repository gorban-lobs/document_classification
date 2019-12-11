import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier


class MultiClassifier:
    def __init__(self, train_data, train_target, train_names):
        self.class_names = train_names
        self.vectorizer = TfidfVectorizer()
        self.vectorized_train_data = self.vectorizer.fit_transform(train_data)

        self.classifiers_dict = self.create_classifiers(train_target)
    
    def create_classifiers(self, train_target):
        bayes_classifier = MultinomialNB(alpha=.01)
        bayes_classifier.fit(self.vectorized_train_data, train_target)
        
        sgd_classifier = SGDClassifier(loss='hinge', penalty='l2',
                                       alpha=1e-3, random_state=42,
                                       max_iter=5, tol=None)
        sgd_classifier.fit(self.vectorized_train_data, train_target)

        # rand_forest_classifier = RandomForestClassifier(n_estimators=len(train_target),
        #                                                 random_state=0)
        # rand_forest_classifier.fit(self.vectorized_train_data, train_target)

        return {
            'nb': bayes_classifier,
            'svg': sgd_classifier,
            # 'rf': rand_forest_classifier,
        }

    def classify_text(self, text, classifier_name):
        classifier = self.classifiers_dict.get(classifier_name, None)
        if classifier:
            text_data = np.array([text])
            vectorized_text = self.vectorizer.transform(text_data)
            result_indices = classifier.predict(vectorized_text)
            return self.class_names[result_indices[0]]
        return "Неправильный тип классификатора"
