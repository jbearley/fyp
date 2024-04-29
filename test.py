from Jacob import *

def check_for_aoi(aoireqs, dict_6, semesterlist):
    for course in semesterlist:
        for aoicourse, info in dict_6.items():
            print(aoicourse, info)
            if course == aoicourse:
                print("?", course, aoicourse)
                if info in aoireqs:
                    aoireqs.remove(info)
                break