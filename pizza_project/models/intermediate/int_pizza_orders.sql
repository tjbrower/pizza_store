-- From the stg_orders table we should bring in ALL columns as we need the date and the time
-- From the stg_order_details table we should bring in ALL columns as we need to join to other tables and then get the quantity amounts
-- - NOTE! There really is only 1 column of 'new' data here. The other 3 columns just join to other tables
-- From the stg_pizzas table, we should bring in ALL the columns as 2 of them will join to others and 2 will give us size and prices
-- From the stg_pizza_types table, we should bring in everything so we can do some analysis on ingredients as well as what categories are doing well

select 
  sod.*
  ,sp.pizza_type_id
  ,sp.pizza_size
  ,sp.pizza_price
  ,(quantity * pizza_price) as charge_by_order_details_id
  ,spt.pizza_name
  ,spt.pizza_category
  ,spt.ingredients
  ,so.order_date
  ,so.order_time
from {{ref('stg_order_details')}} sod
left join {{ref('stg_pizzas')}} sp
  on sp.pizza_id = sod.pizza_id
left join {{ref('stg_pizza_types')}} spt
  on spt.pizza_type_id = sp.pizza_type_id
left join {{ref('stg_orders')}} so
  on so.order_id = sod.order_id
