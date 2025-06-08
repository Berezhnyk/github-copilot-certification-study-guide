"""
API Documentation MCP Server - Live API Documentation and Testing
TODO: Build MCP server providing live API documentation and testing capabilities
This exercise demonstrates integrating OpenAPI/Swagger with Copilot through MCP
"""

import asyncio
import json
import yaml
import requests
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from datetime import datetime
from urllib.parse import urljoin

from mcp import MCPServer, Resource, Tool, ToolResult
import openapi_spec_validator
from openapi_spec_validator import validate_spec

# TODO: Ask Copilot to help implement comprehensive API documentation MCP server

@dataclass
class APIEndpoint:
    """API endpoint information"""
    path: str
    method: str
    summary: str
    description: str
    parameters: List[Dict[str, Any]]
    request_body: Optional[Dict[str, Any]]
    responses: Dict[str, Dict[str, Any]]
    tags: List[str]
    security: List[Dict[str, Any]]

@dataclass
class APITestResult:
    """API test execution result"""
    endpoint: str
    method: str
    status_code: int
    response_time_ms: float
    success: bool
    response_body: Any
    error_message: Optional[str]
    validation_errors: List[str]

class APIDocumentationMCPServer(MCPServer):
    """MCP Server for API documentation and testing capabilities"""
    
    def __init__(self, openapi_specs: List[str], server_name: str = "api-documentation"):
        super().__init__(server_name)
        self.openapi_specs = openapi_specs  # URLs or file paths to OpenAPI specs
        self.parsed_specs = {}
        self.endpoints_cache = {}
        self.test_history = []
        
    async def initialize(self):
        """Initialize by loading and parsing OpenAPI specifications"""
        for spec_source in self.openapi_specs:
            try:
                spec_data = await self.load_openapi_spec(spec_source)
                self.parsed_specs[spec_source] = spec_data
                self.endpoints_cache[spec_source] = self.extract_endpoints(spec_data)
                print(f"Loaded API spec: {spec_source}")
            except Exception as e:
                print(f"Failed to load spec {spec_source}: {e}")
    
    async def load_openapi_spec(self, source: str) -> Dict[str, Any]:
        """Load OpenAPI specification from URL or file"""
        # TODO: Implement robust spec loading with validation
        if source.startswith(('http://', 'https://')):
            response = requests.get(source)
            response.raise_for_status()
            
            if source.endswith('.yaml') or source.endswith('.yml'):
                spec_data = yaml.safe_load(response.text)
            else:
                spec_data = response.json()
        else:
            # Load from file
            with open(source, 'r') as f:
                if source.endswith('.yaml') or source.endswith('.yml'):
                    spec_data = yaml.safe_load(f)
                else:
                    spec_data = json.load(f)
        
        # Validate OpenAPI specification
        validate_spec(spec_data)
        return spec_data
    
    def extract_endpoints(self, spec_data: Dict[str, Any]) -> List[APIEndpoint]:
        """Extract endpoint information from OpenAPI spec"""
        # TODO: Implement comprehensive endpoint extraction
        endpoints = []
        
        base_url = self.get_base_url(spec_data)
        paths = spec_data.get('paths', {})
        
        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method in ['get', 'post', 'put', 'delete', 'patch', 'head', 'options']:
                    endpoint = APIEndpoint(
                        path=path,
                        method=method.upper(),
                        summary=operation.get('summary', ''),
                        description=operation.get('description', ''),
                        parameters=operation.get('parameters', []),
                        request_body=operation.get('requestBody'),
                        responses=operation.get('responses', {}),
                        tags=operation.get('tags', []),
                        security=operation.get('security', [])
                    )
                    endpoints.append(endpoint)
        
        return endpoints
    
    async def list_resources(self) -> List[Resource]:
        """List API documentation resources for Copilot"""
        resources = []
        
        for spec_source, spec_data in self.parsed_specs.items():
            # API overview
            api_name = spec_data.get('info', {}).get('title', 'Unknown API')
            resources.append(Resource(
                uri=f"api://specs/{spec_source}",
                name=f"API Spec: {api_name}",
                mimeType="application/json",
                description=f"Complete OpenAPI specification for {api_name}"
            ))
            
            # Individual endpoints
            for endpoint in self.endpoints_cache[spec_source]:
                endpoint_id = f"{endpoint.method}_{endpoint.path.replace('/', '_')}"
                resources.append(Resource(
                    uri=f"api://endpoints/{spec_source}/{endpoint_id}",
                    name=f"{endpoint.method} {endpoint.path}",
                    mimeType="application/json",
                    description=f"{endpoint.summary} - {endpoint.description}"
                ))
        
        # Test results and history
        resources.append(Resource(
            uri="api://test-results",
            name="API Test Results",
            mimeType="application/json",
            description="Recent API test execution results and performance metrics"
        ))
        
        return resources
    
    async def read_resource(self, uri: str) -> str:
        """Read detailed API documentation resources"""
        try:
            if uri.startswith("api://specs/"):
                spec_source = uri.replace("api://specs/", "")
                return json.dumps(self.parsed_specs[spec_source], indent=2)
            
            elif uri.startswith("api://endpoints/"):
                parts = uri.replace("api://endpoints/", "").split("/")
                spec_source, endpoint_id = "/".join(parts[:-1]), parts[-1]
                return await self.get_endpoint_documentation(spec_source, endpoint_id)
            
            elif uri == "api://test-results":
                return json.dumps(self.test_history[-50:], indent=2, default=str)
            
            else:
                raise ValueError(f"Unknown resource URI: {uri}")
                
        except Exception as e:
            return json.dumps({"error": str(e)})
    
    async def get_endpoint_documentation(self, spec_source: str, endpoint_id: str) -> str:
        """Get comprehensive endpoint documentation"""
        # TODO: Implement detailed endpoint documentation generation
        endpoints = self.endpoints_cache[spec_source]
        endpoint = next((e for e in endpoints if f"{e.method}_{e.path.replace('/', '_')}" == endpoint_id), None)
        
        if not endpoint:
            return json.dumps({"error": "Endpoint not found"})
        
        # Generate comprehensive documentation
        doc = {
            "endpoint": {
                "path": endpoint.path,
                "method": endpoint.method,
                "summary": endpoint.summary,
                "description": endpoint.description,
                "tags": endpoint.tags
            },
            "parameters": self.format_parameters(endpoint.parameters),
            "request_body": self.format_request_body(endpoint.request_body),
            "responses": self.format_responses(endpoint.responses),
            "security": endpoint.security,
            "examples": await self.generate_endpoint_examples(endpoint),
            "test_template": await self.generate_test_template(endpoint),
            "curl_examples": await self.generate_curl_examples(endpoint)
        }
        
        return json.dumps(doc, indent=2)
    
    async def call_tool(self, name: str, arguments: dict) -> ToolResult:
        """Execute API documentation and testing tools"""
        try:
            if name == "test_endpoint":
                return await self.test_endpoint(
                    arguments["endpoint"],
                    arguments["method"], 
                    arguments.get("parameters", {}),
                    arguments.get("body")
                )
            elif name == "validate_response":
                return await self.validate_response(
                    arguments["endpoint"],
                    arguments["method"],
                    arguments["response"]
                )
            elif name == "generate_client_code":
                return await self.generate_client_code(
                    arguments["endpoint"],
                    arguments["language"]
                )
            elif name == "run_test_suite":
                return await self.run_test_suite(arguments.get("endpoints"))
            elif name == "generate_mock_data":
                return await self.generate_mock_data(
                    arguments["schema"],
                    arguments.get("count", 1)
                )
            else:
                return ToolResult(
                    content=f"Unknown tool: {name}",
                    isError=True
                )
        except Exception as e:
            return ToolResult(
                content=f"Tool execution failed: {str(e)}",
                isError=True
            )
    
    async def test_endpoint(
        self, 
        endpoint: str, 
        method: str, 
        parameters: Dict[str, Any] = None, 
        body: Any = None
    ) -> ToolResult:
        """Test API endpoint with given parameters"""
        # TODO: Implement comprehensive endpoint testing
        start_time = datetime.now()
        
        try:
            # Find the endpoint spec
            endpoint_spec = self.find_endpoint_spec(endpoint, method)
            if not endpoint_spec:
                return ToolResult(
                    content=f"Endpoint {method} {endpoint} not found in specifications",
                    isError=True
                )
            
            # Build request
            url = self.build_request_url(endpoint, parameters)
            headers = self.build_request_headers(endpoint_spec)
            
            # Execute request
            response = requests.request(
                method=method.lower(),
                url=url,
                headers=headers,
                json=body if body else None,
                timeout=30
            )
            
            # Calculate response time
            response_time = (datetime.now() - start_time).total_seconds() * 1000
            
            # Validate response against spec
            validation_errors = await self.validate_response_against_spec(
                endpoint_spec, response
            )
            
            # Create test result
            test_result = APITestResult(
                endpoint=endpoint,
                method=method,
                status_code=response.status_code,
                response_time_ms=response_time,
                success=200 <= response.status_code < 300,
                response_body=response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text,
                error_message=None if 200 <= response.status_code < 300 else f"HTTP {response.status_code}",
                validation_errors=validation_errors
            )
            
            # Store test result
            self.test_history.append(test_result)
            
            return ToolResult(
                content=json.dumps({
                    "test_result": test_result.__dict__,
                    "response_headers": dict(response.headers),
                    "validation_passed": len(validation_errors) == 0
                }, indent=2, default=str),
                isError=not test_result.success
            )
            
        except Exception as e:
            error_result = APITestResult(
                endpoint=endpoint,
                method=method,
                status_code=0,
                response_time_ms=(datetime.now() - start_time).total_seconds() * 1000,
                success=False,
                response_body=None,
                error_message=str(e),
                validation_errors=[]
            )
            
            self.test_history.append(error_result)
            
            return ToolResult(
                content=json.dumps(error_result.__dict__, indent=2, default=str),
                isError=True
            )
    
    async def generate_client_code(self, endpoint: str, language: str) -> ToolResult:
        """Generate client code for API endpoint in specified language"""
        # TODO: Implement client code generation for multiple languages
        endpoint_spec = self.find_endpoint_spec(endpoint, "GET")  # Default to GET
        
        if language.lower() == "javascript":
            code = await self.generate_javascript_client(endpoint_spec)
        elif language.lower() == "python":
            code = await self.generate_python_client(endpoint_spec)
        elif language.lower() == "curl":
            code = await self.generate_curl_client(endpoint_spec)
        else:
            return ToolResult(
                content=f"Language {language} not supported",
                isError=True
            )
        
        return ToolResult(
            content=json.dumps({
                "language": language,
                "endpoint": endpoint,
                "generated_code": code,
                "usage_instructions": f"Generated {language} client code for {endpoint}"
            }, indent=2),
            isError=False
        )
    
    async def run_test_suite(self, endpoints: Optional[List[str]] = None) -> ToolResult:
        """Run comprehensive test suite for API endpoints"""
        # TODO: Implement automated test suite execution
        if not endpoints:
            # Test all endpoints
            endpoints = []
            for spec_source in self.endpoints_cache:
                for endpoint in self.endpoints_cache[spec_source]:
                    endpoints.append(f"{endpoint.method} {endpoint.path}")
        
        test_results = []
        for endpoint_desc in endpoints:
            method, path = endpoint_desc.split(" ", 1)
            result = await self.test_endpoint(path, method)
            test_results.append(result)
        
        # Aggregate results
        total_tests = len(test_results)
        passed_tests = sum(1 for r in test_results if not r.isError)
        
        suite_result = {
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "failed_tests": total_tests - passed_tests,
            "success_rate": (passed_tests / total_tests) * 100 if total_tests > 0 else 0,
            "test_results": [json.loads(r.content) for r in test_results],
            "execution_time": datetime.now().isoformat()
        }
        
        return ToolResult(
            content=json.dumps(suite_result, indent=2),
            isError=passed_tests < total_tests
        )
    
    # TODO: Ask Copilot to implement utility methods
    def get_base_url(self, spec_data: Dict[str, Any]) -> str:
        """Extract base URL from OpenAPI spec"""
        servers = spec_data.get('servers', [])
        if servers:
            return servers[0].get('url', 'http://localhost')
        return 'http://localhost'
    
    def find_endpoint_spec(self, path: str, method: str) -> Optional[Dict[str, Any]]:
        """Find endpoint specification in loaded specs"""
        for spec_source in self.endpoints_cache:
            for endpoint in self.endpoints_cache[spec_source]:
                if endpoint.path == path and endpoint.method == method:
                    return endpoint
        return None
    
    async def generate_mock_data(self, schema: Dict[str, Any], count: int = 1) -> ToolResult:
        """Generate mock data based on OpenAPI schema"""
        # TODO: Implement schema-based mock data generation
        mock_data = []
        
        for _ in range(count):
            mock_item = await self.generate_from_schema(schema)
            mock_data.append(mock_item)
        
        return ToolResult(
            content=json.dumps({
                "schema": schema,
                "generated_count": count,
                "mock_data": mock_data
            }, indent=2),
            isError=False
        )

