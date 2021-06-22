var express = require("express");
var app = express();
var request = require("request");

app.set("view engine","ejs");

app.get("/",function(req,res){
    res.render("search");
});

function sexCount(arr, grp) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i]["Sex"] == grp) {
            count++;
        }
    }
    return count;
}

function locationCount(arr, grp) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i]["Location"] == grp) {
            count++;
        }
    }
    return count;
}

function sentimentCount(arr, grp) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i]["Sentiment"] == grp) {
            count++;
        }
    }
    return count;
}

app.get("/results",function(req,res){
    var query = req.query.search;
    var url = "https://2uoffcsokj.execute-api.us-east-1.amazonaws.com/development/tweet-data?hashtag=" + query;
    request(url,function(error, response, body){
        if(!error && response.statusCode == 200){
            var data = JSON.parse(body);
            var male = sexCount(data["body"],"Male")
            var female = sexCount(data["body"],"Female")
            var ind = locationCount(data["body"],"India")
            var aus = locationCount(data["body"],"Australia")
            var uk = locationCount(data["body"],"United Kingdom")
            var us = locationCount(data["body"],"United States")
            var sig = locationCount(data["body"],"Singapore")
            var other = locationCount(data["body"],"Others")
            var pos = sentimentCount(data["body"],"POSITIVE")
            var neg = sentimentCount(data["body"],"NEGATIVE")
            var neu = sentimentCount(data["body"],"NEUTRAL")
		    res.render("results",{data: data,male: male,female: female,ind: ind,aus: aus,uk: uk,us: us,sig: sig,other: other,pos: pos,neg: neg,neu: neu});
        }
    })
});

app.get("/documentation", function(req,res){
    res.render("documentation");
})

const port = process.env.PORT || 3000;

app.listen(port,function(){
    console.log("App has started!");
});
