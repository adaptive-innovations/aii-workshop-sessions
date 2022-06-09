# DAT A - Introduction to Databases
## Session 04


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Joins](https://www.w3schools.com/sql/sql_join.asp)     |

We use joins to merge information from related tables.

<a href="https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help/one-to-many-relationships.html">
  <img src="https://github.com/adaptive-innovations/aii-workshop-sessions/blob/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN,%20Aliases/TableRelationship.png?raw=true" alt="Credit: Filemaker" width=75%/>
</a>

## Code Highlights
SELECT Statements Example
```sql
SELECT
    OrderID
    ,CustomerID
FROM Orders;

SELECT
    CustomerID
    ,CompanyName
FROM Customers;

```
Note the relationship: ```CustomerID```

The JOIN Statement
```sql
SELECT
    Orders.OrderID
    ,Orders.CustomerID
    ,Customers.CompanyName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

Another JOIN Example
```sql
SELECT
    Products.ProductID
    ,Products.ProductName
    ,Categories.CategoryName
    ,Categories.Description
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID;
```

With a WHERE Clause
```sql
SELECT
    Products.ProductID
    ,Products.ProductName
    ,Categories.CategoryName
    ,Categories.Description
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
WHERE Categories.Description LIKE '%SWEET%';
```

With an ORDER BY Clause
```sql
SELECT
    Products.ProductID
    ,Products.ProductName
    ,Categories.CategoryName
    ,Categories.Description
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
WHERE Categories.Description LIKE '%SWEET%'
ORDER BY Categories.CategoryName ASC, Products.ProductName ASC;
```

With a COMMENT
```sql
SELECT
    Products.ProductID
    ,Products.ProductName
    ,Categories.CategoryName
    ,Categories.Description
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
WHERE Categories.Description LIKE '%SWEET%' -- Per Ted, the boss man.
ORDER BY Categories.CategoryName ASC, Products.ProductName ASC;
```

With a TOP Clause
```sql
SELECT TOP(20)
    Products.ProductID
    ,Products.ProductName
    ,Categories.CategoryName
    ,Categories.Description
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
WHERE Categories.Description LIKE '%SWEET%' -- Per Ted, the boss man.
ORDER BY Categories.CategoryName ASC, Products.ProductName ASC;
```

Aliases: Table Name Example
```sql
SELECT
    P.ProductID
    ,P.ProductName
    ,C.CategoryName
    ,C.Description
FROM Products AS P
JOIN Categories AS C ON P.CategoryID = C.CategoryID;
```

Aliases: Column Name Example
```sql
SELECT
    P.ProductID
    ,P.ProductName AS Name
    ,P.CategoryID
    ,C.CategoryName AS Category
    ,C.Description AS [Category Description]
FROM Products AS P
JOIN Categories AS C ON P.CategoryID = C.CategoryID;
```

### Relationship types
#### One to One
In a **One to One** relationship, each record in Table 1 has a unique identifier, and each record in Table 2 has a unique identifier.

<a href="https://docs.oracle.com/html/E79061_01/Content/Data%20model/Define_a_relationship.htm">
  <img src="https://raw.githubusercontent.com/adaptive-innovations/aii-workshop-sessions/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN%2C%20Aliases/Relationships%20-%201%20to%201.png?raw=true" alt="Credit: Oracle" width=75%/>
</a>

#### One to Many
In a **One to Many** relationship, each record in Table 1 has a unique identifier, but each record in Table 2 has multiple instances of unique identifiers.
_Note that each pet has only one owner._

<a href="https://docs.oracle.com/html/E79061_01/Content/Data%20model/Define_a_relationship.htm">
  <img src="https://raw.githubusercontent.com/adaptive-innovations/aii-workshop-sessions/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN%2C%20Aliases/Relationships%20-%201%20to%20Many.png?raw=true" alt="Credit: Oracle" width=75%/>
</a>

#### Many to Many
In a **Many to Many** relationship, each record in Table 1 has multiple instances of unique identifiers, and each record in Table 2 has multiple instances of unique identifiers.
_Note that a pet can have multiple owners._

<a href="https://docs.oracle.com/html/E79061_01/Content/Data%20model/Define_a_relationship.htm">
  <img src="https://github.com/adaptive-innovations/aii-workshop-sessions/blob/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN,%20Aliases/Relationships%20-%20Many%20to%20Many.png?raw=true" alt="Credit: Oracle" width=75%/>
</a>

#### Many to One
In a **Many to One** relationship, each record in Table 1 has multiple instances of unique identifiers, but each record in Table 2 has a unique identifier.

<a href="https://docs.oracle.com/html/E79061_01/Content/Data%20model/Define_a_relationship.htm">
  <img src="https://github.com/adaptive-innovations/aii-workshop-sessions/blob/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN,%20Aliases/Relationships%20-%20Many%20to%20One.png?raw=true" alt="Credit: Oracle" width=75%/>
</a>


Here's our reference drawing we made in class to demonstrate JOIN results:
[Join Illustration](https://github.com/adaptive-innovations/aii-workshop-sessions/blob/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN,%20Aliases/JoinDemonstration.PNG?raw=true)

## Challenge
- Choose a table to JOIN with ```Orders```, and write a query that includes at least 3 columns from each table.
- Demonstrate using a WHERE Clause with your query.
- Demonstrate using an ORDER BY Clause with your query.
- Demonstrate using Aliases with your query's Table names.
- Demonstrate using Aliases with some of your query's Column names.
- BONUS: Use Multiple Joins to Join 3 or more different related tables.