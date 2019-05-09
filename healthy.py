from pymongo import MongoClient
from bson.objectid import ObjectId


mongo_uri = 'mongodb+srv://admin:admin@cluster0-aekow.mongodb.net/test?retryWrites=true'
client = MongoClient(mongo_uri)

db = client.database

Myfood = db['my_food']

# food_document = [
#     {
#     'image':'ga.jpg',
#     'title':'Cơm gạo lứt, thịt gà sốt Leekumki',
#     'price':'70.000 VND',
#     'resources':'150gr cơm gạo lứt,150gr thịt ức gà, 200gr rau củ',
#     'calo':'388',
#     'carb':'44,4 gr',
#     'protein':'36,4 gr',
#     'fat':'6,2 gr'
#     },
#     {
#     'image':'thitlon.jpg',
#     'title':'Cơm gạo lứt, thịt heo sốt Teriyaki',
#     'price':'70.000 VND',
#     'resources':'150gr cơm gạo lứt, 150gr thịt heo, 200gr rau củ',
#     'calo':'374',
#     'carb':'44,4 gr',
#     'protein':'36,4 gr',
#     'fat':'4,7 gr'
#     },
#     {
#     'image':'trung.jpg',
#     'title':'Cơm gạo lứt, trứng thịt băm cốt dừa',
#     'price':'50.000 VND',
#     'resources':'150gr cơm gạo lứt, 200gr trứng thịt băm,200gr rau củ',
#     'calo':'525',
#     'carb':'50,3 gr',
#     'protein':'24,7 gr',
#     'fat':'22,6 gr'
#     },
#     {
#     'image':'ca.jpg',
#     'title':'Cơm gạo lứt, cá phi lê hấp tương gừng',
#     'price':'60.000 VND',
#     'resources':'150gr cơm gạo lứt, 200gr cá, 200gr rau củ',
#     'calo':'410',
#     'carb':'44,4 gr',
#     'protein':'44,3 gr',
#     'fat':'6,3 gr'
#     },
#     {
#     'image':'thitvien.jpg',
#     'title':'Cơm gạo lứt, thịt thăn heo viên hấp',
#     'price':'60.000 VND',
#     'resources':'150gr cơm gạo lứt , 200gr thịt băm viên,200gr rau củ ',
#     'calo':'488',
#     'carb':'44,4 gr',
#     'protein':'43,9 gr',
#     'fat':'15,7 gr'
#     },
#     {
#     'image':'bo.jpg',
#     'title':'Cơm gạo lứt, thịt bò kho vang đỏ',
#     'price':'70.000 VND',
#     'resources':'150gr cơm gạo lứt, 150gr thịt bò, 200gr rau củ',
#     'calo':'429',
#     'carb':'44,4 gr',
#     'protein':'55,9 gr',
#     'fat':'10,7 gr'
#     },
#     {
#     'image':'combo.jpg',
#     'title':'Cơm trắng, thịt bò xào',
#     'price':'50.000 VND',
#     'resources':'300gr cơm trắng,150gr thịt bò ,100gr dưa chuột',
#     'calo':'707',
#     'carb':'90 gr',
#     'protein':'58 gr',
#     'fat':'9,6 gr'
#     },
#     {
#     'image':'comga.jpg',
#     'title':'Cơm trắng, thịt gà sốt Leekumki',
#     'price':'50.000 VND',
#     'resources':'300gr cơm trắng, 200gr thịt gà , 250gr súp lơ',
#     'calo':'690',
#     'carb':'88,2 gr',
#     'protein':'52,8 gr',
#     'fat':'7,3 gr'
#     },
#     {
#     'image':'tom.jpg',
#     'title':'Cơm trắng, tôm hấp',
#     'price':'60.000 VND',
#     'resources':'300gr cơm trắng,200gr tôm, 150gr rau',
#     'calo':'615',
#     'carb':'91 gr',
#     'protein':'51,7 gr',
#     'fat':'2,8 gr'
#     },
#     {
#     'image':'comga2.jpg',
#     'title':'Cơm trắng, thịt gà rang',
#     'price':'60.000 VND',
#     'resources':'300gr cơm trắng, 200gr thịt gà, 150gr đỗ xào',
#     'calo':'655',
#     'carb':'91 gr',
#     'protein':'51,9 gr',
#     'fat':'6,6 gr'
#     },
#     {
#     'image':'comca.jpg',
#     'title':'Cơm trắng, cá kho',
#     'price':'50.000 VND',
#     'resources':'300gr cơm trắng,200gr thịt bò,150gr đỗ xào',
#     'calo':'605',
#     'carb':'89,8 gr',
#     'protein':'55,4 gr',
#     'fat':'0,6 gr'
#     },
#     {
#     'image':'bittet.jpg',
#     'title':'Cơm trắng, thịt bò bít tết',
#     'price':'80.000 VND',
#     'resources':'300gr cơm trắng,150gr thịt bò,100gr dưa chuột',
#     'calo':'695',
#     'carb':'91 gr',
#     'protein':'58 gr',
#     'fat':'9,4 gr'
#     }
# ]

# Myfood.insert_many(food_document)

