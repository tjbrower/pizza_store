select 
    pizza_id
    ,pizza_type_id
    ,size as pizza_size
    ,CAST(price as float) as pizza_price
from pizzas_raw