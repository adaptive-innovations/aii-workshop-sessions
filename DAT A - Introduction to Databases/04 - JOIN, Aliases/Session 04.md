# DAT A - Introduction to Databases
## Session 04


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Joins](https://www.w3schools.com/sql/sql_join.asp)     |

We use joins to get information from related tables.

<a href="https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help/one-to-many-relationships.html">
  <img src="https://github.com/adaptive-innovations/aii-workshop-sessions/blob/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN,%20Aliases/TableRelationship.png?raw=true" alt="Credit: Filemaker" width=75%/>
</a>

## Code Highlights
SELECT Statements Example
```sql
SELECT
    ProductID
    ,ProductName
    ,CategoryID
FROM Products;

SELECT
    CategoryID
    ,CategoryName
    ,Description
FROM Categories;
```
Note the relationship: ```CategoryID```

The JOIN Statement
```sql
SELECT
    Products.ProductID
    ,Products.ProductName
    ,Products.CategoryID
    ,Categories.CategoryName
    ,Categories.Description
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID;
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

## Challenge
