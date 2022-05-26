# DAT A - Introduction to Databases
## Session 01


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
