# Insert NAICS and Description values from full_dataset
INSERT INTO `G31_OLTP`.Industry (naics, ind_desc)
SELECT NAICS, NAICS_DESC
FROM `FCP_CBP`.full_dataset
GROUP BY NAICS, NAICS_DESC;

# flag_desc initially set to NOT NULL
# Making this field nullable to insert PK and flag_desc separately
ALTER TABLE G31_OLTP.Flag MODIFY flag_desc text(50);

# Insert Flag codes from full_dataset
INSERT INTO `G31_OLTP`.Flag (code)
SELECT DISTINCT(EMPL_F)
FROM FCP_CBP.full_dataset
# Filtering out nulls since code is PK
WHERE EMPL_F IS NOT NULL;

# Insert flag descriptions
# Source: https://www.census.gov/programs-surveys/susb/technical-documentation/data-user-resources/noise-range-flags.html
UPDATE `G31_OLTP`.Flag
SET flag_desc = (case when code = 'G' then '<2% noise'
                      when code = 'H' then '2% - 5% noise'
                      when code = 'J' then '>5% noise'
                      when code = 'D' then 'Data withheld for privacy'
                      when code = 'S' then 'Data withheld for publication standards'
                end
                )