import random


semesters = [
    "2022 Fall",
    "2023 Spring",
    "2023 Fall",
    "2024 Spring",
    "2024 Fall",
    "2025 Spring",
    "2025 Fall",
    "2026 Spring",
]

attributes = [
    "First Year Seminar",
    "Artistic Literacy",
    "Critical Thinking",
    "The Engaged Citizen",
    "Historical Foundations",
    "Information Literacy",
    "Global and Cultural Understanding",
    "Scientific Literacy - Life/Behavioral Science",
    "Scientific Literacy - Physical Science",
    "Quantitative Literacy",
    "Values and Ethics",
    "Written Communication",
    "Equity and Inclusion",
]


def random_class():
    return {
        "title": "Class Name",
        "course_number": "CLS 123",
        "num_credits": 3,
        "attributes": random.sample(attributes, random.randint(1, 6)),
    }


def random_sample_classes_per_semester():
    sample_classes_per_semester = {}
    for i in range(random.randint(4, 6)):
        sample_classes_per_semester["class_" + str(i)] = random_class()
    return sample_classes_per_semester


def random_classes_by_semester():
    classes_by_semester = {}
    for semester in semesters:
        classes_by_semester[semester] = random_sample_classes_per_semester()
    return classes_by_semester
