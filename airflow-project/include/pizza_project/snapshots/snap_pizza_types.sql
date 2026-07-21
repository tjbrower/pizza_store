{% snapshot snap_pizza_types %}

{{
    config(
        target_schema='snapshots',
        unique_key='pizza_type_id',
        strategy='check',
        check_cols=['pizza_category', 'ingredients']
    )
}}

select * from {{ ref('stg_pizza_types') }}

{% endsnapshot %}