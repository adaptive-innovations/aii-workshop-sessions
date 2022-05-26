# DAT A - Introduction to Databases
## Session 02


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[The WHERE Clause](https://www.w3schools.com/sql/sql_where.asp)     |

## Code Highlights
Is Equal To Text
```sql
SELECT * FROM Customers
WHERE Country = 'USA';
```

Is Equal To Date
```sql
SELECT * FROM Orders
WHERE OrderDate = '1998-05-01';
```

Is Equal To Number
```sql
SELECT * FROM Products
WHERE UnitsInStock = 101;
```

Is Greater Than
```sql
SELECT * FROM Products
WHERE UnitsInStock > 101;
```

Is Greater Than or Equal To
```sql
SELECT * FROM Products
WHERE UnitsInStock >= 101;
```

Is Not Equal To
```sql
SELECT * FROM Products
WHERE UnitsInStock != 101;
```

Is Greater Than Date
```sql
SELECT * FROM Orders
WHERE OrderDate > '1998-05-01';
```

AND
```sql
SELECT * FROM Orders
WHERE CustomerID = 'TOMSP'
AND Freight > 10;
```

OR
```sql
SELECT * FROM Products
WHERE UnitsInStock = 0
OR UnitsInStock < ReorderLevel;
```

AND/OR
```sql
SELECT * FROM Products
WHERE 
Discontinued = 0 AND
(UnitsInStock = 0 OR UnitsInStock < ReorderLevel);
```

## Challenge
- How many ```Products``` have a unit price > 25?
- How many ```Products``` have a > 100 in stock?
- How many ```Products``` have been discontinued?
- How many ```Customers``` are in Seattle?
- How many ```Customers``` are in France?
- Find an employee in ```Employees``` who can assist our customers in Seattle?
- Are all of our ```Employees``` either ```Mr.```, ```Mrs.```, or ```Ms.```?
- How many ```Regions``` are there?
