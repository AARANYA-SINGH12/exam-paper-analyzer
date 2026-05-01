from collections import defaultdict

def analyze_patterns(questions, years):
    total_years = len(years)
    sorted_years = sorted(years)
    
    topic_years = defaultdict(set)
    
    for q in questions:
        topic_years[q["topic_label"]].add(q["year"])

    print(dict(topic_years))

    topics = []

    for label, year_set in topic_years.items():
        frequency = len(year_set)
        percentage = (frequency / total_years) * 100

        if percentage >= 70:
            priority = "Must Study"
        elif percentage >= 40:
            priority = "Moderate"
        else:
            priority = "Low Priority"

        gap = sorted_years[-1] - max(year_set)
        if frequency >= 3 and gap >= 2:
            is_predicted = True
        else:
            is_predicted = False  

        entry = {
            "label": label,
            "frequency": frequency,
            "percentage": percentage,
            "priority": priority,
            "appeared_in": sorted(year_set),
            "is_predicted": is_predicted
        }

        topics.append(entry)
    
    topics.sort(key=lambda x: x["frequency"], reverse=True)

    predicted_topics = [t for t in topics if t["is_predicted"]]

    return {
        "topics": topics,
        "years": sorted_years,
        "total_years": total_years,
        "predicted_topics": predicted_topics
    }
    

