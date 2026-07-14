import duckdb

def drop_tables(con):
    con.execute("""
    DROP TABLE IF EXISTS pizzas_raw            
""")
    
    con.execute("""
    DROP TABLE IF EXISTS order_details_raw
                """)

    con.execute("""
    DROP TABLE IF EXISTS orders_raw
                """)
    
    con.execute("""
    DROP TABLE IF EXISTS pizza_types_raw
                """)
    
    return()

def create_tables(con):
    con.execute("""
    CREATE TABLE orders_raw AS
    SELECT *
    FROM read_csv_auto('/usr/local/airflow/include/data_sources/orders.csv');
                """)

    con.execute("""
    CREATE TABLE order_details_raw AS
    SELECT *
    FROM read_csv_auto('/usr/local/airflow/include/data_sources/order_details.csv');
                """)

    con.execute("""
    CREATE TABLE pizza_types_raw AS
    SELECT *
    FROM read_csv_auto('/usr/local/airflow/include/data_sources/pizza_types_new.csv');
                """)

    con.execute("""
    CREATE TABLE pizzas_raw AS
    SELECT *
    FROM read_csv_auto('/usr/local/airflow/include/data_sources/pizzas.csv');
                """)

    return()

def close_db_connection(con):
    con.close()

    return()

def main():
    con = duckdb.connect("/usr/local/airflow/include/pizza_store.duckdb")
    drop_tables(con)
    create_tables(con)
    close_db_connection(con)

if __name__ == "__main__":
    main()

