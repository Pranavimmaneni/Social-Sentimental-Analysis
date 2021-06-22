# Social-Sentimental-Analysis

## Application Link
http://socialsentimental-analysis.herokuapp.com/

## API Usage

API Link : https://2uoffcsokj.execute-api.us-east-1.amazonaws.com/development

*Body Parameter*:
```
{
    "hashtag": "telstra",
}
```
**Request URL**: https://2uoffcsokj.execute-api.us-east-1.amazonaws.com/development/tweet-data?hashtag=telstra

*Response*:
```
{
    "HashTag": "#Telstra",
    “Date/Time”: “2021-06-21 17:39:38”,
    "Name": "David White",
    “Screen Name”: “david0102”,
    "Sex": "Male",
    “Location”: “Australia”
    “Description”: “I love Telstra products and
    services”,
    “Sentiment”: “Positive”
}
```

## Clone & Use
1. Clone the repository.
2. Navigate to the 'app' directory.
3. Run command : `npm init`
4. Install dependencies : `npm install express request ejs --save`
5. Install and use nodemon : `npm install --save-dev nodemon`
6. In the package.json file, add `"start": "nodemon app.js"` under `scripts`
```
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon index.js"
  },
```
7. Run the file using the command : `npm start`
8. Test the API on http://localhost:3000/
