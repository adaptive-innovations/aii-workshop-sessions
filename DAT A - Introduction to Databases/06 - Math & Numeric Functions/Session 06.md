# DAT A - Introduction to Databases
## Session 06


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Math & Numeric Functions](https://www.w3schools.com/sql/sql_ref_sqlserver.asp#midcontentadcontainer)     |


## Code Highlights
New column using Addition
```sql
USE [workshop];
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,1 + 2 as MyNewColumn
  FROM Tanks;
```

New column using Subtraction
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,100 - 10 as MyNewColumn
  FROM Tanks;
```

New column using Division
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,500/10 as MyNewColumn
  FROM Tanks;
```

New column using Multiplication
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,3*4 as MyNewColumn
  FROM Tanks;
```

Count Rows
```sql
SELECT COUNT(*) as CountRows FROM Tanks;
```
Get Maximum Value
```sql
SELECT MAX(tank_length_ft) FROM Tanks;
```

Get Minimum Value
```sql
SELECT MIN(tank_length_ft) FROM Tanks;
```

Get Average Value
```sql
SELECT AVG(tank_diameter_ft) FROM Tanks;
```

Get the value of Pi!
```sql
SELECT PI();
```

Let's calculate the amount of water our tanks can hold.
- Start with our basic query
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
  FROM [workshop].[dbo].[Tanks];
```
- Find the radius of the tank by dividing the diameter by 2
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,[tank_diameter_ft]/2 as tank_radius_ft
  FROM [workshop].[dbo].[Tanks];
```
- What is the radius<sup>2</sup>? Use the ```SQUARE()``` Function.
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,[tank_diameter_ft]/2 as tank_radius_ft
      ,SQUARE([tank_diameter_ft]/2) as tank_radius_sq_ft
  FROM [workshop].[dbo].[Tanks];
```
- Calculate the Area using radius<sup>2</sup> x Pi using the ```PI()``` Function
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,[tank_diameter_ft]/2 as tank_radius_ft
      ,SQUARE([tank_diameter_ft]/2) as tank_radius_sq_ft
      ,SQUARE([tank_diameter_ft]/2)*PI() as tank_area_sq_ft
  FROM [workshop].[dbo].[Tanks];
```

- Calculate the Tank Volume (area x length)
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,[tank_diameter_ft]/2 as tank_radius_ft
      ,SQUARE([tank_diameter_ft]/2) as tank_radius_sq_ft
      ,SQUARE([tank_diameter_ft]/2)*PI() as tank_area_sq_ft
      ,SQUARE([tank_diameter_ft]/2)*PI()*tank_length_ft as tank_volume_ft
  FROM [workshop].[dbo].[Tanks];
```

- Calculate the gallons of capacity using a [tank volume to gallons conversion value](https://www.asknumbers.com/cubic-feet-to-gallons.aspx).
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,[tank_diameter_ft]/2 as tank_radius_ft
      ,SQUARE([tank_diameter_ft]/2) as tank_radius_sq_ft
      ,SQUARE([tank_diameter_ft]/2) * PI() as tank_area_sq_ft
      ,SQUARE([tank_diameter_ft]/2) * PI() * tank_length_ft as tank_volume_ft
      ,SQUARE([tank_diameter_ft]/2) * PI() * tank_length_ft * 7.4805194805195 as tank_capacity_gals
  FROM [workshop].[dbo].[Tanks];
```

- Let's round the result to 2 floating points using the ```ROUND()``` function.
> Basic Syntax: ```ROUND(number, decimals)```</br>Example: ```ROUND(152.25667, 2)```</br>Example Result: ```152.25```
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,SQUARE([tank_diameter_ft]/2) as tank_radius_sq_ft
      ,SQUARE([tank_diameter_ft]/2) * PI() as tank_area_sq_ft
      ,SQUARE([tank_diameter_ft]/2) * PI() * tank_length_ft as tank_volume_ft
      ,SQUARE([tank_diameter_ft]/2) * PI() * tank_length_ft * 7.4805194805195 as tank_capacity_gals
      ,ROUND(SQUARE([tank_diameter_ft]/2) * PI() * tank_length_ft * 7.4805194805195, 2) as tank_capacity_gals_rounded
  FROM [workshop].[dbo].[Tanks];
```

- Cleanup.
```sql
SELECT [design_id]
      ,[design_name]
      ,[designed_by]
      ,[tank_length_ft]
      ,[tank_diameter_ft]
      ,ROUND(SQUARE([tank_diameter_ft]/2) * PI() * tank_length_ft * 7.4805194805195, 2) as tank_capacity_gals
  FROM [workshop].[dbo].[Tanks];
```

## Notes
- I considered teaching the ```RAND()``` function, but it seemed needlessly confusing. For more information, read about it [here](https://www.w3schools.com/sql/func_sqlserver_rand.asp).
- ```ABS()``` can be used to get an absolute value.
> Basic Syntax: ```ABS(number)```</br>Example: ```ABS(100-300)```</br>Example Result: ```200```

## Challenge
- 
