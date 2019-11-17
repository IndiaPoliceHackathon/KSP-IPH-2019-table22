import json

overall_score = 0
complete_list = []
priority_dict = {'id':0, 'snippet':"", 'visible_link':""}

with open('sumukh.json') as j_handler:
    a = []
    data = json.load(j_handler)
    query_full = data[0]["query"]
    query = (query_full.split())[0:2]
    first_name = query[0]
    print(query[0])
    try:
        last_name = list(query[1])
    except:
        last_name = list("asdfghjklasdfghjkasdfghjklsadfghjklasdfghjk")
    print(query[1])
    results = data[0]["results"]
    index = 0
    for i in results:
        overall_score = 0
        j = i['snippet'].split()
        if((last_name in j) or (first_name in j)):
            if (first_name in j):
                overall_score += 1

            if (last_name in j):
                overall_score += 0.5

            if(overall_score >= 0.75):
                a.append(index)
                print('enter')
                # priority_dict['id'] = i['id']
                # priority_dict['snippet'] = i['snippet']
                # priority_dict['visible_link'] = i['visible_link']
                # complete_list.append(priority_dict)
        index = index + 1
    for index in a:
        # print(index)
        # print(k)
        print(results[index])
        complete_list.append(results[index])
        

            




            



    



