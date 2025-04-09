--Top 10 Most Viewed Products
SELECT itemid,COUNT(*) AS view_count
FROM events
WHERE event='view'
GROUP BY  itemid
ORDER BY  view_count Desc
LIMIT 10

--Top 10 Products by Transactions
SELECT itemid,COUNT(*) AS transaction_count
FROM events
WHERE event = 'transaction'
GROUP BY itemid
ORDER BY transaction_count DESC
LIMIT 10;

--User Activity Over Time
SELECT Date_trunc('hour',timestamp) as hour , COUNT(*) AS total_events
FROM events
GROUP BY hour
ORDER BY hour

--Most active users
SELECT visitorid,COUNT(*) AS total_events
FROM events
GROUP BY visitorid
ORDER BY total_events DESC
LIMIT 10;

--Most recent users
with cte as(
select visitorid,date_trunc('hour',timestamp) as last_seen
from events
)
select visitorid,max(last_seen) as most_recent
from cte 
group by visitorid
order by most_recent desc
limit 10

