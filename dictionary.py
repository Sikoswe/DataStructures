fredrick = {"name":"fredrick","age":42,"nationality":"zambian"}
print(fredrick["age"])
print(type(fredrick["nationality"]))





# diferentiate between list and a dictionary, citing two examples.
mwansa = {"mary":"tricia","bill":"rule","chama":"lusaka"}
print(mwansa["bill"])


sikoswe = {"name":"ftredrick","surnane":"sikoswe","gender":"male","age":"55","school":"namalundu"}
print(sikoswe["gender"])

mwewa = {"name":"david","surname":"mwewa","gender":"male","age":"42","school":"kabwe"}
print(mwewa["age"])


mweemba = {"name":"sharoty","surname":"mweemba","gender":"female","age":"12","school":"siavonga"}
print(mweemba["name"])



myfamily = {
"child1" : {
     "name" : "elton",
     "year" : 2000
     },

"child2" : {
    "name" : "mwiya",
    "year" : 2008
     },

"child3" : {
    "name" : "mwansa",
    "year" : 2019
    }
}
print(myfamily["child3"])


namm = {'myfamily':[{"child1" : {
     "name" : "elton",
     "year" : 2000
     },"child2" : {
    "name" : "mwiya",
    "year" : 2008
     },
"child3" : {
    "name" : "mwansa",
    "year" : 2019
    }},{}]}
print(namm["myfamily"][1])





sikoswe1 = {
    'my_family':[
            {
            "name" : "Emil",
            "year" : 2004
        },
        {
            "name" : "Tobias",
            "year" : 2007
        },
        {
            "name" : "Linus",
            "year" : 2011
        }
            
        ]
}
print(sikoswe1["my_family"][2])