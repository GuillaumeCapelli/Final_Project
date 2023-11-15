SELECT td.date_time AS Date, COUNT(*) AS NumberOfComments
FROM TimeDate td
JOIN Scraped_Comment sc ON td.date_id = sc.date_id
GROUP BY td.date_time
ORDER BY td.date_time;

SELECT AVG(cl.comment_length) AS AverageCommentLength
FROM CommentLength cl
JOIN Scraped_Comment sc ON cl.length_id = sc.length_id;

SELECT sc.username, COUNT(*) AS NumberOfComments
FROM Scraped_Comment sc
GROUP BY sc.username
ORDER BY NumberOfComments DESC
LIMIT 10;

SELECT tc.comment, tc.toxic, tc.severe_toxic, tc.obscene, tc.threat, tc.insult, tc.identity_hate
FROM Train_comments tc
WHERE tc.toxic = 1
  AND tc.severe_toxic = 1
  AND tc.obscene = 1
  AND tc.threat = 1
  AND tc.insult = 1
  AND tc.identity_hate = 1
ORDER BY tc.comment
LIMIT 10;

SELECT AVG(comment_length) AS Average_Length_Of_Highly_Toxic_Comments
FROM train_comments
WHERE toxic = 1
  AND severe_toxic = 1
  AND obscene = 1
  AND threat = 1
  AND insult = 1
  AND identity_hate = 1;


