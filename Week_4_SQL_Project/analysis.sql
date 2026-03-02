WITH home_wins AS (
   	SELECT
  		HomeTeam,
  		COUNT(*) as  total_home_wins,
  		RANK() OVER(ORDER BY COUNT(*) DESC) as  rank
  	FROM premier_league
    WHERE "FT Result" = 'H'
    GROUP BY hometeam
  )
  SELECT * FROM home_wins WHERE rank <=10;



  WITH liverpool_matches AS (
    -- Домашние матчи
    SELECT Date, Season, 'Home' as venue, "FTH Goals" as goals
    FROM premier_league
    WHERE HomeTeam = 'Liverpool'
    
    UNION ALL
    
    -- Гостевые матчи
    SELECT Date, Season, 'Away' as venue, "FTA Goals" as goals
    FROM premier_league
    WHERE AwayTeam = 'Liverpool'
)
SELECT 
    Date,
    Season,
    venue,
    goals,
    SUM(goals) OVER(PARTITION BY Season ORDER BY substr(Date, -4) || '-' ||
                    							substr(Date, -7, 2) || '-' ||
                    							substr(Date, 1, instr(Date, '/') - 1)
) as running_total
FROM liverpool_matches
WHERE "season" = '2013/14'
ORDER BY 
    substr(Date, -4) || '-' ||  -- Год (последние 4 символа)
    substr(Date, -7, 2) || '-' ||  -- Месяц
    substr(Date, 1, instr(Date, '/') - 1)  -- День до первого /;








	SELECT 
    'Home' as venue,
    COUNT(CASE WHEN "FT Result" = 'H' THEN 1 END) as wins,
    COUNT(CASE WHEN "FT Result" = 'D' THEN 1 END) as draws,
    COUNT(CASE WHEN "FT Result" = 'A' THEN 1 END) as losses,
    AVG(`FTH  Goals`) as avg_goals
FROM premier_league

UNION ALL

SELECT 
    'Away' as venue,
    COUNT(CASE WHEN "FT Result" = 'A' THEN 1 END) as wins,
    COUNT(CASE WHEN "FT Result" = 'D' THEN 1 END) as draws,
    COUNT(CASE WHEN "FT Result" = 'H' THEN 1 END) as losses,
    AVG(`FTA  Goals`) as avg_goals
FROM premier_league









