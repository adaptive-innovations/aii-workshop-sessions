# DAT A - Introduction to Databases
## Session 13


|Session Time|Facilitator|Starting URL              |
|------------|-----------|-------------------------------------------------------|
|1 Hour      |GR         |[Working with JSON](https://www.w3schools.com/whatis/whatis_json.asp)  |



## Code Highlights
See the table with JSON objects
```sql
USE workshop;

SELECT *
  FROM employees;
```

Selecting values from JSON objects in a table
```sql
SELECT 
  JSON_VALUE([object], '$.id') AS [employee_id]
  ,JSON_VALUE([object], '$.first_name') AS [first_name]
  ,JSON_VALUE([object], '$.last_name') AS [last_name]
  ,JSON_VALUE([object], '$.email') AS [email]
  ,JSON_VALUE([object], '$.favoritedinosaur') AS [favoritedinosaur] -- NULL because it doesn't exist
FROM employees;
```

Using a JSON value in the WHERE clause
```sql
SELECT
  [object]
FROM [workshop].[dbo].[employees]
WHERE JSON_VALUE([object], '$.id') = 1;
```

Selecting the keys and values from a single JSON object 
```sql
SELECT
  [key]
  ,[value]
FROM OPENJSON(
    (
      SELECT
        [object]
      FROM [workshop].[dbo].[employees]
      WHERE JSON_VALUE([object], '$.id') = 1
    ), '$');
```

Returning a table as JSON. Returns an ```array``` of ```objects```. 
```sql
SELECT
  [entry_id]
  ,[created]
  ,[unit]
  ,[length]
  ,[description]
FROM lumber
FOR JSON AUTO;
```

Returning a table as JSON with nested path control
```sql
SELECT
  [entry_id]
  ,[created]
  ,[unit] AS [dimensions.unit]
  ,[length] AS [dimensions.length]
  ,[description]
FROM lumber
FOR JSON PATH;
```

Returning JSON as object only, without it being in an array
```sql
SELECT
  [entry_id]
  ,[created]
  ,[unit] AS [dimensions.unit]
  ,[length] AS [dimensions.length]
  ,[description]
FROM lumber
WHERE [entry_id] = 1
FOR JSON PATH, WITHOUT_ARRAY_WRAPPER;
```

Returning JSON with both detail and summarized data using nested subquery.
```sql
SELECT
  L.[entry_id]
  ,L.[created]
  ,L.[unit] AS [dimensions.unit]
  ,L.[length] AS [dimensions.length]
  ,(SELECT
      MAX(X.[length]) AS [max_global]
    FROM lumber as X
    WHERE L.[unit] = X.[unit]
    FOR JSON PATH ) AS [summary]
  ,L.[description]
FROM lumber AS L
FOR JSON PATH;
```



## Notes




## Challenge