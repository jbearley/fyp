CREATE TABLE CLASSES (
    ClassID VARCHAR(10),
    Prereqs VARCHAR(100),
    Coreq VARCHAR(100),
    GradeReq VARCHAR(10),
    Fall TINYINT,
    JTerm TINYINT,
    Spring TINYINT,
    Summer TINYINT,
    Credits DECIMAL(3,1)
);

INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACCT 41", "", "", "", 1, 0, 1, 1, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACCT 42", "ACCT 41", "", "", 1, 0, 1, 1, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 131", "MATH 70", "ACTS 131L", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 131L", "MATH 70" "ACTS 131", "", 1, 0, 1, 0, .5)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 195", "FIN 101, MKTG 101, MGMT 110, MGMT 120", "", "SR", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BLAW 60", "", "", "SO", 1, 0, 1, 1, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 001", "", "", "", 1, 0, 1, 0, 0)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 002", "BUS 001", "", "", 1, 0, 1, 0, 0)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 003", "BUS 002", "", "", 1, 0, 1, 0, 0)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 004", "BUS 003", "", "", 1, 0, 1, 0, 0)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 70", "BUS 70", "", "SO", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 73", "", "", "", 1, 0, 1, 0, 2)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("BUS 74", "", "", "", 1, 0, 1, 0, 2)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ECON 2", "", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("IS 44", "", "", "", 1, 0, 1, 1, 2)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("IS 75", "", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("FIN 101", "ACCT 42, IS 44, ECON 2, STAT 71, STAT 30, ACTS 131", "", "", 1, 0, 1, 1, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("MGMT 110", "", "",  "SO", 1, 0, 1, 1, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("MGMT 120", "STAT 72, ACTS 135", "", "", 1, 1, 1, 0)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("MKTG 101", "ECON 2", "", "SO", 1, 0, 1, 1, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("MATH 50", "", "", "", 1, 0, 1, 1, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("MATH 70", "MATH 50", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 50", "", "", "", 1, 0, 0, 0, 0)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 120", "MATH 70", "ACTS 120L", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 120L", "MATH 70", "ACTS 120L", "", 1, 0, 1, 0, .5)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 135", "ACTS 131", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 140", "ACT 135", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 150", "ACTS 120, ACTS 131", "", "", 1, 0, 0, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 161", "ACTS 131", "", "", 0, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 190", "", "", "SR", 0, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ECON 10", "", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("INS 51", "", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("STAT 40", "", "", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("STAT 170", "", "STAT 40", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 155", "", "ACTS 150", "", 0, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("ACTS 165", "", "ACTS 135", "", 1, 0, 0, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("FIN 102", "", "ECON 10, FIN 10, ACTS 135, STAT 71, STAT 130", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("FIN 121", "", "FIN 119, ACTS 120, ACTS 131, STAT 71, STAT 130", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("MATH 100", "", "MATH 70", "", 1, 0, 1, 0, 3)
INSERT INTO CLASSES (ClassID, Prereqs, Coreq, GradeReq, Fall, JTerm, Spring, Summer, Credits) VALUES ("STAT 172", "", "STAT 130, ACTS 131, STAT 40, STAT 170, MATH 70", "", 1, 0, 0, 0, 3