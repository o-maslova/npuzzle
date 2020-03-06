from django.http import HttpResponse, JsonResponse


def parse_line(line, num):
    tmp_dict = {}
    i = 0
    while i < num:
        if i + 1 == num:
            tmp_dict[i] = line[i][1:-1].split(',')
        else:
            tmp_dict[i] = line[i][1:].split(', ')
        i += 1
    return tmp_dict


def solving(request):

    with open('../test', 'r') as fd:
        line = fd.readline()
        lst = {}
        i = 0
        lst['num_of_squares'] = len(line.split('],'))
        lst['steps'] = []
        print(lst)
        while line:
            line = line[1:-2]
            line = line.split('], ')
            lst['steps'].append({'step': i,
                                 'state': parse_line(line=line, num=lst['num_of_squares'])
                                 })
            i += 1
            line = fd.readline()
    print(lst)
    return JsonResponse(lst, safe=False)
