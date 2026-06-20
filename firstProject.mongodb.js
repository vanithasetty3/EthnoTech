use("kasv")
//db["bike"].find()


/*db.train.insertMany([{
    type:"Bharath express",
    colour:"blue",
    price:200000000
}
{
    type:"zuha express",
    colour:"royal blue",
    price:400000000,
    capacity:400
}])*/

//db["train"].find({colour:"red"});
//db.bike.find({price:{$gt:100000}});
//db.car.find({colour:"black"});
//db.bike.find({},{brand:1,model:1,price:1});
//db.car.updateOne({brand:"Thar"},{$inc:{price:9999}});
//db.car.updateOne({brand:"ford"},{$set:{tags:["logo"]}});
//db.car.updateOne({brand:"bmw"},{$set:{tags:["logo"]}});
db.car.deleteOne({brand:"ford"});