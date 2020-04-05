# UTILS MODULE


# Support function for creating one array with one array in each index with period,demand
# ex : [[1,2] , [2,3], ...]
def createarraywithtuplespm(first, second):
    array = []
    for f, s in zip(first, second):
        array.append((f, s))

    return array
