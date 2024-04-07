from collections import OrderedDict
from operator import itemgetter
from class_prereqs_score import class_prereqs_score
from class_is_prereq_score import class_is_prereq_score
from dictionaries2 import *
"""
This is the dictionary1 prereq: {'ACCT 41': None, 'ACCT 42': 'ACCT 41', 'ACCT 110': 'ACCT 42, IS 44', 'ACCT 120': 'ACCT 110', 'ACCT 165': 'ACCT 42', 'ACCT 166': 'ACCT 165', 'ACCT 167': 'ACCT 166', 'ACCT 175': 'ACCT 105, ACCT 165', 'ACCT 185': 'ACCT 42', 'ACCT 186': 'ACCT 185', 'ACTS 50': None, 'ACTS 120': 'MATH 70', 'ACTS 120L': 'MATH 70', 'ACTS 131': 'MATH 70', 'ACTS 131L': 'MATH 70', 'ACTS 135': 'ACTS 131', 'ACTS 140': 'ACT 135', 'ACTS 150': 'ACTS 120, ACTS 131', 'ACTS 155': None, 'ACTS 161': 'ACTS 131', 'ACTS 165': None, 'ACTS 190': None, 'BLAW 60': None, 'BLAW 120': 'BLAW 60', 'BLAW 180': 'BLAW 60', 'BUS 195': 'MGMT 110, MGMT 120, MKTG 101, FIN 101', 'BUS 01': None, 'BUS 02': 'BUS 01', 'BUS 03': 'BUS 02', 'BUS 04': 'BUS 03', 'BUS 05': 'BUS 04', 'BUS 67': None, 'BUS 70': 'BUS 70', 'BUS 73': None, 'BUS 74': None, 'BUS 105': None, 'BUS 120': 'BUS 73, BUS 74', 'BUS 122': 'BUS 73. BUS 74', 'BUS 191': None, 'CS 65': 'MATH 20', 'CS 66': 'CS 65', 'CS 67': 'CS 66', 'CS 83': None, 'CS 130': 'CS 66', 'CS 137': 'CS 67, MATH 50, MATH 54/MATH 101', 'CS 167': 'CS 65, CS 66/STAT 40', 'CS 178': 'CS 66', 'CS 188': 'CS 67, MATH 50, MATH 54/MATH 101', 'CS 191': 'CS 188', 'ECON 02': None, 'ECON 10': None, 'ECON 108': 'MATH 17, ECON 02', 'ECON 109': 'ECON 02', 'ECON 135': 'ECON 10/ECON 01, ECON 02, MATH 17', 'ECON 170': 'ECON 10, ECON 02, STAT 72/STAT 130/MATH 130/ACTS 135, MATH 28', 'ECON 173': 'ECON 02', 'ECON 174': 'ECON 02, ECON 10', 'ECON 190': 'ECON 70/STAT 170', 'ENTR 101': None, 'ENTR 150': 'ENTR 101', 'ENTR 190': 'ENTR 150, MKTG 101', 'FIN 101': 'ACCT 42, IS 44, ECON 2, STAT 71, STAT 30, ACTS 131', 'FIN 102': None, 'FIN 119': 'FIN 101', 'FIN 121': None, 'FIN 129': 'FIN 101', 'FIN 150': 'FIN 101', 'FIN 170': 'FIN 101', 'FIN 193': 'FIN 102, fiN 119/ACTS 120', 'FIN 197': 'FIN 102, FIN 119/ACTS 120, FIN 121/FIN 190/FIN 193', 'INS 51': None, 'INS 141': None, 'INS 161': None, 'INS 180': 'INS 51', 'INS 190': None, 'IS 44': None, 'IS 75': None, 'IS 83': None, 'IS 107': 'IS 44/CS 65', 'IS 114': 'IS 44', 'IS 145': 'IS 44/CS 65', 'IS 150': 'IS 44/CS 65', 'IS 160': 'IS 44/CS 65', 'IS 161': 'IS 107/CS 66', 'MATH 50': None, 'MATH 70': 'MATH 50', 'MATH 100': None, 'MGMT 110': None, 'MGMT 120': 'STAT 72, ACTS 135', 'MGMT 135': None, 'MGMT 160': 'MGMT 120', 'MGMT 170': 'MGMT 110, BUS 70, FIN 101, MKTG 101', 'MGMT 182': 'MGMT 110', 'MGMT 184': 'MGMT 110', 'MGMT 185': 'MGMT 110', 'MKTG 101': 'ECON 2', 'MKTG 102': None, 'MKTG 104': 'MKTG 102', 'MKTG 106': 'MKTG 101', 'MKTG 111': 'MKTG 101', 'MKTG 113': 'MKTG 101, STAT 72/ ACTs 131/MATH 131/STAT 170', 'MKTG 115': 'MKTG 101, PSy 01', 'MKTG 120': 'MKTG 101', 'MKTG 130': 'MKTG 101. MKTG 113, STAT 72', 'MKTG 170': 'MKTG 101', 'STAT 40': None, 'STAT 71': None, 'STAT 72': 'IS 44, STAT 71/STAT 130/ACTS 131', 'STAT 108': 'STAT 71', 'STAT 130': 'STAT 40, MATH 70', 'STAT 170': 'STAT 40', 'STAT 172': 'STAT 130, ACTS 131, STAT 40, STAT 170, MATH 70', 'STAT 190': 'CS 167, STAT 172', 'ACCT 105': 'ACCT 41, ACCT 42, IS 44', 'ECON 131': 'ECON 10/ECON 01'}
This is the dictionary2 fall/spring: {'ACCT 41': '11', 'ACCT 42': '11', 'ACCT 110': '01', 'ACCT 120': '10', 'ACCT 165': '10', 'ACCT 166': '01', 'ACCT 167': '10', 'ACCT 175': '01', 'ACCT 185': '10', 'ACCT 186': '01', 'ACTS 50': '10', 'ACTS 120': '11', 'ACTS 120L': '11', 'ACTS 131': '11', 'ACTS 131L': '11', 'ACTS 135': '11', 'ACTS 140': '11', 'ACTS 150': '10', 'ACTS 155': '01', 'ACTS 161': '01', 'ACTS 165': '10', 'ACTS 190': '01', 'BLAW 60': '11', 'BLAW 120': '01', 'BLAW 180': '10', 'BUS 195': '11', 'BUS 01': '11', 'BUS 02': '11', 'BUS 03': '11', 'BUS 04': '11', 'BUS 05': '11', 'BUS 67': '00', 'BUS 70': '11', 'BUS 73': '11', 'BUS 74': '11', 'BUS 105': '00', 'BUS 120': '10', 'BUS 122': '10', 'BUS 191': '11', 'CS 65': '11', 'CS 66': '11', 'CS 67': '11', 'CS 83': '11', 'CS 130': '10', 'CS 137': '10', 'CS 167': '10', 'CS 178': '01', 'CS 188': '10', 'CS 191': '01', 'ECON 02': '11', 'ECON 10': '11', 'ECON 108': '10', 'ECON 109': '01', 'ECON 135': '01', 'ECON 170': '10', 'ECON 173': '10', 'ECON 174': '01', 'ECON 190': '11', 'ENTR 101': '11', 'ENTR 150': '10', 'ENTR 190': '01', 'FIN 101': '11', 'FIN 102': '11', 'FIN 119': '11', 'FIN 121': '11', 'FIN 129': '01', 'FIN 150': '01', 'FIN 170': '10', 'FIN 193': '11', 'FIN 197': '01', 'INS 51': '11', 'INS 141': '10', 'INS 161': '01', 'INS 180': '10', 'INS 190': '01', 'IS 44': '11', 'IS 75': '11', 'IS 83': '11', 'IS 107': '10', 'IS 114': '10', 'IS 145': '01', 'IS 150': '01', 'IS 160': '11', 'IS 161': '01', 'MATH 50': '11', 'MATH 70': '11', 'MATH 100': '11', 'MGMT 110': '11', 'MGMT 120': '11', 'MGMT 135': '01', 'MGMT 160': '01', 'MGMT 170': '11', 'MGMT 182': '10', 'MGMT 184': '01', 'MGMT 185': '10', 'MKTG 101': '11', 'MKTG 102': '11', 'MKTG 104': '01', 'MKTG 106': '11', 'MKTG 111': '01', 'MKTG 113': '10', 'MKTG 115': '11', 'MKTG 120': '10', 'MKTG 130': '01', 'MKTG 170': '10', 'STAT 40': '11', 'STAT 71': '11', 'STAT 72': '11', 'STAT 108': '01', 'STAT 130': '10', 'STAT 170': '11', 'STAT 172': '10', 'STAT 190': '01', 'ACCT 105': '10', 'ECON 131': '00'}
This is the dictionary3 credits: {'ACCT 41': Decimal('3.0'), 'ACCT 42': Decimal('3.0'), 'ACCT 110': Decimal('3.0'), 'ACCT 120': Decimal('3.0'), 'ACCT 165': Decimal('3.0'), 'ACCT 166': Decimal('3.0'), 'ACCT 167': Decimal('3.0'), 'ACCT 175': Decimal('3.0'), 'ACCT 185': Decimal('3.0'), 'ACCT 186': Decimal('3.0'), 'ACTS 50': Decimal('0.0'), 'ACTS 120': Decimal('3.0'), 'ACTS 120L': Decimal('0.5'), 'ACTS 131': Decimal('3.0'), 'ACTS 131L': Decimal('0.5'), 'ACTS 135': Decimal('3.0'), 'ACTS 140': Decimal('3.0'), 'ACTS 150': Decimal('3.0'), 'ACTS 155': Decimal('3.0'), 'ACTS 161': Decimal('3.0'), 'ACTS 165': Decimal('3.0'), 'ACTS 190': Decimal('3.0'), 'BLAW 60': Decimal('3.0'), 'BLAW 120': Decimal('3.0'), 'BLAW 180': Decimal('3.0'), 'BUS 195': Decimal('3.0'), 'BUS 01': Decimal('0.0'), 'BUS 02': Decimal('0.0'), 'BUS 03': Decimal('0.0'), 'BUS 04': Decimal('0.0'), 'BUS 05': Decimal('0.0'), 'BUS 67': Decimal('3.0'), 'BUS 70': Decimal('3.0'), 'BUS 73': Decimal('2.0'), 'BUS 74': Decimal('2.0'), 'BUS 105': Decimal('3.0'), 'BUS 120': Decimal('3.0'), 'BUS 122': Decimal('3.0'), 'BUS 191': Decimal('3.0'), 'CS 65': Decimal('3.0'), 'CS 66': Decimal('3.0'), 'CS 67': Decimal('3.0'), 'CS 83': Decimal('3.0'), 'CS 130': Decimal('3.0'), 'CS 137': Decimal('3.0'), 'CS 167': Decimal('3.0'), 'CS 178': Decimal('3.0'), 'CS 188': Decimal('3.0'), 'CS 191': Decimal('3.0'), 'ECON 02': Decimal('3.0'), 'ECON 10': Decimal('3.0'), 'ECON 108': Decimal('3.0'), 'ECON 109': Decimal('3.0'), 'ECON 135': Decimal('3.0'), 'ECON 170': Decimal('3.0'), 'ECON 173': Decimal('3.0'), 'ECON 174': Decimal('3.0'), 'ECON 190': Decimal('3.0'), 'ENTR 101': Decimal('3.0'), 'ENTR 150': Decimal('3.0'), 'ENTR 190': Decimal('3.0'), 'FIN 101': Decimal('3.0'), 'FIN 102': Decimal('3.0'), 'FIN 119': Decimal('3.0'), 'FIN 121': Decimal('3.0'), 'FIN 129': Decimal('3.0'), 'FIN 150': Decimal('3.0'), 'FIN 170': Decimal('3.0'), 'FIN 193': Decimal('3.0'), 'FIN 197': Decimal('3.0'), 'INS 51': Decimal('3.0'), 'INS 141': Decimal('3.0'), 'INS 161': Decimal('3.0'), 'INS 180': Decimal('3.0'), 'INS 190': Decimal('3.0'), 'IS 44': Decimal('2.0'), 'IS 75': Decimal('3.0'), 'IS 83': Decimal('3.0'), 'IS 107': Decimal('3.0'), 'IS 114': Decimal('3.0'), 'IS 145': Decimal('3.0'), 'IS 150': Decimal('3.0'), 'IS 160': Decimal('3.0'), 'IS 161': Decimal('3.0'), 'MATH 50': Decimal('3.0'), 'MATH 70': Decimal('3.0'), 'MATH 100': Decimal('3.0'), 'MGMT 110': Decimal('3.0'), 'MGMT 120': Decimal('3.0'), 'MGMT 135': Decimal('3.0'), 'MGMT 160': Decimal('3.0'), 'MGMT 170': Decimal('3.0'), 'MGMT 182': Decimal('3.0'), 'MGMT 184': Decimal('3.0'), 'MGMT 185': Decimal('3.0'), 'MKTG 101': Decimal('3.0'), 'MKTG 102': Decimal('3.0'), 'MKTG 104': Decimal('3.0'), 'MKTG 106': Decimal('3.0'), 'MKTG 111': Decimal('3.0'), 'MKTG 113': Decimal('3.0'), 'MKTG 115': Decimal('3.0'), 'MKTG 120': Decimal('3.0'), 'MKTG 130': Decimal('3.0'), 'MKTG 170': Decimal('3.0'), 'STAT 40': Decimal('3.0'), 'STAT 71': Decimal('3.0'), 'STAT 72': Decimal('3.0'), 'STAT 108': Decimal('3.0'), 'STAT 130': Decimal('3.0'), 'STAT 170': Decimal('3.0'), 'STAT 172': Decimal('3.0'), 'STAT 190': Decimal('3.0'), 'ACCT 105': Decimal('3.0'), 'ECON 131': Decimal('3.0')}
This is the dictionary4 required year: {'ACCT 41': None, 'ACCT 42': None, 'ACCT 110': None, 'ACCT 120': None, 'ACCT 165': 'JR', 'ACCT 166': None, 'ACCT 167': None, 'ACCT 175': 'JR', 'ACCT 185': 'JR', 'ACCT 186': 'JR', 'ACTS 50': None, 'ACTS 120': None, 'ACTS 120L': None, 'ACTS 131': None, 'ACTS 131L': None, 'ACTS 135': None, 'ACTS 140': None, 'ACTS 150': None, 'ACTS 155': None, 'ACTS 161': None, 'ACTS 165': None, 'ACTS 190': 'SR', 'BLAW 60': 'SO', 'BLAW 120': None, 'BLAW 180': None, 'BUS 195': 'SR', 'BUS 01': None, 'BUS 02': None, 'BUS 03': None, 'BUS 04': None, 'BUS 05': None, 'BUS 67': None, 'BUS 70': 'SO', 'BUS 73': None, 'BUS 74': None, 'BUS 105': None, 'BUS 120': 'JR', 'BUS 122': 'JR', 'BUS 191': 'SO', 'CS 65': None, 'CS 66': None, 'CS 67': None, 'CS 83': None, 'CS 130': None, 'CS 137': None, 'CS 167': None, 'CS 178': None, 'CS 188': None, 'CS 191': None, 'ECON 02': None, 'ECON 10': None, 'ECON 108': None, 'ECON 109': None, 'ECON 135': None, 'ECON 170': None, 'ECON 173': None, 'ECON 174': None, 'ECON 190': None, 'ENTR 101': 'SO', 'ENTR 150': None, 'ENTR 190': None, 'FIN 101': None, 'FIN 102': None, 'FIN 119': None, 'FIN 121': None, 'FIN 129': None, 'FIN 150': None, 'FIN 170': None, 'FIN 193': None, 'FIN 197': 'SR', 'INS 51': None, 'INS 141': None, 'INS 161': None, 'INS 180': 'SR', 'INS 190': 'SR', 'IS 44': None, 'IS 75': None, 'IS 83': 'SO', 'IS 107': None, 'IS 114': None, 'IS 145': None, 'IS 150': None, 'IS 160': None, 'IS 161': None, 'MATH 50': None, 'MATH 70': None, 'MATH 100': None, 'MGMT 110': 'SO', 'MGMT 120': None, 'MGMT 135': 'JR', 'MGMT 160': None, 'MGMT 170': 'Sr', 'MGMT 182': None, 'MGMT 184': 'JR', 'MGMT 185': 'JR', 'MKTG 101': 'SO', 'MKTG 102': None, 'MKTG 104': None, 'MKTG 106': None, 'MKTG 111': None, 'MKTG 113': None, 'MKTG 115': None, 'MKTG 120': None, 'MKTG 130': None, 'MKTG 170': None, 'STAT 40': None, 'STAT 71': None, 'STAT 72': None, 'STAT 108': None, 'STAT 130': None, 'STAT 170': None, 'STAT 172': None, 'STAT 190': None, 'ACCT 105': None, 'ECON 131': None}
This is the dictionary5 coreq: {'ACCT 41': None, 'ACCT 42': None, 'ACCT 110': None, 'ACCT 120': None, 'ACCT 165': None, 'ACCT 166': None, 'ACCT 167': None, 'ACCT 175': None, 'ACCT 185': None, 'ACCT 186': None, 'ACTS 50': None, 'ACTS 120': 'ACTS 120L', 'ACTS 120L': 'ACTS 120L', 'ACTS 131': 'ACTS 131L', 'ACTS 131L': 'ACTS 131', 'ACTS 135': None, 'ACTS 140': None, 'ACTS 150': None, 'ACTS 155': 'ACTS 150', 'ACTS 161': None, 'ACTS 165': 'ACTS 135', 'ACTS 190': None, 'BLAW 60': None, 'BLAW 120': None, 'BLAW 180': None, 'BUS 195': None, 'BUS 01': None, 'BUS 02': None, 'BUS 03': None, 'BUS 04': None, 'BUS 05': None, 'BUS 67': None, 'BUS 70': None, 'BUS 73': None, 'BUS 74': None, 'BUS 105': None, 'BUS 120': None, 'BUS 122': None, 'BUS 191': None, 'CS 65': None, 'CS 66': None, 'CS 67': None, 'CS 83': None, 'CS 130': None, 'CS 137': None, 'CS 167': None, 'CS 178': None, 'CS 188': None, 'CS 191': None, 'ECON 02': None, 'ECON 10': None, 'ECON 108': None, 'ECON 109': None, 'ECON 135': None, 'ECON 170': None, 'ECON 173': None, 'ECON 174': None, 'ECON 190': None, 'ENTR 101': None, 'ENTR 150': None, 'ENTR 190': None, 'FIN 101': None, 'FIN 102': 'ECON 10, FIN 10, ACTS 135, STAT 71, STAT 130', 'FIN 119': None, 'FIN 121': 'FIN 119, ACTS 120, ACTS 131, STAT 71, STAT 130', 'FIN 129': None, 'FIN 150': None, 'FIN 170': None, 'FIN 193': None, 'FIN 197': None, 'INS 51': None, 'INS 141': None, 'INS 161': None, 'INS 180': None, 'INS 190': None, 'IS 44': None, 'IS 75': None, 'IS 83': None, 'IS 107': None, 'IS 114': None, 'IS 145': None, 'IS 150': None, 'IS 160': None, 'IS 161': None, 'MATH 50': None, 'MATH 70': None, 'MATH 100': 'MATH 70', 'MGMT 110': None, 'MGMT 120': None, 'MGMT 135': None, 'MGMT 160': None, 'MGMT 170': None, 'MGMT 182': None, 'MGMT 184': None, 'MGMT 185': None, 'MKTG 101': None, 'MKTG 102': None, 'MKTG 104': None, 'MKTG 106': None, 'MKTG 111': None, 'MKTG 113': None, 'MKTG 115': None, 'MKTG 120': None, 'MKTG 130': None, 'MKTG 170': None, 'STAT 40': None, 'STAT 71': None, 'STAT 72': None, 'STAT 108': None, 'STAT 130': None, 'STAT 170': None, 'STAT 172': None, 'STAT 190': None, 'ACCT 105': None, 'ECON 131': None}
This is the dictionary6 aoi: {'ART 013': 'Artistic Literacy', 'ART 014': 'Artistic Literacy', 'ART 015': 'Artistic Literacy', 'ART 019': 'Artistic Literacy', 'ART 021': 'Artistic Literacy', 'ART 050': 'Critical Thinking', 'ART 060': 'Artistic Literacy', 'ART 063': 'Artistic Literacy', 'ART 070': 'Artistic Literacy', 'ART 071': 'Artistic Literacy', 'ART 072': 'Artistic Literacy', 'ART 074': 'Artistic Literacy', 'ART 075': 'Historical Foundations', 'ART 078': 'Artistic Literacy', 'ART 079': 'Artistic Literacy', 'ART 090': 'Artistic Literacy', 'ART 099': 'Artistic Literacy', 'ART 103': 'Historical Foundations', 'ART 108': 'Historical Foundations', 'ART 111': 'Critical Thinking', 'ART 112': 'Information Literacy', 'ART 113': 'Artistic Literacy', 'ART 118': 'Historical Foundations', 'ART 119': 'Artistic Literacy', 'ART 145': 'Engaged Citizen', 'ART 150': 'Critical Thinking', 'ART 153': 'Artistic Literacy', 'ART 167': 'Artistic Literacy', 'ART 177': 'Artistic Literacy', 'ART 185': 'Critical Thinking', 'BIO 061': 'Artistic Literacy', 'CHEM 070': 'Artistic Literacy', 'EDUC 113': 'Artistic Literacy', 'ENG 026': 'Artistic Literacy', 'ENG 027': 'Artistic Literacy', 'ENG 041': 'Artistic Literacy', 'ENG 105': 'Artistic Literacy', 'ENG 134': 'Artistic Literacy', 'JMC 058': 'Artistic Literacy', 'JMC 059': 'Artistic Literacy', 'HONR 087': 'Artistic Literacy', 'MUS 011': 'Artistic Literacy', 'MUS 073': 'Artistic Literacy', 'MUS 078': 'Artistic Literacy', 'MUS 080': 'Artistic Literacy', 'MUS 081': 'Global and Cultural Understanding', 'MUS 082': 'Artistic Literacy', 'MUS 119': 'Engaged Citizen', 'MUS 160': 'Historical Foundations', 'PHIL 148': 'Artistic Literacy', 'POLS 109': 'Historical Foundations', 'SPAN 152': 'Global and Cultural Understanding', 'THEA 005': 'Critical Thinking', 'THEA 018': 'Artistic Literacy', 'THEA 030': 'Artistic Literacy', 'THEA 032': 'Artistic Literacy', 'THEA 074': 'Artistic Literacy', 'THEA 076': 'Artistic Literacy', 'THEA 114': 'Artistic Literacy', 'THEA 120': 'Historical Foundations', 'THEA 121': 'Historical Foundations', 'THEA 123': 'Historical Foundations', 'AP - Art': 'Artistic Literacy', 'AP - Music Lit': 'Artistic Literacy', 'AP - Humanities and Fine Arts Subtest': 'Artistic Literacy', 'ACCT 041': 'Critical Thinking', 'ART 082': 'Critical Thinking', 'BIO 099': 'Quantitative Literacy', 'BLAW 060': 'Values and Ethics', 'COUN 224': 'Critical Thinking', 'CS 010': 'Information Literacy', 'CS 065': 'Information Literacy', 'EDUC/STEM 174': 'Critical Thinking', 'EDUC 199/299': 'Global and Cultural Understanding', 'EDUC 199': 'Historical Foundations', 'ENG 030': 'Critical Thinking', 'ENG 037': 'Engaged Citizen', 'ENG 038': 'Written Communication', 'ENG 039': 'Written Communication', 'ENG 081': 'Critical Thinking', 'ENG 102': 'Critical Thinking', 'ENG 107': 'Written Communication', 'ENG 138': 'Engaged Citizen', 'ENG 139': 'Critical Thinking', 'ENG 173': 'Critical Thinking', 'ENG 174': 'Critical Thinking', 'HSCI 060': 'Quantitative Literacy', 'INTD 075': 'Engaged Citizen', 'JMC 076': 'Critical Thinking', 'JMC 130': 'Critical Thinking', 'LPS 135': 'Values and Ethics', 'MATH 025': 'Quantitative Literacy', 'MATH 101': 'Critical Thinking', 'MUS 053': 'Critical Thinking', 'PATH 100': 'Critical Thinking', 'PHAR 117': 'Critical Thinking', 'PHAR 169': 'Critical Thinking', 'PHAR 172': 'Critical Thinking', 'PHAR 173': 'Critical Thinking', 'PHIL 021': 'Critical Thinking', 'PHIL 051': 'Critical Thinking', 'PHIL 090': 'Values and Ethics', 'PHIL 100/RHET 100': 'Critical Thinking', 'PHIL 104': 'Critical Thinking', 'PHIL 106': 'Critical Thinking', 'PHIL 107': 'Critical Thinking', 'PHIL 118': 'Values and Ethics', 'PHIL 124': 'Engaged Citizen', 'PHIL 137': 'Values and Ethics', 'PHIL 138': 'Critical Thinking', 'PHYS 050': 'Critical Thinking', 'POLS 180': 'Critical Thinking', 'POLS 181': 'Critical Thinking', 'PSY 010': 'Critical Thinking', 'PSY 024/BIO 025': 'Critical Thinking', 'PSY 030': 'Critical Thinking', 'SCSA 156': 'Critical Thinking', 'SCSS 082': 'Critical Thinking', 'SCSS 133': 'Critical Thinking', 'SCSS 135': 'Critical Thinking', 'SCSS 151': 'Critical Thinking', 'SCSS 158': 'Critical Thinking', 'SCSS 159': 'Critical Thinking', 'SCSS 196/SCS 196/PSY 194': 'Critical Thinking', 'STAT 060': 'Quantitative Literacy', 'STAT 072': 'Quantitative Literacy', 'STEM 199': 'Critical Thinking', 'BIO 108': 'Engaged Citizen', 'BUS 067/HIST 067': 'Engaged Citizen', 'ECON 108/ENSS 108': 'Engaged Citizen', 'ECON 109': 'Engaged Citizen', 'ECON 115': 'Engaged Citizen', 'ECON 120': 'Engaged Citizen', 'EDUC 140': 'Engaged Citizen', 'EDUC 185': 'Engaged Citizen', 'ENG 069': 'Engaged Citizen', 'ENG 070': 'Engaged Citizen', 'ENG 083': 'Engaged Citizen', 'ENG 121': 'Engaged Citizen', 'ENG 199': 'Written Communication', 'ENSP 50': 'Engaged Citizen', 'ENSP 051/PHSC 051': 'Engaged Citizen', 'ENSP 055': 'Life/Behavioral Science', 'ENSS 50': 'Life/Behavioral Science', 'ENSS 119': 'Life/Behavioral Science', 'HIST 168': 'Engaged Citizen', 'HIST 170': 'Engaged Citizen', 'HIST 188': 'Engaged Citizen', 'HONR 140/REL 155': 'Engaged Citizen', 'HSCI 106': 'Engaged Citizen', 'INTD 050': 'Engaged Citizen', 'INTD 085': 'Historical Foundations', 'INTD 087': 'Engaged Citizen', 'INTD 150': 'Engaged Citizen', 'JMC 066': 'Engaged Citizen', 'JMC 084': 'Engaged Citizen', 'JMC 085': 'Engaged Citizen', 'LEAD 100': 'Engaged Citizen', 'LIBR 085': 'Information Literacy', 'LIB 099': 'Engaged Citizen', 'LPS 100': 'Engaged Citizen', 'LPS 138': 'Engaged Citizen', 'PHIL 151': 'Values and Ethics', 'POLS 075': 'Engaged Citizen', 'POLS 113': 'Engaged Citizen', 'POLS 114': 'Engaged Citizen', 'POLS 115': 'Engaged Citizen', 'POLS 116': 'Engaged Citizen', 'ARAB 002': 'Global and Cultural Understanding', 'ARAB 052': 'Global and Cultural Understanding', 'ART 104': 'Historical Foundations', 'ASL 002': 'Global and Cultural Understanding', 'ASL 070': 'Global and Cultural Understanding', 'BIO 111': 'Life/Behavioral Science', 'BUS 67/HIST 67/HONRS65': 'Global and Cultural Understanding', 'BUS 70': 'Global and Cultural Understanding', 'BUS 198': 'Global and Cultural Understanding', 'CHIN 002': 'Global and Cultural Understanding', 'CHIN0 52': 'Global and Cultural Understanding', 'COUN 145/245': 'Historical Foundations', 'ECON 135': 'Global and Cultural Understanding', 'EDUC 164/264': 'Global and Cultural Understanding', 'EDU 189': 'Values and Ethics', 'ENG 20': 'Global and Cultural Understanding', 'ENG 60': 'Global and Cultural Understanding', 'ENG 65': 'Global and Cultural Understanding', 'ENG 071': 'Global and Cultural Understanding', 'ENG 079': 'Global and Cultural Understanding', 'ENG 158/HONS 175': 'Global and Cultural Understanding', 'ENG 164': 'Global and Cultural Understanding', 'ENG 165': 'Global and Cultural Understanding', 'ENG 168': 'Global and Cultural Understanding', 'FREN 002': 'Global and Cultural Understanding', 'FREN 052': 'Global and Cultural Understanding', 'FREN 151': 'Global and Cultural Understanding', 'FREN 152': 'Global and Cultural Understanding', 'GERM 002': 'Global and Cultural Understanding', 'GERM 052': 'Global and Cultural Understanding', 'GERM 151': 'Global and Cultural Understanding', 'HSCI 104': 'Global and Cultural Understanding', 'HIST 021': 'Historical Foundations', 'HIST 022': 'Historical Foundations', 'HIST 60': 'Global and Cultural Understanding', 'HIST 123': 'Historical Foundations', 'HIST 124': 'Historical Foundations', 'HIST 125': 'Historical Foundations', 'HIST 126': 'Historical Foundations', 'HIST 128': 'Historical Foundations', 'HIST 129': 'Historical Foundations', 'HIST 135': 'Historical Foundations', 'HIST 136': 'Historical Foundations', 'HIST 138': 'Historical Foundations', 'HIST 152': 'Historical Foundations', 'HIST 156': 'Global and Cultural Understanding', 'HIST 176': 'Historical Foundations', 'HSC 106': 'Global and Cultural Understanding', 'JAPN 002': 'Global and Cultural Understanding', 'JAPN 052': 'Global and Cultural Understanding', 'JMC 133': 'Global and Cultural Understanding', 'LEAD 110': 'Global and Cultural Understanding', 'POLS 065': 'Global and Cultural Understanding', 'POLS 121': 'Engaged Citizen', 'POLS 126': 'Global and Cultural Understanding', 'POLS 127': 'Engaged Citizen', 'POLS 129': 'Engaged Citizen', 'POLS 139': 'Engaged Citizen', 'POLS 162': 'Engaged Citizen', 'POLS 174': 'Engaged Citizen', 'REL 003': 'Global and Cultural Understanding', 'REL 62': 'Global and Cultural Understanding', 'REL 64': 'Global and Cultural Understanding', 'REL 67/HONRS 089': 'Global and Cultural Understanding', 'REL 114': 'Global and Cultural Understanding', 'REL 121/PHIL 121': 'Global and Cultural Understanding', 'REL 124': 'Global and Cultural Understanding', 'REL 125/PHIL 125': 'Global and Cultural Understanding', 'REL 151/SCSA 196': 'Global and Cultural Understanding', 'SCSA 002': 'Global and Cultural Understanding', 'SCSA 180': 'Global and Cultural Understanding', 'SCSS 20': 'Global and Cultural Understanding', 'SPAN 002': 'Global and Cultural Understanding', 'POLS 124': 'Engaged Citizen', 'POLS 125': 'Values and Ethics', 'POLS 128': 'Engaged Citizen', 'POLS 151': 'Engaged Citizen', 'POLS 152': 'Engaged Citizen', 'POLS 153': 'Engaged Citizen', 'POLS 155': 'Engaged Citizen', 'POLS 156': 'Engaged Citizen', 'POLS 157': 'Engaged Citizen', 'POLS 160': 'Engaged Citizen', 'POLS 163': 'Engaged Citizen', 'POLS 165': 'Engaged Citizen', 'POLS 166': 'Engaged Citizen', 'POLS 167': 'Engaged Citizen', 'POLS 168': 'Engaged Citizen', 'POLS 170': 'Engaged Citizen', 'POLS 171': 'Engaged Citizen', 'POLS 173': 'Values and Ethics', 'POLS 176': 'Engaged Citizen', 'POLS 179': 'Engaged Citizen', 'POLS 183': 'Engaged Citizen', 'POLS 185': 'Engaged Citizen', 'POLS 186': 'Engaged Citizen', 'POLS 189': 'Engaged Citizen', 'POLS 190': 'Engaged Citizen', 'PSY 134': 'Engaged Citizen', 'REL 120': 'Engaged Citizen', 'SCSS 071/ENSP 071': 'Engaged Citizen', 'SCS
"""

