precios_licores = [
("Ron", 50000),
("Vodka", 40000),
("Ginebra", 60000),
("Whisky", 80000),
({"hola":12}, {
   "club":1000,
   "red":12333,
   "stella":19000
}),
("Tequila",1222),
("Brandy", 55000),
("Cognac", 90000),
("Licor de café", 45000),
]
a=dict(precios_licores)
print("las cervezas disponibles")
for i in a["Cerveza"].keys():
   print(i)


# print(precios_licores)