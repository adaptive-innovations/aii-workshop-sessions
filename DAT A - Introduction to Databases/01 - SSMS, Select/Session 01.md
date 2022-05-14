# DAT A - Introduction to Databases
## Session 01

|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[SQL Basic Syntax](https://www.w3schools.com/sql/sql_syntax.asp)     |

## Code Highlights
Basic SELECT Statement
```sql
SELECT * FROM Products;
```

SELECT from a different Table
```sql
SELECT * FROM Customers;
```
> What happens if we execute multiple queries?

SELECT Specific Columns
```sql
SELECT ContactName, City FROM Customers;
```

SELECT DISTINCT Columns
```sql
SELECT DISTINCT City FROM Customers;
```

SELECT COUNT of DISTINCT Columns
```sql
SELECT DISTINCT City, COUNT(*) FROM Customers;
```




## Challenge
Create a query that...