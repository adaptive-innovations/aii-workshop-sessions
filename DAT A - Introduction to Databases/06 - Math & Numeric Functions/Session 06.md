# DAT A - Introduction to Databases
## Session 06


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Math & Numeric Functions](https://www.w3schools.com/sql/sql_ref_sqlserver.asp#midcontentadcontainer)     |


## Code Highlights
New column using Addition
```sql
USE workshop;
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,1 + 2 as MyNewColumn
  FROM Tanks;
```

New column using Subtraction
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,100 - 10 as MyNewColumn
  FROM Tanks;
```

New column using Division
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,500/10 as MyNewColumn
  FROM Tanks;
```

New column using Multiplication
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
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
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
  FROM Tanks;
```
- Find the radius of the tank by dividing the diameter by 2
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,tank_diameter_ft/2 as tank_radius_ft
  FROM Tanks;
```
- What is the radius<sup>2</sup>? Use the ```SQUARE()``` Function.
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,tank_diameter_ft/2 as tank_radius_ft
      ,SQUARE(tank_diameter_ft/2) as tank_radius_sq_ft
  FROM Tanks;
```
- Calculate the Area using radius<sup>2</sup> x Pi using the ```PI()``` Function
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,tank_diameter_ft/2 as tank_radius_ft
      ,SQUARE(tank_diameter_ft/2) as tank_radius_sq_ft
      ,SQUARE(tank_diameter_ft/2)*PI() as tank_area_sq_ft
  FROM Tanks;
```

- Calculate the Tank Volume (area x length)
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,tank_diameter_ft/2 as tank_radius_ft
      ,SQUARE(tank_diameter_ft/2) as tank_radius_sq_ft
      ,SQUARE(tank_diameter_ft/2)*PI() as tank_area_sq_ft
      ,SQUARE(tank_diameter_ft/2)*PI()*tank_length_ft as tank_volume_ft
  FROM Tanks;
```

- Calculate the gallons of capacity using a [tank volume to gallons conversion value](https://www.asknumbers.com/cubic-feet-to-gallons.aspx).
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,tank_diameter_ft/2 as tank_radius_ft
      ,SQUARE(tank_diameter_ft/2) as tank_radius_sq_ft
      ,SQUARE(tank_diameter_ft/2) * PI() as tank_area_sq_ft
      ,SQUARE(tank_diameter_ft/2) * PI() * tank_length_ft as tank_volume_ft
      ,SQUARE(tank_diameter_ft/2) * PI() * tank_length_ft * 7.4805194805195 as tank_capacity_gals
  FROM Tanks;
```

- Let's round the result to 2 floating points using the ```ROUND()``` function.
> Basic Syntax: ```ROUND(number, decimals)```</br>Example: ```ROUND(152.25667, 2)```</br>Example Result: ```152.25```
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,SQUARE(tank_diameter_ft/2) as tank_radius_sq_ft
      ,SQUARE(tank_diameter_ft/2) * PI() as tank_area_sq_ft
      ,SQUARE(tank_diameter_ft/2) * PI() * tank_length_ft as tank_volume_ft
      ,SQUARE(tank_diameter_ft/2) * PI() * tank_length_ft * 7.4805194805195 as tank_capacity_gals
      ,ROUND(SQUARE(tank_diameter_ft/2) * PI() * tank_length_ft * 7.4805194805195, 2) as tank_capacity_gals_rounded
  FROM Tanks;
```

- Cleanup.
```sql
SELECT design_id
      ,design_name
      ,designed_by
      ,tank_length_ft
      ,tank_diameter_ft
      ,ROUND(SQUARE(tank_diameter_ft/2) * PI() * tank_length_ft * 7.4805194805195, 2) as tank_capacity_gals
  FROM Tanks;
```

## Notes
- I considered teaching the ```RAND()``` function, but it seemed needlessly confusing. For more information, read about it [here](https://www.w3schools.com/sql/func_sqlserver_rand.asp).
> Basic Syntax: ```RAND(seed)```</br>Example: ```RAND(123456)```</br>Example Result: ```0.0139254973340301```


- ```ABS()``` can be used to get an absolute value.
> Basic Syntax: ```ABS(number)```</br>Example: ```ABS(100-300)```</br>Example Result: ```200```

## Challenge
- For each record in ```Products```, multiply the ```UnitPrice``` by ```UnitsInStock``` so we can see the total dollar value of what we have in the warehouse per product.
- For each record in ```Products```, multiply the ```UnitPrice``` by ```UnitsOnOrder``` so we can see how much money we have tied up in orders per product.
- What is the most expensive product cost in ```Products```, according to ```UnitPrice```? Using ```MAX```
- What is the least expensive product cost in ```Products```, according to ```UnitPrice```? Using ```MIN```
- What is the average product cost in ```Products```, according to ```UnitPrice```? Using ```AVG```
- Assuming that the ```Products``` table UnitPrice is what we paid for the product, and the ```Order Details``` UnitPrice is what we sold it for, ```JOIN``` the ```Products``` table with the ```Order Details``` table to see how much money we're making or losing money per order. Remember to consider discount and quantity, but disregard freight.