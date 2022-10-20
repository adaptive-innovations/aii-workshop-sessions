# DAT A - Introduction to Databases
## Session 15


|Session Time|Facilitator|Starting URL              |
|------------|-----------|-------------------------------------------------------|
|1 Hour      |GR         |[Stored Procedures](https://www.w3schools.com/sql/sql_stored_procedures.asp)  |



## Code Highlights
First, switch the the ```labs``` database:
```sql
USE labs;
```

Using Variables in SQL
```sql
DECLARE @name nvarchar(10);
SET @name = 'Arnold'
SELECT(@name);
```

Using the PRINT statement
```sql
DECLARE @name nvarchar(10);
SET @name = 'Arnold'
PRINT(@name);
```

Messages vs Results
```sql
DECLARE @name nvarchar(10);
SET @name = 'Arnold'
PRINT('Here is a message for you:')
PRINT(@name)
SELECT(@name);
```

Create a custom function in SQL.
```sql
CREATE FUNCTION dbo.multiplyIntegers(@numberOne int, @numberTwo int)
RETURNS int
AS
  BEGIN
    DECLARE @product int;
    SET @product = @numberOne * @numberTwo
    RETURN(@product);
  END
GO
```

Use your new function
```sql
SELECT dbo.multiplyIntegers(3, 2);
```

Show Custom Functions
```sql
SELECT * FROM sys.objects WHERE type_desc LIKE '%FUNCTION%';
```


Create a custom function in SQL. Example B
```sql
CREATE FUNCTION dbo.getLocalDatetime()
RETURNS DATETIME
AS
  BEGIN
    DECLARE @return_value DATETIME;
    SET @return_value = DATEADD(mi, DATEPART(tz, CURRENT_TIMESTAMP AT TIME ZONE 'Pacific Standard Time'), CURRENT_TIMESTAMP)
    RETURN(@return_value);
  END
GO
```


Alter a custom function in SQL. Example B
```sql
ALTER FUNCTION dbo.getLocalDatetime()
RETURNS DATETIME
AS
  BEGIN
    DECLARE @return_value DATETIME;
    SET @return_value = DATEADD(mi, DATEPART(tz, CURRENT_TIMESTAMP AT TIME ZONE 'Pacific Standard Time'), CURRENT_TIMESTAMP)
    RETURN(@return_value);
  END
GO
```

Drop a custom function in SQL.
```sql
DROP FUNCTION dbo.getLocalDatetime()
```

Create a stored procedure in SQL.
```sql
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
  SELECT * FROM Northwind.dbo.Customers WHERE City = @City AND PostalCode = @PostalCode
GO
```

Execute a stored procedure in SQL.
```sql
EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';
```

Show stored procedures
```sql
SELECT * FROM sys.objects WHERE type_desc LIKE '%PROCEDURE%';
```

THE BIG EXAMPLE OF A TABLE AND VIEW RESET
```sql
-- CREATE PROCEDURE
CREATE OR ALTER PROCEDURE ResetParentsTableGR
AS
    -- DECLARE VARIABLES
    DECLARE @RowID INT;
    SET @RowID = 0;
    
    -- DROP AND RECREATE TABLE (Dropping the table serves to clear all of the data as well)
    DROP TABLE Parents;
    CREATE TABLE Parents 
    (
        [id] INT
        ,[name] NVARCHAR(MAX)
    );

    -- INSERT THE ROWS
    SET @RowID = @RowID + 1;
    INSERT INTO Parents ([id], [name]) VALUES (@RowID, 'Elrond');
    SET @RowID = @RowID + 1;
    INSERT INTO Parents ([id], [name]) VALUES (@RowID, 'Christopher Pevensie');
    SET @RowID = @RowID + 1;
    INSERT INTO Parents ([id], [name]) VALUES (@RowID, 'John Wick');
    GO

    -- MAKE THE VIEW IF NOT EXISTS
    CREATE OR ALTER VIEW v_parents AS
    SELECT
        [id]
        ,[name]
        ,dbo.getLocalDatetimeEF() AS ThisTime
    FROM Parents
GO

-- USE THE PROCEDURE!
EXEC ResetParentsTableGR;
-- VERIFY THE VIEW WORKS!
SELECT * FROM v_parents GO
```


## Discussion
Functions vs Stored Procedures
|Functions|Stored Procedures|
|---------|-----------------|
|Use to simplify redundancy in queries|Use to automate procedures on your database|
|Must Return a Value|Return Value is optional|
|Input parameters only| Can use output parameters as well|
|Can be called from a procedure|Cannot be called from a function|
|Supports ```SELECT```|Supports ```SELECT```/```INSERT```/```UPDATE```/```DELETE```|
|Can be used in ```WHERE```/```HAVING```/```SELECT```|Can **NOT** be used in ```WHERE```/```HAVING```/```SELECT```|
|Can return tables which can then be ```JOIN```ed|Cannot return rowsets|
|Cannot handle exceptions|Can handle exceptions using a try-catch block|

## Challenge