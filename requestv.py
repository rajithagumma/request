import requests,json
def request():
    x=requests.get("http://saral.navgurukul.org/api/courses")
    with open("raj.json","w") as f:
        json.dump(x.json(),f,indent=4)
    with open("raj.json","r") as f:
        data=json.load(f)
    a=[]
    c=0
    for i in data[ "availableCourses"]:
        c+=1
        print(c,i["name"],"=",i["id"])
        a.append(int(i["id"]))
    print()
    choose=int(input("select you choice:-"))-1
    if choose in a:
        at=requests.get("http://saral.navgurukul.org/api/courses/"+str(a[choose])+"/exercises")
        T=at.json()
        slug=[]
        h=0
        j=0
        while j<len(T["data"]):
            print(h+1,"=",T["data"][j]["name"])
            slug.append(T["data"][j]["slug"])
            h=h+1
            j=j+1 
        slugname=int(input("enter your slug number:-"))
        list=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"/exercise/getBySlug?slug="+slug[slugname])
        t=list.json()
        print(t["name"])
        print(t["slug"])
        print("content",t["content"])   
    else:
        print("your course number does not exist")
request()