# TODO: Register MCP tools for API operations
def create_api_documentation_tools() -> List[Tool]:
    """Create MCP tools for API documentation and testing"""
    return [
        Tool(
            name="test_endpoint",
            description="Test API endpoint with specified parameters",
            inputSchema={
                "type": "object",
                "properties": {
                    "endpoint": {"type": "string", "description": "API endpoint path"},
                    "method": {"type": "string", "description": "HTTP method"},
                    "parameters": {"type": "object", "description": "Request parameters"},
                    "body": {"description": "Request body for POST/PUT requests"}
                },
                "required": ["endpoint", "method"]
            }
        ),
        Tool(
            name="generate_client_code",
            description="Generate client code for API endpoint",
            inputSchema={
                "type": "object",
                "properties": {
                    "endpoint": {"type": "string", "description": "API endpoint path"},
                    "language": {
                        "type": "string", 
                        "enum": ["javascript", "python", "curl"],
                        "description": "Programming language for client code"
                    }
                },
                "required": ["endpoint", "language"]
            }
        ),
        Tool(
            name="validate_response",
            description="Validate API response against OpenAPI specification",
            inputSchema={
                "type": "object",
                "properties": {
                    "endpoint": {"type": "string", "description": "API endpoint path"},
                    "method": {"type": "string", "description": "HTTP method"},
                    "response": {"description": "API response to validate"}
                },
                "required": ["endpoint", "method", "response"]
            }
        ),
        Tool(
            name="run_test_suite",
            description="Run comprehensive test suite for API endpoints",
            inputSchema={
                "type": "object",
                "properties": {
                    "endpoints": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Specific endpoints to test (optional)"
                    }
                }
            }
        ),
        Tool(
            name="generate_mock_data",
            description="Generate mock data based on OpenAPI schema",
            inputSchema={
                "type": "object",
                "properties": {
                    "schema": {"type": "object", "description": "OpenAPI schema definition"},
                    "count": {"type": "integer", "description": "Number of mock items to generate"}
                },
                "required": ["schema"]
            }
        )
    ]

# Expected Copilot behaviors with API MCP server:
# - Should understand API specifications and suggest appropriate usage patterns
# - Should generate proper API client code with error handling
# - Should recommend optimal request/response patterns
# - Should help with API testing and validation
# - Should suggest improvements to API design based on OpenAPI best practices
# - Should assist with API documentation and examples generation
