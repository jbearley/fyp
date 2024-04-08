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


class Dummy_Data:
    def __init__(self, user_choices):
        self.all_classes = []
        self.majors = user_choices["majors"]
        self.FYP = self.random_classes_by_semester()
        self.requirements = self.random_requirements()

    def get_FYP(self):
        return self.FYP
    
    def get_requirements(self):
        return self.requirements

    def random_class(self, key):
        return {
            "title": key,
            "course_number": "CLS 123",
            "num_credits": 3,
            "attributes": random.sample(attributes, random.randint(1, 6)),
        }

    def random_sample_classes_per_semester(self, i):
        sample_classes_per_semester = {}
        for j in range(random.randint(4, 6)):
            class_key = "class_" + str(i) + "_" + str(j)
            random_class = self.random_class(class_key)
            sample_classes_per_semester[class_key] = random_class
            self.all_classes.append(class_key)
        return sample_classes_per_semester

    def random_classes_by_semester(self):
        classes_by_semester = {}
        for i in range(len(semesters)):
            classes_by_semester[semesters[i]] = self.random_sample_classes_per_semester(
                i
            )
        return classes_by_semester

    def random_requirements(self):
        res = {}
        res["majors"] = {}
        for major in self.majors:
            req_batch = random.sample(self.all_classes, random.randint(20, 24))
            requirements = {
                "pick_1_requirement_1": req_batch[0:3],
                "pick_2_requirement_2": req_batch[3:8],
                "pick_2_requirement_3": req_batch[8:15],
                "singles": req_batch[15:],
            }
            res["majors"][major] = requirements
        res["AOIs"] = {
            # for the dummy data, each of these is a subset of all classes in the FYP, but for the real thing each can be a subset of all classes at Drake
            "pick_one_artistic_literacy": random.sample(self.all_classes, 5),
            "pick_one_critical_thinking": random.sample(self.all_classes, 5),
            "pick_one_the_engaged_citizen": random.sample(self.all_classes, 5),
            "pick_one_historical_foundations": random.sample(self.all_classes, 5),
            "pick_one_information_literacy": random.sample(self.all_classes, 5),
            "pick_one_global_and_cultural_understanding": random.sample(
                self.all_classes, 5
            ),
            "pick_one_scientific_literacy_-_life/behavioral_science": random.sample(
                self.all_classes, 5
            ),
            "pick_one_scientific_literacy_-_physical_science": random.sample(
                self.all_classes, 5
            ),
            "pick_one_quantitative_literacy": random.sample(self.all_classes, 5),
            "pick_one_values_and_ethics": random.sample(self.all_classes, 5),
            "pick_one_written_communication": random.sample(self.all_classes, 5),
        }
        res["equity_and_inclusion"] = {"pick_one": random.sample(self.all_classes, 2)}
        res["total_credits"] = 120
        return res
