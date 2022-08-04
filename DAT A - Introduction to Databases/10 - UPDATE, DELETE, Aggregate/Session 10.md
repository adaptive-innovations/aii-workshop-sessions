# DAT A - Introduction to Databases
## Session 09


|Session Time|Facilitator|Starting URL              |
|------------|-----------|-------------------------------------------------------|
|1 Hour      |GR         |[Data Types](https://www.w3schools.com/sql/sql_datatypes.asp#midcontentadcontainer)     |



## Code Highlights
SELECT Current State of the insertTest Table
```sql
USE labs;
SELECT * FROM insertTest;
```
<br>

Update a record 

_(It is wise to test affected rows by crafting the SELECT statement first)_
```sql
UPDATE insertTest
SET stringColumn = 'Hey, this is new!'
WHERE entryID = 1;

SELECT * FROM insertTest WHERE entryID = 1;
```
<br>

Update using an operator
```sql
UPDATE insertTest
SET intColumn = intColumn + 2
WHERE entryID = 1;

SELECT * FROM insertTest WHERE entryID = 1;
```
<br>

Update multiple columns of a record
```sql
UPDATE insertTest
SET stringColumn = 'Hey, this is new!'
    ,intColumn = intColumn + 2
WHERE entryID = 1;

SELECT * FROM insertTest WHERE entryID = 1;
```
<br>

Update multiple columns of multiple records
```sql
UPDATE insertTest
SET stringColumn = 'Hey, these are new!'
    ,intColumn = intColumn + 2
WHERE entryID < 10;

SELECT * FROM insertTest WHERE entryID < 10;
```
<br>


Delete a record
```sql
DELETE FROM insertTest
WHERE entryID = 10;

SELECT * FROM insertTest WHERE entryID < 10;
```
<br>


GROUP BY
```sql
SELECT
    ShipCountry
FROM Orders
GROUP BY ShipCountry;
```


Aggregate Functions
```sql
SELECT
    ShipCountry
    ,SUM(Freight) as FreightSum
    ,AVG(Freight) as FreightAvg
    ,COUNT(*) as FreightCountRows
    ,MAX(Freight) as FreightMax
    ,MIN(Freight) as FreightMin
FROM Orders
GROUP BY ShipCountry;
```

Aggregate Functions: Which country do we ship to the most?
```sql
SELECT TOP(1)
    ShipCountry
    ,SUM(Freight) as FreightSum
    ,AVG(Freight) as FreightAvg
    ,COUNT(*) as FreightCountRows
    ,MAX(Freight) as FreightMax
    ,MIN(Freight) as FreightMin
FROM Orders
GROUP BY ShipCountry
ORDER BY COUNT(*) DESC;
```

Aggregate Functions with JOIN
```sql
SELECT 
    CustomerID
    ,Employees.FirstName
    ,SUM(Freight) as FreightSum
    ,AVG(Freight) as FreightAvg
    ,COUNT(*) as CountRows
    ,MAX(ShipName) as Max
    ,MIN(ShipName) as Min
FROM Orders
JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY CustomerID, Employees.FirstName
ORDER BY COUNT(*) DESC;
```

## Notes




## Challenge