# example of dictionary

student1 = {
    "name":"Andrew",
    "age" : 45,
    "address":{
        "city":"Indore"
    }
}
print("Name : ",student1["name"]);
print("Age : ",student1["age"]);
print("City : ",student1["address"]["city"]);

student2 = dict(name="Andrew",age=45)
print("Name : ",student2["name"]);
print("Age : ",student2["age"]);

student3 = dict({
    "name":"Andrew",
    "age" : 45
})
print("Name : ",student3["name"]);
print("Age : ",student3["age"]);


