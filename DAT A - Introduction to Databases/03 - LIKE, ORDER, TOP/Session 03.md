# DAT A - Introduction to Databases
## Session 01


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Order By](https://www.w3schools.com/sql/sql_orderby.asp)     |

## Code Highlights
Is Equal To Text
```sql
SELECT * FROM Customers
WHERE ContactTitle = 'Owner';
```

Contains Text
```sql
SELECT * FROM Customers
WHERE ContactTitle LIKE '%Sales%';
```

Begins With Text
```sql
SELECT * FROM Customers
WHERE CompanyName LIKE 'A%';
```

Ends With Text
```sql
SELECT * FROM Customers
WHERE CompanyName LIKE '%r';
```

For More wildcard options, check out https://www.w3schools.com/sql/sql_wildcards.asp

Does NOT Contain Text
```sql
SELECT * FROM Customers
WHERE ContactTitle NOT LIKE '%Sales%';
```

ORDER BY clause
```sql
SELECT * FROM Orders
ORDER BY Freight ASC;
```

ORDER BY clause (Descending)
```sql
SELECT * FROM Orders
ORDER BY Freight DESC;
```

TOP to limit results
```sql
SELECT TOP 5 * FROM Orders
ORDER BY Freight DESC;
```

Use TOP to identify most expensive product
```sql
SELECT TOP 1 * FROM Products
ORDER BY UnitPrice DESC;
```


## Challenge
