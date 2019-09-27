import MySQLdb
import generate_config as config

connection = MySQLdb.connect(
    host=config.database["host"],
    user=config.database["user_name"],
    passwd=config.database["password"])  # create the connection

cursor = connection.cursor()  # get the cursor

cursor.execute("use {0}".format(config.database["name"]))  # select the database
cursor.execute("show tables")


query_column_info = """select 
                            c.column_name,
                            c.data_type,
                            c.character_maximum_length,
                            c.numeric_precision,
                            c.numeric_scale,
                            c.is_nullable,
                            c.extra, 
                            c.column_comment,
                            c.column_key,
                            c.column_default
                        from information_schema.columns as c
                        where  c.table_name='{0}' 
                        order by c.ordinal_position"""

query_check_index = """select 
                            count(s.index_name) as has_index
                        from information_schema.statistics as s
                        where  s.table_name='{0}' 
                        """

query_constraint = """select 
                            k.referenced_table_name,
                            k.referenced_column_name 
                        from information_schema.key_column_usage as k
                        where k.column_name='{0}' and  k.table_name='{1}' AND k.referenced_table_name IS NOT NULL
                        """