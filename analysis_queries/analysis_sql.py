# with sainsbury as (SELECT * FROM transaction_descriptions 
#         WHERE td_name LIKE '%SAINSBURY%') 
#         SELECT sainsbury.td_id, sainsbury.td_name,
#         amount_spent, season, date
#         FROM sainsbury
#         INNER JOIN purchases 
#         ON sainsbury.td_id = purchases.td_id
#         ORDER BY date desc