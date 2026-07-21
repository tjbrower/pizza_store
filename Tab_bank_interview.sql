select 
    customer_ids,
    end_date,
    SSN,
    count(SSN) numofinstances
from 
    customers c
join customer_transactions ct
    on c.customer_id = ct.customer_id
group by 1
having count(ssn) > 1
--limit 0;

describe customers;
