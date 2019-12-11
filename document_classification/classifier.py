import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier


class MultiClassifier:
    def __init__(self, train_data, train_target, train_names):
        self.class_names = train_names
        self.vectorizer = TfidfVectorizer()
        self.vectorized_train_data = self.vectorizer.fit_transform(train_data)

        self.classifiers_dict = self.create_classifiers(train_target)

        self.group_description = self.get_group_description()
    
    def create_classifiers(self, train_target):
        bayes_classifier = MultinomialNB(alpha=.01)
        bayes_classifier.fit(self.vectorized_train_data, train_target)
        
        sgd_classifier = SGDClassifier(loss='hinge', penalty='l2',
                                       alpha=1e-3, random_state=42,
                                       max_iter=5, tol=None)
        sgd_classifier.fit(self.vectorized_train_data, train_target)

        knn_classifier = KNeighborsClassifier(n_neighbors=30,
                                              weights='distance')
        knn_classifier.fit(self.vectorized_train_data, train_target)

        return {
            'nb': bayes_classifier,
            'sgd': sgd_classifier,
            'knn': knn_classifier,
        }

    def classify_text(self, text, classifier_name):
        classifier = self.classifiers_dict.get(classifier_name, None)
        if classifier:
            text_data = np.array([text])
            vectorized_text = self.vectorizer.transform(text_data)
            result_indices = classifier.predict(vectorized_text)
            return self.group_description[self.class_names[result_indices[0]]]
        return "Неправильный тип классификатора"


    def get_group_description(self):
        return {
            'comp.graphics': 'Компьютерная графика',
            'comp.os.ms-windows.misc': 'OS Windows',
            'comp.sys.ibm.pc.hardware': 'IBM PC',
            'comp.sys.mac.hardware': 'Macintosh',
            'comp.windows.x': 'Windows X',
            'rec.autos': 'Автомобили',
            'rec.motorcycles': 'Мотоциклы',
            'rec.sport.baseball': 'Бейсбол',
            'rec.sport.hockey': 'Хоккей',
            'sci.crypt': 'Криптография',
            'sci.electronics': 'Электроника',
            'sci.med': 'Медицина',
            'sci.space': 'Космос',
            'misc.forsale': 'Продажи',
            'talk.politics.misc': 'Политика (разное)',
            'talk.politics.guns': 'Политика (оружие)',
            'talk.politics.mideast': 'Политика (Средний Восток)',
            'talk.religion.misc': 'Религия (разное)',
            'alt.atheism': 'Атеизм',
            'soc.religion.christian': 'Религия (христианство)',
        }