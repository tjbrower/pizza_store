{% snapshot snap_pizzas %}

{{
    config(
        target_schema='snapshots',
        unique_key='pizza_id',
        strategy='check',
        check_cols=['pizza_price', 'pizza_size']
    )
}}

select * from {{ ref('stg_pizzas') }}

{% endsnapshot %}