# DAT A - Introduction to Databases
## Session 04


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Order By](https://www.w3schools.com/sql/sql_orderby.asp)     |

## Code Highlights
SELECT Statements We've Done So Far
```sql
SELECT ProductID, ProductName, CategoryID FROM Products;
SELECT ProductName FROM Categories;
```
Note the relationship: ```CategoryID```



### Relationship types
#### One to One
In a **One to One** relationship, each record in Table 1 has a unique identifier, and each record in Table 2 has a unique identifier.

<a href="https://docs.oracle.com/html/E79061_01/Content/Data%20model/Define_a_relationship.htm">
  <img src="https://raw.githubusercontent.com/adaptive-innovations/aii-workshop-sessions/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN%2C%20Aliases/Relationships%20-%201%20to%201.png" alt="Credit: Oracle" width=75%/>
</a>

#### One to Many
In a **One to Many** relationship, each record in Table 1 has a unique identifier, but each record in Table 2 has a multiple instances of that unique identifier.

<a href="https://docs.oracle.com/html/E79061_01/Content/Data%20model/Define_a_relationship.htm">
  <img src="https://raw.githubusercontent.com/adaptive-innovations/aii-workshop-sessions/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN%2C%20Aliases/Relationships%20-%201%20to%20Many.png" alt="Credit: Oracle" width=75%/>
</a>


## Challenge
