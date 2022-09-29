# DAT A - Introduction to Databases
## Session 12


|Session Time|Facilitator|Starting URL              |
|------------|-----------|-------------------------------------------------------|
|1 Hour      |GR         |[WITH Statement](https://modern-sql.com/feature/with)     |



## Code Highlights
Here's a query which summarizes all sales made per EmployeeID
```sql
SELECT 
    EmployeeID
    ,COUNT(*) as NumberOfSales
FROM Orders
GROUP BY EmployeeID;
```

Here's a 2nd query which lists the Employee's names and Titles
```sql
SELECT
    Employees.EmployeeID
    ,CONCAT(FirstName, ' ', LastName) AS EmployeeName
    ,Title AS EmployeeTitle
    ,TempTable.NumberOfSales
FROM Employees
JOIN TempTable ON Employees.EmployeeID = TempTable.EmployeeID;
```

USE Northwind;

-- VERSION A
WITH TempTable AS (
    SELECT 
        EmployeeID
        ,COUNT(*) as NumberOfSales
    FROM Orders
    GROUP BY EmployeeID
)

SELECT
    Employees.EmployeeID
    ,CONCAT(FirstName, ' ', LastName) AS EmployeeName
    ,Title AS EmployeeTitle
    ,TempTable.NumberOfSales
FROM Employees
JOIN TempTable ON Employees.EmployeeID = TempTable.EmployeeID;

-- VERSION B
WITH EESum AS (
    SELECT 
        EmployeeID
        ,COUNT(*) as NumberOfSales
    FROM Orders
    GROUP BY EmployeeID
),
EEInfo AS (
    SELECT
        EmployeeID
        ,CONCAT(FirstName, ' ', LastName) AS EmployeeName
        ,Title AS EmployeeTitle
    FROM Employees
)

SELECT
    EEInfo.EmployeeID
    ,EmployeeName
    ,EmployeeTitle
    ,NumberOfSales
FROM EESum
JOIN EEInfo ON EESum.EmployeeID = EEInfo.EmployeeID

-- VERSION C
WITH EESum AS (
    SELECT 
        EmployeeID
        ,COUNT(*) as NumberOfSales
    FROM Orders
    GROUP BY EmployeeID
),
EEInfo AS (
    SELECT
        EmployeeID
        ,CONCAT(FirstName, ' ', LastName) AS EmployeeName
        ,Title AS EmployeeTitle
    FROM Employees
),
EmployeeSales AS (
    SELECT
        EEInfo.EmployeeID
        ,EmployeeName
        ,EmployeeTitle
        ,NumberOfSales
    FROM EESum
    JOIN EEInfo ON EESum.EmployeeID = EEInfo.EmployeeID
)

SELECT * FROM EmployeeSales


## Notes




## Challenge
- In ```Order Details ```Use ([UnitPrice] * [Quantity]) and the [Discount] to get line item totals
- Use the above to summarize Order Details by Total Cost per OrderID
- Join the above with ```Orders``` to get the CustomerID
- Join the above with ```Customers``` to get the CompenyName

The query result should give us the total amount spent per Company Name
Columns:
- CustomerID
- CompanyName
- Total Spent