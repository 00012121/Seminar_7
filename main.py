# eng2uz = dict()
# eng2uz = {'bir': 'one'}
# student = {'name': 'Azizbek',
#            'id': '00012121',
#            'course': 'BIS'}
#
#
# print(eng2uz)
# print(student)
# print(len(student))
# print('one' in eng2uz)
# print('course' in student)
#
# vals = eng2uz.values()
#
# print('bir' in vals)

# myFinalMarks = {'CSF': 75,
#                 'FunPro': 80,
#                 'WT': 85}
#
#
# def calculateAverage(myFinalMarks):
#     total = 0
#
#     for key in myFinalMarks:
#         total = total + myFinalMarks[key]
#
#     average = total / len(myFinalMarks)
#     return average
#
#
# print(calculateAverage(myFinalMarks))


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('brontosaurus')
print(h)
