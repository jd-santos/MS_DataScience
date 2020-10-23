CREATE TABLE G31_OLAP.Flag_Dim (
    Flag_Key        INTEGER     NOT NULL    AUTO_INCREMENT,
    Code            CHAR(1)             ,
    Description     TEXT                ,
    PRIMARY KEY (Flag_Key)
);

INSERT INTO G31_OLAP.Flag_Dim(Code, Description)
SELECT f.code, f.flag_desc
FROM FCP_CBP_OLTP.Flag f;

CREATE VIEW G31_OLAP.Emp_Flag_Vw AS
    SELECT f.Flag_Key AS Emp_Flag_Key, f.Code, f.Description
    FROM G31_OLAP.Flag_Dim f
;

CREATE VIEW G31_OLAP.Yr_Flag_Vw AS
    SELECT f.Flag_Key AS Yr_Flag_Key, f.Code, f.Description
    FROM G31_OLAP.Flag_Dim f
;

CREATE VIEW G31_OLAP.Qtr_Flag_Vw AS
    SELECT f.Flag_Key AS Qtr_Flag_Key, f.Code, f.Description
    FROM G31_OLAP.Flag_Dim f
;

#--------------------------------------------
# Will's Portion (Fact Table)
CREATE TABLE G31_OLAP.District_Industry_Fact
(
    District_Key       INTEGER     NOT NULL,
    Industry_Key      INTEGER     NOT NULL,
    Emp_Flag_Key        INTEGER     NOT NULL,
    Yr_Flag_Key     INTEGER     NOT NULL,
    Qtr_Flag_Key    INTEGER     NOT NULL,
    Year    YEAR,
    q1_pr   INTEGER,
    yr_pr   INTEGER,
    num_est INTEGER,
    num_empl    INTEGER,
    PRIMARY KEY (District_Key, Industry_Key, Emp_Flag_Key, Yr_Flag_Key, Qtr_Flag_Key),
    CONSTRAINT District_Key FOREIGN KEY (District_Key) REFERENCES District_Dim(District_Key),
    CONSTRAINT Industry_Key FOREIGN KEY (Industry_Key) REFERENCES Industry_Dim(Industry_Key),
    CONSTRAINT Emp_Flag_Key FOREIGN KEY (Emp_Flag_Key) REFERENCES Emp_Flag_Vw(Emp_Flag_Key),
    CONSTRAINT Yr_Flag_Key FOREIGN KEY (Yr_Flag_Key) REFERENCES Yr_Flag_Vw(Yr_Flag_Key),
    CONSTRAINT Qtr_Flag_Key FOREIGN KEY (Qtr_Flag_Key) REFERENCES Qtr_Flag_Vw(Qtr_Flag_Key)
);

INSERT INTO G31_OLAP.District_Industry_Fact (District_Key,
                                    Industry_Key,
                                    Emp_Flag_Key,
                                    Yr_Flag_Key,
                                    Qtr_Flag_Key,
                                    Year, q1_pr,
                                    yr_pr,
                                    num_est,
                                    num_empl)
SELECT District_Dim.District_Key,
       Industry_Dim.Industry_Key,
       Emp_Flag_Vw.Emp_Flag_Key,
       Yr_Flag_Vw.Yr_Flag_Key,
       Qtr_Flag_Vw.Qtr_Flag_Key,
       full_dataset.YR,
       full_dataset.Q1_PR,
       full_dataset.YR_PR,
       full_dataset.NUM_EST,
       full_dataset.NUM_EMPL
FROM FCP_CBP.full_dataset, District_Dim, Industry_Dim, G31_OLAP.Emp_Flag_Vw, G31_OLAP.Yr_Flag_Vw, G31_OLAP.Qtr_Flag_Vw
WHERE Industry_Dim.NAICS_Code = full_dataset.NAICS
        AND District_Dim.Congressional_Session = full_dataset.CONGRESS
        AND District_Dim.District_Num = full_dataset.DISTRICT
        AND District_Dim.State = full_dataset.STATE
        AND District_Dim.FIPS = full_dataset.STATE_FIPS
        AND Emp_Flag_Vw.Code = full_dataset.EMPL_F
        AND Yr_Flag_Vw.Code = full_dataset.YR_PR_F
        AND Qtr_Flag_Vw.Code = full_dataset.Q1_PR_F
