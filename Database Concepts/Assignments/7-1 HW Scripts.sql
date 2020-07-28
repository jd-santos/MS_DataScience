SELECT FirstName, LastName, CONCAT(FirstName, ' ',LastName) as FullName
FROM employees;

SELECT OrderID, ProductID, UnitPrice, Quantity, UnitPrice*Quantity AS TotalPrice
FROM orderdetails
ORDER BY OrderID, ProductID;

SELECT FirstName, LastName, Title, DATE(BirthDate)
FROM employees
ORDER BY BirthDate;

SELECT COUNT(*)
FROM customers;

SELECT MIN(OrderDate)
FROM orders;

SELECT DISTINCT(Country)
FROM customers;

SELECT ContactTitle, COUNT(*)
FROM customers
GROUP BY ContactTitle;