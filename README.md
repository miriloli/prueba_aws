# AWS API Project Documentation

## Project Description

The AWS API project is a REST API developed using the AWS Serverless service. It provides functionalities to manage company favorites.

## Usage Instructions

### Get All Favorites of a Company

To get all favorites of a company, make a GET request to the following URL:

[https://ng5m0uh5s7.execute-api.eu-north-1.amazonaws.com/dev/companies/{id}/favorites](https://ng5m0uh5s7.execute-api.eu-north-1.amazonaws.com/dev/companies/{id}/favorites)

Replace `{id}` with the desired company ID (1-10).

#### Request Example

```bash
GET https://ng5m0uh5s7.execute-api.eu-north-1.amazonaws.com/dev/companies/1/favorites
´´´
### Add a Favorite to a Company

To add a favorite to a company, make a POST request to the following URL:

[https://ng5m0uh5s7.execute-api.eu-north-1.amazonaws.com/dev/companies/{id}/favorites](https://ng5m0uh5s7.execute-api.eu-north-1.amazonaws.com/dev/companies/{id}/favorites)

Replace `{id}` with the desired company ID. In the request body, provide the favorite data in JSON format.

#### Request Example

```bash
POST https://ng5m0uh5s7.execute-api.eu-north-1.amazonaws.com/dev/companies/1/favorites

{
"favourite_org_id": "9"
}
´´´

## [Postman Collection](link_to_postman_collection)
The Postman collection provides examples of requests to interact with the API. You can import it into Postman to easily test the different functionalities.

## DynamoDB Tables
The project uses two DynamoDB tables:

1. **CompaniesTable**: Stores information about companies.
   - **Attributes**: companyId (HASH), companyName
   - **Global Secondary Indexes**: CompanyNameIndex (HASH)

2. **FavoritesTable**: Stores information about company favorites.
   - **Attributes**: org_id (HASH), favourite_org_id (RANGE), date
   - **Global Secondary Indexes**: dateIndex (HASH)

## Project Configuration

### Service Details
- **Service Name**: apiAws
- **Serverless Framework Version**: 3
- **Provider**: AWS
- **Region**: eu-north-1

### Functions
#### Create Favorite
- **Handler**: favorites/add_favorite.add_favorite
- **HTTP Route**: POST /companies/{id}/favorites
- **IAM Permissions**: Access to dynamodb:PutItem on the favorites table

#### Get All Favorites
- **Handler**: favorites/get_favorites.get_favorites
- **HTTP Route**: GET /companies/{id}/favorites
- **IAM Permissions**: Access to dynamodb:Scan on the favorites table

## Author
This project was developed by Miriam Gallardo González-Amor.

Thank you for using the AWS API! If you have any questions or issues, feel free to contact us.
