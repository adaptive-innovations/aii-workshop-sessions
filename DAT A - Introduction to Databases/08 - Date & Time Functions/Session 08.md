# DAT A - Introduction to Databases
## Session 08


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Date/Time Functions](https://www.w3schools.com/sql/sql_ref_sqlserver.asp)     |


Working with Date/Time

## Code Highlights
Starting query on the ```Contacts``` table in the ```workshop``` database.
```sql
USE workshop;
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
FROM Contacts;
```

Get Year using the ```YEAR()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,YEAR(DOB) as BirthYear
FROM Contacts;
```

Get Month using the ```MONTH()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,MONTH(DOB) as BirthMonth
FROM Contacts;
```

Get Day using the ```DAY()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,DAY(DOB) as BirthDay
FROM Contacts;
```

Get Current Time using ```CURRENT_TIMESTAMP``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,CURRENT_TIMESTAMP as RightNow
FROM Contacts;
```

Get Current UTC Time using the ```GETUTCDATE()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,GETUTCDATE() as RightNowUTC
FROM Contacts;
```

Return the difference between two dates using the ```DATEDIFF()``` function.
https://www.w3schools.com/sql/func_sqlserver_datediff.asp
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,DATEDIFF(year, DOB, CURRENT_TIMESTAMP) as Age
FROM Contacts;
```

Add a time/date interval to a date using the ```DATEADD()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,DATEADD(year, 21, DOB) AS Turned21
      ,DATEADD(month, -1, CURRENT_TIMESTAMP) AS OneMonthAgo
      ,DATEADD(hour, -3, CURRENT_TIMESTAMP) AS ThreeHoursAgo
FROM Contacts;
```

Return a date from the specified parts (year, month, and day values) using ```DATEFROMPARTS()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,DATEFROMPARTS(YEAR(CURRENT_TIMESTAMP), MONTH(DOB), DAY(DOB)) AS BirthdayThisYear
FROM Contacts;
```

Return a specified part of a date (as string) using ```DATENAME()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,DATENAME(month, CURRENT_TIMESTAMP) AS CurrentMonthName
      ,DATENAME(weekday, CURRENT_TIMESTAMP) AS CurrentWeekdayName
      ,DATENAME(weekday, DOB) AS DOBWeekday
FROM Contacts;
```

Return a specified part of a date (as integer) using ```DATEPART()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,DATEPART(MINUTE, CURRENT_TIMESTAMP) AS CurrentMinute
      ,DATEPART(WEEKDAY, CURRENT_TIMESTAMP) AS CurrentWeekDay
      ,DATEPART(tz, CURRENT_TIMESTAMP AT TIME ZONE 'Pacific Standard Time') AS TzOffsetMinsPST
      ,DATEPART(tz, CURRENT_TIMESTAMP AT TIME ZONE 'Fiji Standard Time') AS TzOffsetMinsFST
FROM Contacts;
```

Check an expression and returns 1 if it is a valid date, otherwise 0 using ```ISDATE()``` function.
```sql
SELECT ID
      ,CONCAT_WS(' ', Prefix, FirstName, LastName) AS Name
      ,DOB AS DateOfBirth
      ,ISDATE(FirstName) AS IsNameADate
      ,ISDATE('2020/01/01') AS IsStrADate
FROM Contacts;
```

Run this to show time zone info on the server
```sql
SELECT * FROM sys.time_zone_info;
```

## Challenge
Pick one of these challenges:
- Use one of the new functions we learned today to generate current UNIX timestamp.
- Use one of the new functions we learned today to find out what weekday you were born.
- Use one of the new functions we learned today to use someone's date of birth to identify if we've missed their birthday already this year (if number is negative vs positive), count in weeks.