# DAT A - Introduction to Databases
## Session 06


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[String Functions](https://www.w3schools.com/sql/sql_ref_sqlserver.asp)     |


## Code Highlights
Basic query on the ```Contacts``` table in the ```workshop``` database.
```sql
USE workshop;
SELECT * FROM Contacts;
```

Adds two or more strings together using the ```+``` operator.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_concat_with_plus.asp)
```sql
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
FROM Contacts;
```


Add two or more strings together using the ```CONCAT()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_concat.asp)
```sql
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
    ,CONCAT(Occupation, ' at ', Company) AS [Job Description] --> New Column
FROM Contacts;
```

Adds two or more strings together with a separator using the ```CONCAT_WS()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_concat_ws.asp)
```sql
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
    ,CONCAT(Occupation, ' at ', Company) AS [Job Description]
    ,CONCAT_WS(', ', Address, City, State, Zip) AS [Mailing Address] --> New Column
FROM Contacts;
```

Convert a string to lower-case using the ```LOWER()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_lower.asp)
```sql
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
    ,CONCAT(Occupation, ' at ', Company) AS [Job Description]
    ,CONCAT_WS(', ', Address, City, State, Zip) AS [Mailing Address]
    ,'Favorite Color is ' + LOWER(FavoriteColor) + '.' AS [Favorite Color] --> New Column
FROM Contacts;
```

Convert a string to upper-case using the ```UPPER()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_upper.asp)
```sql
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
    ,CONCAT(Occupation, ' at ', Company) AS [Job Description]
    ,CONCAT_WS(', ', Address, City, State, Zip) AS [Mailing Address]
    ,'Favorite Color is ' + LOWER(FavoriteColor) + '.' AS [Favorite Color]
    ,UPPER(CC_Type) AS [Credit Card Type] --> New Column
FROM Contacts;
```

Replaces all occurrences of a substring within a string using the ```REPLACE()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_replace.asp)
```sql
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
    ,CONCAT(Occupation, ' at ', Company) AS [Job Description]
    ,CONCAT_WS(', ', Address, City, State, Zip) AS [Mailing Address]
    ,'Favorite Color is ' + LOWER(FavoriteColor) + '.' AS [Favorite Color]
    ,UPPER(CC_Type) AS [Credit Card Type]
    ,REPLACE(CC_Num, ' ', '') AS [Credit Card Number] --> New Column
FROM Contacts;
```

Format a value with the specified format using the ```FORMAT()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_format.asp)
```sql
SELECT
    ID AS [Contact ID]
    ,LastName + ', ' + FirstName AS [Full Name]
    ,CONCAT(Occupation, ' at ', Company) AS [Job Description]
    ,CONCAT_WS(', ', Address, City, State, Zip) AS [Mailing Address]
    ,'Favorite Color is ' + LOWER(FavoriteColor) + '.' AS [Favorite Color]
    ,UPPER(CC_Type) AS [Credit Card Type]
    ,REPLACE(CC_Num, ' ', '') AS [Credit Card Number]
    ,FORMAT(CC_EXP, 'MM/yy') AS [Credit Card Expiration] --> New Column
    ,FORMAT(CC_CVV2, '000') AS [Credit Card CVV] --> New Column
    ,FORMAT(Phone, '(000) 000-0000') AS Phone --> New Column
FROM Contacts;
```

Removes leading and trailing spaces using the ```TRIM()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_trim.asp)
> Also, see LTRIM() (Left Trim) and RTRIM() (Right Trim) 
```sql
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
    ,TRIM(Bio) as Bio --> New Column
FROM Contacts;
```

Returns the length of the bio using the ```LEN()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_len.asp)
```sql
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
    ,LEN(TRIM(Bio)) AS [Bio  Character Length] --> New Column
FROM Contacts;
```

Extract a number of LEFT characters from a string using the ```LEFT()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_left.asp)
> The RIGHT() function extracts a number of RIGHT characters from a string.
```sql
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
    ,LEFT(Vehicle, 4) AS [Vehicle YYYY] --> New Column
FROM Contacts;
```

Extract a number of characters from the middle of a string using the ```SUBSTRING()``` function.
[See Usage Instructions](https://www.w3schools.com/sql/func_sqlserver_substring.asp)
```sql
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
    ,SUBSTRING(Vehicle, 3, 2) AS [Vehicle YY] --> New Column
FROM Contacts;
```

Get the Zodiac Sign from the RIGHT side of a messy string using a combination of functions.
```sql
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
FROM Contacts;
```

Export It!

## Notes

## Challenge
