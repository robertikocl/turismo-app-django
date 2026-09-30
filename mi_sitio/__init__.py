import pymysql
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

pymysql.version_info = (2, 2, 7, "final", 0)
pymysql.install_as_MySQLdb()

# Compatibilidad directa con MariaDB 10.4 de XAMPP
BaseDatabaseWrapper.check_database_version_supported = lambda self: None
DatabaseFeatures.can_return_columns_from_insert = False
DatabaseFeatures.can_return_rows_from_bulk_insert = False
DatabaseFeatures.has_native_uuid_field = False