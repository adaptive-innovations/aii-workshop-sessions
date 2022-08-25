# DAT A - Introduction to Databases
## Session 11


|Session Time|Facilitator|Starting URL              |
|------------|-----------|-------------------------------------------------------|
|1 Hour      |GR         |[Create View](https://www.w3schools.com/sql/sql_view.asp)     |



## Code Highlights
Show all tables in database ```Northwind```
```sql
USE Northwind;
SELECT * FROM sys.tables;
```

Show all tables in database ```labs```
```sql
USE labs;
SELECT * FROM sys.tables;
```

Create a new view in ```labs``` database which reads from data in the ```Northwind``` database
```sql
USE labs;
CREATE VIEW MyNewWiew AS
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
    ,CONCAT(Occupation, ' at ', Company) AS [Job Description]
    ,CONCAT_WS(', ', Address, City, State, Zip) AS [Mailing Address]
    ,'Favorite Color is ' + LOWER(FavoriteColor) + '.' AS [Favorite Color]
    ,UPPER(CC_Type) AS [Credit Card Type]
    ,REPLACE(CC_Num, ' ', '') AS [Credit Card Number]
    ,FORMAT(CC_EXP, 'MM/yy') AS [Credit Card Expiration]
    ,FORMAT(CC_CVV2, '000') AS [Credit Card CVV]
    ,FORMAT(Phone, '(000) 000-0000') AS Phone
    ,TRIM(Bio) as Bio
    ,LEN(TRIM(Bio)) AS [Bio  Character Length]
    ,LEFT(Vehicle, 4) AS [Vehicle YYYY]
    ,SUBSTRING(Vehicle, 3, 2) AS [Vehicle YY]
    ,RIGHT(Other, LEN(Other)-CHARINDEX('?', Other)) As [Zodiac Sign] --> New Column
FROM [workshop].[dbo].[Contacts];
```

List all views in the ```labs``` database
```sql
USE labs;
SELECT * FROM sys.views;
```


## Notes




## Challenge