select 
    order_id
    ,CAST(date as DATE) AS order_date
    ,CAST(time AS time) as order_time
from orders_raw