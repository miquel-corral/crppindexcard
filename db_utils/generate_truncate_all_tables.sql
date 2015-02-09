select 'truncate table "' || tablename || '" cascade;'
from pg_tables where schemaname = 'public';