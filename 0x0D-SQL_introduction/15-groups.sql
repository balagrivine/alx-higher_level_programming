-- script that lists number of records thith the same score


SELECT score, COUNT(*) AS 'number' FROM second_table GROUP BY score;
