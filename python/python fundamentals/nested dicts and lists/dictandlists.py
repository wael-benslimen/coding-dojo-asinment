x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]= 15
students[1]["last_name"] = "brayent"
sports_directory['soccer'][0] = "andreas"
z[0]['y'] = 30
########################################
students1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
     for i in range(len(list)):
         print(f"first_name - {list[i]['first_name']} ,last_name {list[i]['last_name']}")
    
iterateDictionary(students1) 
########################################
def iterateDictionary2(key_name, list):
    for i in range(len(list)):
        print(list[i][str(key_name)])
        
iterateDictionary2('first_name', students1)
########################################
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(key)
        print(len(some_dict[key]))
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
    
printInfo(dojo)
