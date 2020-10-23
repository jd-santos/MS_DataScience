#pet_type
INSERT INTO M09_LE.pet_type (pet_type)
VALUES ('A literal unicorn'),
       ('Buff Chihuahua'),
       ('An inseparable band of revolutionary hamsters'),
       ('Dwayne the Rock Johnson'),
       ('Turtle, Ninja');

INSERT INTO M09_LE.roomy (rmy_name, rmy_birthdate)
VALUES ('JD', '1991-05-05'),
       ('Jon WeHaddaBabyItsaBoy', '1992-10-15'),
       ('Tim Apple', '1960-11-01');

# pets
insert into M09_LE.pets (pet_name, pet_birthdate, rmy_id, pt_id)
VALUES ('James Ogilvy, Earl of Seafield'        , '1664-07-11', 99083, 7813),
       ('Bandito'                               , '2014-03-02', 99083, 7814),
       ('Karl, Friedrich, and Pierre Joseph'    , '1991-04-29', 99084, 7815),
       ('Dwayne'                                , '1972-05-02', 99085, 7816),
       ('Donatello'                             , '1386-01-01', 99085, 7817)
;
UPDATE M09_LE.pets
    SET pet_name = 'Professor McProfessorface'
    WHERE pet_id = 9170;

DELETE FROM M09_LE.pets
    WHERE pet_id = 9170;

# Some selects to check my work
SELECT * FROM M09_LE.roomy
WHERE rmy_name in ('JD', 'Jon WeHaddaBabyItsaBoy', 'Tim Apple')
;
SELECT * FROM M09_LE.pets
WHERE pet_id = 9170
;

# Using a single SQL statement, create a new table in M09_LE
#...Insert the data from customers and orders tables
CREATE TABLE `M09_LE`.DeLosSantos_Jonathan AS
    SELECT c.*, o.orderid, o.employeeid, o.orderdate, o.requireddate, o.shippeddate,
           o.shipvia, o.freight, o.shipname, o.shipaddress, o.shipcity, o.shipregion, o.shippostalcode, o.shipcountry
    FROM sql_practice.customers c
        LEFT JOIN sql_practice.orders o USING (CustomerID)
;
