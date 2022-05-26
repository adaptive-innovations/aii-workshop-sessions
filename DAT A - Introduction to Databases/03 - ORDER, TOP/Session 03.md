# DAT A - Introduction to Databases
## Session 01


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[The WHERE Clause](https://www.w3schools.com/sql/sql_where.asp)     |

## Code Highlights
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
