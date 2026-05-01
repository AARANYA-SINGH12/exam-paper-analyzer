from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_topics(questions, num_topics):
    texts = []
    for _ in questions:
        texts.append(_["text"])
    
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)

    kmeans = KMeans(n_clusters=num_topics, random_state=42, n_init=10)
    kmeans.fit(tfidf_matrix)
    labels = kmeans.labels_ 

    def keyword_label():
        topic_labels = {}
        feature_names = vectorizer.get_feature_names_out()
    
        for cluster_id in range(num_topics):
            centroid = kmeans.cluster_centers_[cluster_id]
            top_indices = centroid.argsort()[-3:][::-1]
            top_words = [feature_names[i] for i in top_indices]
            topic_labels[cluster_id] = " / ".join(top_words)
    
        return topic_labels
    
    topic_labels = keyword_label()


    for i, question in enumerate(questions):
        question["topic_id"] = int(labels[i])
        question["topic_label"] = topic_labels[int(labels[i])]

    return questions