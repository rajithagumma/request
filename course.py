import requests,json
re=requests.get("https://saral.navgurukul.org/api/courses")
f=open("course.json","w")
json.dump(re.json(),f,indent=4)
f=open("course.json","r")
data=json.load(f)
d=[]
i=1
for j in data["availableCourses"]:
    print(i,j["name"],j["id"])
    d.append(int(j["id"]))
    i=i+1
# print(d)
choice=int(input("enter the id number:-"))
if choice in d:
    
    file=requests.get("http://saral.navgurukul.org/api/courses/"+str(choice)+"/exercises")
    r=file.json() 
    # f2=open("course1.json","w")
    # json.dump(file.json(),f2,indent=4)
    slug=[]
    h=0
    k=0
    while k<len(r["data"]):
        print(h+1,"=",r["data"][k]["name"])
        slug.append(r["data"][k]["slug"])
        h=h+1
        k=k+1 
    slugname=int(input("enter your slug number:-"))
    list=requests.get("http://saral.navgurukul.org/api/courses/"+str(choice)+"/exercise/getBySlug?slug="+slug[slugname])
    # file2=open("course3.json","w")
    # json.dump(list.json(),file2,indent=4)

    t=list.json()
    print(t["name"])
    print(t["slug"])
    print("content",t["content"])   
else:
    print("your course number does not exist")
