from django.shortcuts import render
from django.http import HttpResponse

def parse_line(line):
    line = line[1:-2]
    line_lst = line.split('],')


def index(request):

    with open('../test', 'r') as fd:
        line = fd.readline()
        lst = []
        num_of_squares = len(line.split('],'))
        while line:
            line = line[1:-2]
            # print(line)
            lst.append([elem.strip('[]') for elem in line.split(', ')])
            line = fd.readline()
    print(lst)
    return HttpResponse(lst, content_type="application/json")
    # return render(request, 'index.html')
