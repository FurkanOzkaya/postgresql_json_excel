# Design Document



# Api List

- get-data
- post-data
- delete-data
- update-data
- post-column

# API's Details

## 1. get-data/
This end point return all information (columns + datas)

Request Type: GET  
Return Codes: 200, 204  
Response Type: JSON
```json 
GET  /api/get-data/ 
```
### return output example:

```json
{  
"column":  
	[  
		{  
			"id":  1,  
			"name":  "Name"  
		},  
		{  
			"id":  2,  
			"name":  "Surname"  
		},  
		{  
			"id":  3,  
			"name":  "Phone Number"  
		}  
	],  
"data":  
	[  
		{  
			"id":  1,  
			"content":  
			{  
				"Name":  "Furkan",  
				"Surname":  "Ozkaya",  
				"Phone Number":  "+90123456"  
			} 
		} 
	]  
}
```
## 2. post-data/

This end point add json data to database.

Request Type: POST  
Return Codes: 201, 400  
Parameters: content (json)
Response Type: JSON

### Expected input 
```json
{
	"content":  
			{  
			"Name":  "Furkan2",  
			"Surname":  "Ozkaya2",  
			"Phone Number":  "+901234567"  
			} 
}
```
### return output example:
```json
{  
	"id":  2,  
	"content":  
		{  
		"Name":  "Furkan2",  
		"Surname":  "Ozkaya2",  
		"Phone Number":  "+901234567"  
		} 
}
```

## 3. delete-data/<pk>
This end point delete excel row on database.

Request Type: Delete
Return Codes: 202, 204  
Parameters: Id of data
Response Type: JSON


## 4. update-data/<pk>
This end point update a row.

Request Type: PUT
Return Codes: 200, 204, 400  
Parameters: Id of data
Response Type: JSON

### Expected input 
```
api/update-data/<pk>
```
```json
{
	"content": 
	{

		"Name": "Furkan3",

		"Surname": "Ozkaya2",

		"Phone Number": "+901234567"
	}
}
```

### return output example:
```json
{
	"id": 2,

	"content": 
	{

		"Name": "Furkan3",

		"Surname": "Ozkaya2",

		"Phone Number": "+901234567"
	}
}
```

## 5. post-column/

This end point add json data to database.

Request Type: POST  
Return Codes: 201, 400  
Parameters: name
Response Type: JSON

### Expected input 
```json
{
	"name": "Column_Name"
}
```

### return output example:
```json
{
	"id": 5,
	"name": "Column_Name"
}
```
