select 
    order_date
    ,cast(sum(charge_by_order_details_id) as float) as daily_revenue_amnt
from
    {{ref('int_pizza_orders')}}
group by 
    1
