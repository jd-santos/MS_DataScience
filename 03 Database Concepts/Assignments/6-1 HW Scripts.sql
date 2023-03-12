SELECT CategoryName, Description
FROM categories;

SELECT FirstName, LastName, HireDate
FROM employees
WHERE Title = 'Sales Representative' AND Country = 'USA';

SELECT OrderID, OrderDate
FROM orders
WHERE EmployeeID = ;

SELECT SupplierID, ContactName, ContactTitle
FROM suppliers
WHERE ContactTitle != 'Marketing Manager';

SELECT ProductID, ProductName
FROM products
WHERE ProductName LIKE '%queso%';

SELECT OrderID, CustomerID, ShipCountry
FROM orders
WHERE ShipCountry = 'France' OR ShipCountry = 'Belgium';

SELECT OrderID, CustomerID, ShipCountry
FROM orders
WHERE ShipCountry in ('Brazil', 'Mexico', 'Argentina', 'Venezuela');

SELECT FirstName, LastName, Title, BirthDate
FROM employees
ORDER BY BirthDate;