from flask import Flask,request
from flask_restful import Resource ,Api,reqparse

app = Flask(__name__)
api =  Api(app)

parser = reqparse.RequestParser()

parser.add_argument('num')

def bubblesort(alist):
    length = len(alist) - 2
    unsorted = True

    while unsorted:
        for element in range(0,length):
            unsorted = False

            if alist[element] > alist[element + 1]:
                hold = alist[element + 1]
                alist[element + 1] = alist[element]
                alist[element] = hold
                unsorted = True
    return alist


def quicksort(alist):
    if len(alist) == 1 or len(alist) == 0:
        return alist
    else:
        pivot = alist[0]
        i = 0
        for j in range(len(alist)-1):
            if alist[j+1] < pivot:
                alist[j+1],alist[i+1] = alist[i+1], alist[j+1]
                i += 1
        alist[0],alist[i] = alist[i],alist[0]
        first_part = quicksort(alist[:i])
        second_part = quicksort(alist[i+1:])
        first_part.append(alist[i])
        return first_part + second_part

    return alist
	
def mergesort(alist):
    result = []
    if len(alist) < 2:
        return alist
    mid = int(len(alist)/2)
    y = mergesort(alist[:mid])
    z = mergesort(alist[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result

    return alist

class bubblesort(Resource):
		def post(self):
			args = parser.parse_args()
			data = strZargs['num']
			data = data.split(',')
			data = map(int,data)
			return {"result":BubbleSort(data)}

class quicksort(Resource):
		def post(self):
			args = parser.parse_args()
			data = strZargs['num']
			data = data.split(',')
			data = map(int,data)
			return {"result":QuickSort(data)}
			
class mergesort(Resource):
		def post(self):
			args = parser.parse_args()
			data = strZargs['num']
			data = data.split(',')
			data = map(int,data)
			return {"result":Mergesort(data)}
			
			
api.add_resource(bubblesort,'/api/bubblesort')
api.add_resource(quicksort,'/api/quicksort')
api.add_resource(mergesort,'/api/mergesort')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5001)
