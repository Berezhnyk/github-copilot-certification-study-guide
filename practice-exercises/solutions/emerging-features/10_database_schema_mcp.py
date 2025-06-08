"""
Database Schema MCP Server - Model Context Protocol Implementation
TODO: Create MCP server providing Copilot with database schema and query capabilities
This exercise demonstrates building MCP servers to extend Copilot's knowledge
"""

import asyncio
import json
import logging
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

from mcp import MCPServer, Resource, Tool, ToolResult
from sqlalchemy import create_engine, inspect, text, MetaData
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError

# TODO: Ask Copilot to help implement complete MCP server for database integration

@dataclass
class TableSchema:
    """Database table schema information"""
    name: str
    columns: List[Dict[str, Any]]
    indexes: List[Dict[str, Any]]
    foreign_keys: List[Dict[str, Any]]
    constraints: List[Dict[str, Any]]
    row_count: Optional[int] = None
    size_mb: Optional[float] = None

@dataclass
class QueryAnalysis:
    """Query execution analysis"""
    query: str
    execution_plan: str
    estimated_cost: float
    execution_time_ms: float
    rows_affected: int
    suggested_indexes: List[str]
    performance_issues: List[str]

class DatabaseMCPServer(MCPServer):
    """MCP Server for database schema and query operations"""
    
    def __init__(self, connection_string: str, server_name: str = "database-schema"):
        super().__init__(server_name)
        self.connection_string = connection_string
        self.engine: Optional[Engine] = None
        self.inspector = None
        self.metadata = None
        self.logger = logging.getLogger(__name__)
        
        # TODO: Initialize database connection and caching
        
    async def initialize(self):
        """Initialize database connection and metadata"""
        try:
            self.engine = create_engine(self.connection_string, echo=False)
            self.inspector = inspect(self.engine)
            self.metadata = MetaData()
            self.metadata.reflect(bind=self.engine)
            
            self.logger.info(f"Connected to database with {len(self.get_table_names())} tables")
        except SQLAlchemyError as e:
            self.logger.error(f"Failed to connect to database: {e}")
            raise
    
    async def list_resources(self) -> List[Resource]:
        """List all database tables and views as resources for Copilot"""
        # TODO: Implement comprehensive resource listing
        resources = []
        
        # Table schemas
        for table_name in self.get_table_names():
            resources.append(Resource(
                uri=f"db://tables/{table_name}",
                name=f"Table: {table_name}",
                mimeType="application/json",
                description=f"Schema information for {table_name} table including columns, indexes, and relationships"
            ))
        
        # Views
        for view_name in self.get_view_names():
            resources.append(Resource(
                uri=f"db://views/{view_name}",
                name=f"View: {view_name}",
                mimeType="application/json", 
                description=f"View definition and schema for {view_name}"
            ))
        
        # Stored procedures (if supported)
        for proc_name in self.get_stored_procedures():
            resources.append(Resource(
                uri=f"db://procedures/{proc_name}",
                name=f"Procedure: {proc_name}",
                mimeType="application/json",
                description=f"Stored procedure definition for {proc_name}"
            ))
        
        # Database statistics
        resources.append(Resource(
            uri="db://statistics",
            name="Database Statistics",
            mimeType="application/json",
            description="Overall database statistics including table sizes, row counts, and performance metrics"
        ))
        
        return resources
    
    async def read_resource(self, uri: str) -> str:
        """Read detailed information about database resources"""
        # TODO: Implement resource reading with detailed schema information
        try:
            if uri.startswith("db://tables/"):
                table_name = uri.split("/")[-1]
                return await self.get_table_schema_json(table_name)
            
            elif uri.startswith("db://views/"):
                view_name = uri.split("/")[-1]
                return await self.get_view_definition_json(view_name)
            
            elif uri.startswith("db://procedures/"):
                proc_name = uri.split("/")[-1]
                return await self.get_procedure_definition_json(proc_name)
            
            elif uri == "db://statistics":
                return await self.get_database_statistics_json()
            
            else:
                raise ValueError(f"Unknown resource URI: {uri}")
                
        except Exception as e:
            self.logger.error(f"Error reading resource {uri}: {e}")
            return json.dumps({"error": str(e)})
    
    async def get_table_schema_json(self, table_name: str) -> str:
        """Get comprehensive table schema information as JSON"""
        # TODO: Implement detailed table schema extraction
        schema = TableSchema(
            name=table_name,
            columns=self.inspector.get_columns(table_name),
            indexes=self.inspector.get_indexes(table_name),
            foreign_keys=self.inspector.get_foreign_keys(table_name),
            constraints=self.inspector.get_check_constraints(table_name),
            row_count=await self.get_table_row_count(table_name),
            size_mb=await self.get_table_size_mb(table_name)
        )
        
        # Add additional metadata
        schema_dict = {
            "table": schema.name,
            "columns": [
                {
                    "name": col["name"],
                    "type": str(col["type"]),
                    "nullable": col["nullable"],
                    "default": col.get("default"),
                    "primary_key": col.get("primary_key", False),
                    "autoincrement": col.get("autoincrement", False)
                }
                for col in schema.columns
            ],
            "indexes": [
                {
                    "name": idx["name"],
                    "columns": idx["column_names"],
                    "unique": idx["unique"]
                }
                for idx in schema.indexes
            ],
            "foreign_keys": [
                {
                    "name": fk.get("name"),
                    "constrained_columns": fk["constrained_columns"],
                    "referred_table": fk["referred_table"],
                    "referred_columns": fk["referred_columns"]
                }
                for fk in schema.foreign_keys
            ],
            "statistics": {
                "row_count": schema.row_count,
                "size_mb": schema.size_mb,
                "last_analyzed": datetime.now().isoformat()
            },
            "relationships": await self.get_table_relationships(table_name),
            "sample_data": await self.get_sample_data(table_name, limit=3)
        }
        
        return json.dumps(schema_dict, indent=2, default=str)
    
    async def call_tool(self, name: str, arguments: dict) -> ToolResult:
        """Execute database tools for Copilot"""
        try:
            if name == "explain_query":
                return await self.explain_query(arguments["query"])
            elif name == "suggest_indexes":
                return await self.suggest_indexes(arguments["table"], arguments.get("query"))
            elif name == "generate_migration":
                return await self.generate_migration(arguments["changes"])
            elif name == "validate_query":
                return await self.validate_query(arguments["query"])
            elif name == "optimize_query":
                return await self.optimize_query(arguments["query"])
            elif name == "analyze_performance":
                return await self.analyze_query_performance(arguments["query"])
            else:
                return ToolResult(
                    content=f"Unknown tool: {name}",
                    isError=True
                )
        except Exception as e:
            self.logger.error(f"Error executing tool {name}: {e}")
            return ToolResult(
                content=f"Tool execution failed: {str(e)}",
                isError=True
            )
    
    async def explain_query(self, query: str) -> ToolResult:
        """Explain query execution plan for optimization"""
        # TODO: Implement query explanation with detailed analysis
        try:
            with self.engine.connect() as conn:
                # Get execution plan
                explain_query = f"EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) {query}"
                result = conn.execute(text(explain_query))
                plan_json = result.fetchone()[0]
                
                # Analyze the plan
                analysis = self.analyze_execution_plan(plan_json)
                
                response = {
                    "query": query,
                    "execution_plan": plan_json,
                    "analysis": analysis,
                    "recommendations": self.generate_optimization_recommendations(analysis),
                    "estimated_cost": analysis.get("total_cost", 0),
                    "estimated_time_ms": analysis.get("total_time", 0)
                }
                
                return ToolResult(
                    content=json.dumps(response, indent=2),
                    isError=False
                )
        except Exception as e:
            return ToolResult(
                content=f"Query explanation failed: {str(e)}",
                isError=True
            )
    
    async def suggest_indexes(self, table: str, query: Optional[str] = None) -> ToolResult:
        """Suggest database indexes for table or query optimization"""
        # TODO: Implement intelligent index suggestion
        suggestions = []
        
        if query:
            # Analyze query for index opportunities
            suggestions.extend(await self.analyze_query_for_indexes(query))
        else:
            # General index suggestions for table
            suggestions.extend(await self.analyze_table_for_indexes(table))
        
        response = {
            "table": table,
            "query": query,
            "index_suggestions": suggestions,
            "priority": "high" if len(suggestions) > 0 else "low",
            "estimated_improvement": await self.estimate_index_improvement(table, suggestions)
        }
        
        return ToolResult(
            content=json.dumps(response, indent=2),
            isError=False
        )
    
    async def generate_migration(self, changes: Dict[str, Any]) -> ToolResult:
        """Generate database migration scripts"""
        # TODO: Implement migration script generation
        migration_sql = []
        rollback_sql = []
        
        for change in changes.get("changes", []):
            if change["type"] == "add_column":
                migration_sql.append(
                    f"ALTER TABLE {change['table']} ADD COLUMN {change['column']} {change['type_def']};"
                )
                rollback_sql.append(
                    f"ALTER TABLE {change['table']} DROP COLUMN {change['column']};"
                )
            
            elif change["type"] == "add_index":
                migration_sql.append(
                    f"CREATE INDEX {change['name']} ON {change['table']} ({', '.join(change['columns'])});"
                )
                rollback_sql.append(
                    f"DROP INDEX {change['name']};"
                )
        
        migration_script = {
            "version": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "description": changes.get("description", "Database migration"),
            "up_sql": migration_sql,
            "down_sql": rollback_sql[::-1],  # Reverse order for rollback
            "safety_checks": await self.generate_safety_checks(changes),
            "estimated_impact": await self.estimate_migration_impact(changes)
        }
        
        return ToolResult(
            content=json.dumps(migration_script, indent=2),
            isError=False
        )
    
    # TODO: Ask Copilot to implement utility methods
    def get_table_names(self) -> List[str]:
        """Get list of all table names"""
        return self.inspector.get_table_names()
    
    def get_view_names(self) -> List[str]:
        """Get list of all view names"""
        return self.inspector.get_view_names()
    
    def get_stored_procedures(self) -> List[str]:
        """Get list of stored procedures (database-specific)"""
        # TODO: Implement database-specific stored procedure discovery
        return []
    
    async def get_table_row_count(self, table_name: str) -> int:
        """Get approximate row count for table"""
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
                return result.scalar()
        except:
            return 0
    
    async def get_table_size_mb(self, table_name: str) -> float:
        """Get table size in MB"""
        # TODO: Implement database-specific size calculation
        return 0.0
    
    async def get_table_relationships(self, table_name: str) -> Dict[str, Any]:
        """Get table relationships and dependencies"""
        # TODO: Implement relationship analysis
        return {
            "references": [],  # Tables this table references
            "referenced_by": [],  # Tables that reference this table
            "related_tables": []  # Tables commonly joined with this table
        }
    
    async def get_sample_data(self, table_name: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Get sample data from table"""
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(f"SELECT * FROM {table_name} LIMIT {limit}"))
                columns = result.keys()
                rows = result.fetchall()
                return [dict(zip(columns, row)) for row in rows]
        except:
            return []

# TODO: Register MCP tools for Copilot
def create_database_mcp_tools() -> List[Tool]:
    """Create MCP tools for database operations"""
    return [
        Tool(
            name="explain_query",
            description="Explain SQL query execution plan and analyze performance",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL query to explain"}
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="suggest_indexes",
            description="Suggest database indexes for optimization",
            inputSchema={
                "type": "object", 
                "properties": {
                    "table": {"type": "string", "description": "Table name"},
                    "query": {"type": "string", "description": "Optional query to optimize"}
                },
                "required": ["table"]
            }
        ),
        Tool(
            name="generate_migration",
            description="Generate database migration scripts",
            inputSchema={
                "type": "object",
                "properties": {
                    "changes": {
                        "type": "object",
                        "description": "Database changes to implement"
                    }
                },
                "required": ["changes"]
            }
        ),
        Tool(
            name="validate_query", 
            description="Validate SQL query syntax and semantics",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL query to validate"}
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="optimize_query",
            description="Suggest query optimizations",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL query to optimize"}
                },
                "required": ["query"]
            }
        )
    ]

# TODO: Usage examples for Copilot
usage_examples = """
# With this MCP server, Copilot can now:

# 1. Understand your database schema
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5;

# Copilot suggests: "This query joins users and orders tables. 
# Consider adding an index on orders(user_id, created_at) for better performance."

# 2. Generate optimized queries based on schema
# Copilot can suggest proper table joins, optimal WHERE clauses, and appropriate indexes

# 3. Create migration scripts
# Copilot can generate ALTER TABLE statements and safety checks

# 4. Explain complex queries
# Copilot can break down execution plans and suggest improvements
"""

# Expected Copilot behaviors with MCP server:
# - Should understand database relationships and suggest proper joins
# - Should recommend appropriate indexes based on query patterns
# - Should generate database-appropriate SQL syntax
# - Should consider performance implications in query suggestions
# - Should suggest proper data types and constraints
# - Should help with migration planning and safety checks