# Given requirements dictionary
requirements = {
   "acct 41": [],
   "acct 42": ["acct 41"],
   "fin 101": ["acct 42", "is 44", "econ 2", "acts 131"],
   "bus 195": ["fin 101", "mktg 101", "mgmt 110", "mgmt 120"],
   "acts 131": ["math 70"],
   "acts 135": ["acts 131"],
   "stat 170": ["stat 40", "acts 135"],
   "acts 150": ["acts 120", "acts 131"],
   "mgmt 120": ["acts 135"],
   "acts 161": ["acts 131"],
   "is 44": [],
   "econ 2": [],
   "mktg 101": ["econ 2"],
   "mgmt 110": [],
   "mgmt 120": ["acts 135"],
   "math 50": [],
   "math 70": ["math 50"],
   "stat 40": [],
   "acts 120": ["math 70"]
}

def Jplacement_algorithm(requirements, dict_2, dict_7, startingSemester):
    startingSemesterYear = startingSemester.split(" ")
    # Calculate prerequisite dictionary 
    prereq_dict = class_prereqs_score(requirements)

    # Calculate post-requisite dictionary 
    postreq_dict = class_is_prereq_score(requirements)[0]

    # Print the outputs
    print("Prerequisite Dictionary:")
    print(prereq_dict)
    print("\nPost-Requisite Dictionary:")
    print(postreq_dict)

    spots_dict = {}

    for course in requirements:

        prereq_score = prereq_dict[course]
        postreq_score = postreq_dict[course]
        yearOfferings = dict_7[course]
        
        fit = 1
        fits_arr = []

        # Loop to find available semesters for the course based on course type
        while fit <= 8:
            if fit >= prereq_score and fit <= 8 - postreq_score + 1:
                if "Fall" in startingSemester:
                    if int(dict_2[course][0])==1 and fit % 2 != 0: #offered fall, fall semester
                        fits_arr.append(fit) #that works
                    elif int(dict_2[course][1])==1 and fit % 2 == 0: #offered spring, spring semester
                        fits_arr.append(fit) #that works
                    
                    #check if classes are offered in odd/even years and adjust accordingly
                    
                    if int(startingSemesterYear[1]) % 2 == 0: #semesters 1, 4, 5, and 8 are in even years
                        if yearOfferings[0] == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [2,3,6,7]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #remove all odd year semesters from fits_arr
                        if yearOfferings[1] == 0: # if the course isn't offered in even years
                            for evenYrSemester in [1,4,5,8]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #make it not fit in any even year semesters
                                
                    else: #semesters 2, 3, 6, and 7 are in even years
                        if yearOfferings[1] == 0: # if the course isn't offered in even years
                            for evenYrSemester in [2,3,6,7]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #remove all even year semesters from fits_arr
                        if yearOfferings[0] == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [1,4,5,8]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #make it not fit in any odd year semesters
                        
                else:
                    if int(dict_2[course][0])==1 and fit % 2 == 0: #offered fall, fall semester
                        fits_arr.append(fit) #that works
                    elif int(dict_2[course][1])==1 and fit % 2 != 0: #offered spring, spring semester
                        fits_arr.append(fit) #that works
                        
                    #check if classes are offered in odd/even years and adjust accordingly
                        
                    if int(startingSemesterYear[1]) % 2 == 0: #semesters 1, 2, 5, and 6 are in even years
                        if yearOfferings[0] == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [3,4,7,8]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #remove all odd year semesters from fits_arr
                        if yearOfferings[1] == 0: # if the course isn't offered in even years
                            for evenYrSemester in [1,2,5,6]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #make it not fit in any even year semesters
                                
                    else: #semesters 3, 4, 7, and 8 are in even years
                        if yearOfferings[1] == 0: # if the course isn't offered in even years
                            for evenYrSemester in [3,4,7,8]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #remove all even year semesters from fits_arr
                        if yearOfferings[0] == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [1,2,5,6]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #make it not fit in any odd year semesters
            fit += 1
        spots_dict[course] = fits_arr
        
        spots_dict[course] = {'fits': fits_arr}
        # implement sometihng like this when aoi tracker is fixed
        #spots_dict[course] = {'type': course_type, 'fits': fits_arr}

    # Separate AOI courses, electives, and required courses
    #aoi_courses_dict = {}
    #elective_courses_dict = {}
    #required_courses_dict = {}

    # Using for loops to populate the dictionaries based on conditions
    """for k, v in spots_dict.items():
    if v['type'] == 'aoi':
        aoi_courses_dict[k] = v
    elif v['type'] == 'elective':
        elective_courses_dict[k] = v
    elif v['type'] == 'required':
        required_courses_dict[k] = v
    """
    # Fill semester lists for required courses first
    semester_lists = {}

    # Using a for loop to fill the dictionary
    for i in range(1, 9):
        semester_lists[i] = []
    # Initialize semester lists

    # Function to fill semester lists with courses
    def fill_semester_lists(course_dict, semester_lists, credits_left):
        for course, info in course_dict.items():
            #course,info are variable used to iterate
            #course_dict.items are the value (of key:value pairs) of spots_dict = semster numbers avaliable
            fits_arr = info['fits']
            #? what is this
            for semester in fits_arr:
                if credits_left[semester] >= 3:
                    semester_lists[semester].append(course)
                    credits_left[semester] -= 3
                    break

    # Fill semester lists for required courses
    credits_left = {i: 12 for i in range(1, 9)}  # Initialize credits left for each semester
    fill_semester_lists(spots_dict, semester_lists, credits_left)

    # Fill semester lists for AOI courses
    """for course, info in aoi_courses_dict.items():
    fits_arr = info['fits']
    for semester in fits_arr:
        if credits_left[semester] >= 3:
            semester_lists[semester].append(course)
            credits_left[semester] -= 3
            break
    """
    # Fill remaining spots with electives and placeholders
    placeholder_course = "Placeholder"
    remaining_elective_slots = sum(credits_left.values()) // 3  # Calculate the number of elective slots remaining
    elective_slots_filled = 0
    for semester, slots_left in credits_left.items():
        while slots_left >= 3 and elective_slots_filled < remaining_elective_slots:
            semester_lists[semester].append(placeholder_course)
            elective_slots_filled += 1
            slots_left -= 3

    # Print the filled semester lists
    print("Semester Lists:")
    semesterLists = [0]
    for semester, courses in semester_lists.items():
        print(f"Semester {semester}: {courses}")
        semesterLists.append(courses)

    

    #Print the elective courses
    """
    print("\nElective Courses:")
    for course, info in elective_courses_dict.items():
    fits_arr = info['fits']
    print(f"{course}: Available in semesters {fits_arr}")
    """
    
    return semesterLists

#print(function1 (requirements))