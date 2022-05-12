const EmlParser = require('eml-parser');
var AWS = require('aws-sdk');
var s3 = new AWS.S3({ region: process.env.AWS_REGION });
var document_client = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {

    var response = new Object();

    for (let i of event.Records) {

        try {

            let bucket_name = i["s3"]["bucket"]["name"];
            let object_key = i["s3"]["object"]["key"];

            let s3_object = await get_s3_object(bucket_name, object_key);
            let email_data = await parse_email(s3_object);
            await put_item_dynamodb(email_data);
            await delete_s3_object(bucket_name,object_key);

        }
        catch (e) {
            console.error(e);
            response.statusCode = 500;
        }

    }

    response.statusCode = 200;
    response.body = true;

    return response;
};

async function get_s3_object(bucket_name, object_key) {

    var params = {
        Bucket: bucket_name,
        Key: object_key
    };

    return new Promise((resolve, reject) => {
        s3.getObject(params, (err, data) => {
            if (err) {
                console.error("error", err);
                reject(err);
            }
            else resolve(data.Body);
        });

    });

}

async function delete_s3_object(bucket_name, object_key) {

    var params = {
        Bucket: bucket_name,
        Key: object_key
    };

    return new Promise(async (resolve, reject) => {
        await s3.deleteObject(params, (err, data) => {
            if (err) {
                console.error("delete object error: ", err);
                reject(err);
            }
            else resolve(data);
        });
    });

}

async function put_item_dynamodb(data) {

    var db_params = {
        TableName: process.env.EMAIL_TABLE,
        Item: data,
    };
    return new Promise((resolve, reject) => {
        document_client.put(db_params, function(err, data) {
            if (err) {
                console.error("Error Details:", err);
                reject(err);
            }
            else resolve(data);
        });

    });

}

async function parse_email(raw_object) {

    let email_response = new EmlParser(raw_object).parseEml();
    let email_data = await email_response;
    email_data.flagged = false;
    email_data.folder = null;
    email_data.updated_by = "LAMBDA";
    email_data.is_read = false;
    email_data.timestamp = new Date().getTime();
    email_data.username = email_data.to.text;
    return email_data;

}