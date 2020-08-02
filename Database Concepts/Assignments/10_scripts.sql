CREATE TABLE `M10_LE`.`recipe_delossantos_jonathan`
(
	`recipe_id` INT(8) NOT NULL AUTO_INCREMENT,
	`name`      VARCHAR(100),
	PRIMARY KEY (`recipe_id`)
);

CREATE TABLE `M10_LE`.`supplier_delossantos_jonathan`
(
	`supplier_id`   INT(8) NOT NULL AUTO_INCREMENT,
	`name`          varchar(100) ,
	`address`       varchar(255),
	`phone`         char(10),
	`email`         varchar(100),
	`contact`       varchar(100),
	PRIMARY KEY (`supplier_id`)
);

CREATE TABLE `M10_LE`.`ingredient_delossantos_jonathan`
(
    `ingredient_id` INT(8) NOT NULL AUTO_INCREMENT,
    `name`          varchar(50),
    `supplier_id`   int(8) NOT NULL,
    PRIMARY KEY (`ingredient_id`),
    CONSTRAINT `supplier_id` FOREIGN KEY (`supplier_id`)
        REFERENCES `M10_LE`.supplier_delossantos_jonathan(`supplier_id`)
        ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE `M10_LE`.`recipe_ingr_delossantos_jonathan`
(
	`recipe_id`         INT(8) NOT NULL,
	`ingredient_id`     INT(100) NOT NULL,
	`ingredient_amt`    DECIMAL(4,2),
	`measure_type`      VARCHAR(20),
	PRIMARY KEY (`recipe_id`, `ingredient_id`),
    CONSTRAINT `recipe_id` FOREIGN KEY (`recipe_id`)
        REFERENCES `M10_LE`.recipe_delossantos_jonathan(`recipe_id`)
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT `ingredient_id` FOREIGN KEY (`ingredient_id`)
        REFERENCES `M10_LE`.ingredient_delossantos_jonathan(`ingredient_id`)
        ON DELETE NO ACTION ON UPDATE NO ACTION
);

ALTER TABLE `M10_LE`.recipe_delossantos_jonathan
    ADD COLUMN `recipe_author` varchar(100) NULL;

DROP TABLE M10_LE.recipe_ingr_delossantos_jonathan;
DROP TABLE M10_LE.recipe_delossantos_jonathan;
DROP TABLE M10_LE.ingredient_delossantos_jonathan;
DROP TABLE M10_LE.supplier_delossantos_jonathan;

CREATE VIEW M10_LE.DeLosSantos_Jonathan AS
    SELECT YEAR(o.OrderDate), DATE_FORMAT(o.OrderDate, '%M'), c.CompanyName, SUM(od.UnitPrice*od.Quantity-od.Discount) as OrderTotal
    FROM `sql_practice`.orderdetails od
       JOIN `sql_practice`.orders o USING (OrderID)
       JOIN `sql_practice`.customers c USING (CustomerID)
    GROUP BY YEAR(o.OrderDate), DATE_FORMAT(o.OrderDate, '%M'), c.CompanyName
    ORDER BY YEAR(o.OrderDate), DATE_FORMAT(o.OrderDate, '%M')
;
