"""Snowflake database connector with connection pooling and query optimization."""

import snowflake.connector
from contextlib import contextmanager
from typing import Optional, Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class SnowflakeConnector:
    """Connects to Snowflake data warehouse with optimized query execution."""
    
    def __init__(
        self,
        account: str,
        database: str,
        schema: str = 'PUBLIC',
        warehouse: Optional[str] = None,
        role: Optional[str] = None
    ):
        self.account = account
        self.database = database
        self.schema = schema
        self.warehouse = warehouse
        self.role = role
        self._conn = None
    
    @contextmanager
    def connect(self):
        """Context manager for Snowflake connections with auto-close."""
        try:
            self._conn = snowflake.connector.connect(
                account=self.account,
                user=self._get_credential('user'),
                password=self._get_credential('password'),
                database=self.database,
                schema=self.schema,
                warehouse=self.warehouse,
                role=self.role
            )
            yield self._conn
        except Exception as e:
            logger.error(f"Snowflake connection error: {e}")
            raise
        finally:
            if self._conn:
                self._conn.close()
    
    def execute_query(self, query: str, params: Optional[Dict] = None) -> List[Dict[str, Any]]:
        """Execute a query and return results as list of dictionaries."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            return [dict(zip(columns, row)) for row in rows]
    
    def _get_credential(self, key: str) -> str:
        """Retrieve credentials from environment variables."""
        import os
        return os.environ.get(f"SNOWFLAKE_{key.upper()}", '')
