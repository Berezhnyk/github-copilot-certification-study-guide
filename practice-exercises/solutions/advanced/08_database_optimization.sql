-- Database Optimization Challenge
-- TODO: Optimize slow-performing e-commerce database queries using GitHub Copilot
-- Given: Customer orders with products and reviews performance issues
-- Requirements: Identify bottlenecks, create indexes, rewrite queries, implement caching

-- Original slow-performing schema (for reference)
-- TODO: Analyze and optimize this database structure

-- CREATE TABLE customers (
--     id BIGSERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) UNIQUE NOT NULL,
--     registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     status VARCHAR(50) DEFAULT 'active',
--     customer_tier VARCHAR(20) DEFAULT 'regular'
-- );

-- CREATE TABLE products (
--     id BIGSERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     category_id BIGINT,
--     price DECIMAL(10,2) NOT NULL,
--     stock_quantity INTEGER DEFAULT 0,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE orders (
--     id BIGSERIAL PRIMARY KEY,
--     customer_id BIGINT REFERENCES customers(id),
--     order_total DECIMAL(10,2),
--     order_status VARCHAR(50) DEFAULT 'pending',
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE order_items (
--     id BIGSERIAL PRIMARY KEY,
--     order_id BIGINT REFERENCES orders(id),
--     product_id BIGINT REFERENCES products(id),
--     quantity INTEGER NOT NULL,
--     unit_price DECIMAL(10,2) NOT NULL
-- );

-- CREATE TABLE reviews (
--     id BIGSERIAL PRIMARY KEY,
--     product_id BIGINT REFERENCES products(id),
--     customer_id BIGINT REFERENCES customers(id),
--     rating INTEGER CHECK (rating >= 1 AND rating <= 5),
--     review_text TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- ORIGINAL SLOW QUERY (for reference):
-- This query is extremely slow and needs optimization
/*
SELECT 
    c.name,
    COUNT(o.id) as order_count,
    SUM(oi.quantity * p.price) as total_spent,
    AVG(r.rating) as avg_rating
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.id
LEFT JOIN reviews r ON p.id = r.product_id
WHERE o.created_at >= '2023-01-01'
GROUP BY c.id, c.name
HAVING COUNT(o.id) > 5
ORDER BY total_spent DESC
LIMIT 100;
*/

-- TODO: 1. PERFORMANCE ANALYSIS
-- Analyze the slow query and identify bottlenecks:
-- - Missing indexes on foreign keys
-- - Inefficient JOINs causing Cartesian products
-- - Suboptimal WHERE clause placement
-- - GROUP BY on large result sets
-- - Aggregations on non-indexed columns

-- Use EXPLAIN ANALYZE to identify issues:
-- EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) [original query];

-- TODO: 2. INDEX OPTIMIZATION
-- Create strategic indexes to improve query performance

-- Primary optimization indexes:
-- TODO: Create indexes for foreign key relationships
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_customer_id_created_at 
ON orders(customer_id, created_at);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_order_items_order_id 
ON order_items(order_id);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_order_items_product_id 
ON order_items(product_id);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_reviews_product_id 
ON reviews(product_id);

-- TODO: Create composite indexes for common query patterns
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_customer_date_status 
ON orders(customer_id, created_at, order_status);

-- TODO: Create partial indexes for frequent filters
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_recent_active 
ON orders(customer_id, created_at) 
WHERE created_at >= '2023-01-01' AND order_status != 'cancelled';

-- TODO: Create covering indexes to avoid table lookups
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_order_items_covering 
ON order_items(order_id, product_id) 
INCLUDE (quantity, unit_price);

-- TODO: 3. QUERY REWRITING AND OPTIMIZATION
-- Rewrite the slow query using better techniques

-- Version 1: Using CTEs to break down complexity
-- TODO: Implement optimized version with CTEs
WITH customer_orders AS (
    -- TODO: Pre-filter and aggregate order data
    SELECT 
        customer_id,
        COUNT(*) as order_count,
        SUM(order_total) as total_spent
    FROM orders 
    WHERE created_at >= '2023-01-01'
        AND order_status != 'cancelled'
    GROUP BY customer_id
    HAVING COUNT(*) > 5
),
customer_ratings AS (
    -- TODO: Pre-calculate average ratings per customer
    SELECT 
        o.customer_id,
        AVG(r.rating) as avg_rating
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN reviews r ON oi.product_id = r.product_id
    WHERE o.created_at >= '2023-01-01'
    GROUP BY o.customer_id
)
-- TODO: Final optimized query
SELECT 
    c.name,
    co.order_count,
    co.total_spent,
    COALESCE(cr.avg_rating, 0) as avg_rating
FROM customers c
JOIN customer_orders co ON c.id = co.customer_id
LEFT JOIN customer_ratings cr ON c.id = cr.customer_id
ORDER BY co.total_spent DESC
LIMIT 100;

-- Version 2: Using window functions for better performance
-- TODO: Implement window function approach
SELECT DISTINCT
    c.name,
    COUNT(o.id) OVER (PARTITION BY c.id) as order_count,
    SUM(o.order_total) OVER (PARTITION BY c.id) as total_spent,
    AVG(r.rating) OVER (PARTITION BY c.id) as avg_rating
FROM customers c
JOIN orders o ON c.id = o.customer_id
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN reviews r ON oi.product_id = r.product_id AND r.customer_id = c.id
WHERE o.created_at >= '2023-01-01'
    AND o.order_status != 'cancelled'
QUALIFY COUNT(o.id) OVER (PARTITION BY c.id) > 5
ORDER BY total_spent DESC
LIMIT 100;

-- TODO: 4. MATERIALIZED VIEWS FOR COMPLEX AGGREGATIONS
-- Create materialized views for frequently accessed aggregations

-- Customer summary materialized view
-- TODO: Create materialized view for customer metrics
CREATE MATERIALIZED VIEW customer_summary_mv AS
SELECT 
    c.id as customer_id,
    c.name,
    c.email,
    c.customer_tier,
    COUNT(o.id) as total_orders,
    COALESCE(SUM(o.order_total), 0) as total_spent,
    COALESCE(AVG(o.order_total), 0) as avg_order_value,
    MAX(o.created_at) as last_order_date,
    -- TODO: Add more aggregated metrics
    COUNT(CASE WHEN o.created_at >= CURRENT_DATE - INTERVAL '30 days' THEN 1 END) as orders_last_30_days,
    COUNT(CASE WHEN o.created_at >= CURRENT_DATE - INTERVAL '365 days' THEN 1 END) as orders_last_year
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id AND o.order_status != 'cancelled'
GROUP BY c.id, c.name, c.email, c.customer_tier;

-- TODO: Create indexes on materialized view
CREATE INDEX idx_customer_summary_total_spent ON customer_summary_mv(total_spent DESC);
CREATE INDEX idx_customer_summary_customer_tier ON customer_summary_mv(customer_tier);

-- Product performance materialized view
-- TODO: Create product analytics materialized view
CREATE MATERIALIZED VIEW product_analytics_mv AS
SELECT 
    p.id as product_id,
    p.name,
    p.category_id,
    COUNT(oi.id) as times_ordered,
    SUM(oi.quantity) as total_quantity_sold,
    SUM(oi.quantity * oi.unit_price) as total_revenue,
    AVG(r.rating) as avg_rating,
    COUNT(r.id) as review_count,
    -- TODO: Add trend analysis
    COUNT(CASE WHEN o.created_at >= CURRENT_DATE - INTERVAL '30 days' THEN 1 END) as recent_orders
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.id AND o.order_status != 'cancelled'
LEFT JOIN reviews r ON p.id = r.product_id
GROUP BY p.id, p.name, p.category_id;

-- TODO: 5. PARTITIONING STRATEGY
-- Implement table partitioning for large tables

-- Partition orders table by date
-- TODO: Create partitioned orders table
CREATE TABLE orders_partitioned (
    id BIGSERIAL,
    customer_id BIGINT NOT NULL,
    order_total DECIMAL(10,2),
    order_status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY RANGE (created_at);

-- TODO: Create monthly partitions
CREATE TABLE orders_2023_01 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2023-01-01') TO ('2023-02-01');

CREATE TABLE orders_2023_02 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2023-02-01') TO ('2023-03-01');

-- TODO: Create function to automatically create partitions
CREATE OR REPLACE FUNCTION create_monthly_partition(table_name text, start_date date)
RETURNS void AS $$
DECLARE
    partition_name text;
    end_date date;
BEGIN
    -- TODO: Implement automatic partition creation
    partition_name := table_name || '_' || to_char(start_date, 'YYYY_MM');
    end_date := start_date + interval '1 month';
    
    EXECUTE format('CREATE TABLE %I PARTITION OF %I FOR VALUES FROM (%L) TO (%L)',
                   partition_name, table_name, start_date, end_date);
    
    -- Create indexes on partition
    EXECUTE format('CREATE INDEX %I ON %I (customer_id, created_at)',
                   'idx_' || partition_name || '_customer_date', partition_name);
END;
$$ LANGUAGE plpgsql;

-- TODO: 6. QUERY CACHING STRATEGY
-- Implement caching for frequently accessed data

-- Function to get customer summary with caching
-- TODO: Create cached customer summary function
CREATE OR REPLACE FUNCTION get_customer_summary_cached(p_customer_id BIGINT)
RETURNS TABLE(
    customer_name VARCHAR(255),
    total_orders BIGINT,
    total_spent NUMERIC,
    avg_rating NUMERIC
) AS $$
DECLARE
    cache_key TEXT;
    cache_result RECORD;
    cache_ttl INTERVAL := '1 hour';
BEGIN
    -- TODO: Implement Redis-like caching logic
    cache_key := 'customer_summary_' || p_customer_id;
    
    -- Check if cached result exists and is fresh
    -- If not, calculate and cache result
    
    RETURN QUERY
    SELECT 
        cs.name,
        cs.total_orders,
        cs.total_spent,
        COALESCE(AVG(r.rating), 0)
    FROM customer_summary_mv cs
    LEFT JOIN orders o ON cs.customer_id = o.customer_id
    LEFT JOIN order_items oi ON o.id = oi.order_id
    LEFT JOIN reviews r ON oi.product_id = r.product_id
    WHERE cs.customer_id = p_customer_id
    GROUP BY cs.name, cs.total_orders, cs.total_spent;
END;
$$ LANGUAGE plpgsql;

-- TODO: 7. DATA ARCHIVING STRATEGY
-- Implement data archiving for old records

-- Archive old orders to separate table
-- TODO: Create archive table structure
CREATE TABLE orders_archive (
    LIKE orders INCLUDING ALL
);

-- TODO: Create archiving function
CREATE OR REPLACE FUNCTION archive_old_orders(archive_before_date DATE)
RETURNS INTEGER AS $$
DECLARE
    archived_count INTEGER;
BEGIN
    -- TODO: Move old orders to archive table
    WITH moved_orders AS (
        DELETE FROM orders 
        WHERE created_at < archive_before_date
        RETURNING *
    )
    INSERT INTO orders_archive SELECT * FROM moved_orders;
    
    GET DIAGNOSTICS archived_count = ROW_COUNT;
    RETURN archived_count;
END;
$$ LANGUAGE plpgsql;

-- TODO: 8. MONITORING AND MAINTENANCE
-- Create monitoring queries and maintenance procedures

-- Query to monitor slow queries
-- TODO: Create slow query monitoring
CREATE OR REPLACE VIEW slow_queries AS
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    max_time,
    stddev_time
FROM pg_stat_statements
WHERE mean_time > 100  -- queries slower than 100ms
ORDER BY mean_time DESC;

-- TODO: Create maintenance procedure
CREATE OR REPLACE FUNCTION daily_maintenance()
RETURNS void AS $$
BEGIN
    -- Refresh materialized views
    REFRESH MATERIALIZED VIEW CONCURRENTLY customer_summary_mv;
    REFRESH MATERIALIZED VIEW CONCURRENTLY product_analytics_mv;
    
    -- Update table statistics
    ANALYZE customers;
    ANALYZE orders;
    ANALYZE order_items;
    ANALYZE products;
    ANALYZE reviews;
    
    -- TODO: Add more maintenance tasks
    -- Clean up old statistics
    -- Vacuum analyze large tables
    -- Check for unused indexes
END;
$$ LANGUAGE plpgsql;

-- TODO: 9. PERFORMANCE TESTING QUERIES
-- Create queries to test optimization effectiveness

-- Test query performance before and after optimization
-- TODO: Implement performance comparison
DO $$
DECLARE
    start_time TIMESTAMP;
    end_time TIMESTAMP;
    execution_time INTERVAL;
BEGIN
    start_time := clock_timestamp();
    
    -- Execute optimized query
    PERFORM * FROM (
        SELECT 
            c.name,
            cs.total_orders,
            cs.total_spent,
            COALESCE(AVG(r.rating), 0) as avg_rating
        FROM customer_summary_mv cs
        JOIN customers c ON cs.customer_id = c.id
        LEFT JOIN orders o ON c.id = o.customer_id
        LEFT JOIN order_items oi ON o.id = oi.order_id
        LEFT JOIN reviews r ON oi.product_id = r.product_id
        WHERE cs.total_orders > 5
        GROUP BY c.name, cs.total_orders, cs.total_spent
        ORDER BY cs.total_spent DESC
        LIMIT 100
    ) perf_test;
    
    end_time := clock_timestamp();
    execution_time := end_time - start_time;
    
    RAISE NOTICE 'Query executed in: %', execution_time;
END $$;

-- TODO: 10. MONITORING DASHBOARD QUERIES
-- Create queries for performance dashboard

-- Real-time performance metrics
-- TODO: Create dashboard metrics view
CREATE OR REPLACE VIEW performance_dashboard AS
SELECT 
    'Database Size' as metric,
    pg_size_pretty(pg_database_size(current_database())) as value
UNION ALL
SELECT 
    'Total Customers',
    COUNT(*)::text
FROM customers
UNION ALL
SELECT 
    'Total Orders Today',
    COUNT(*)::text
FROM orders
WHERE created_at >= CURRENT_DATE
UNION ALL
SELECT 
    'Average Order Value',
    ROUND(AVG(order_total), 2)::text
FROM orders
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days';

/*
Expected Implementation Areas for GitHub Copilot:

1. Index Strategy:
   - Composite indexes for multi-column queries
   - Partial indexes for filtered queries
   - Covering indexes to avoid table lookups
   - Index maintenance and monitoring

2. Query Optimization:
   - CTE usage for complex queries
   - Window functions for analytics
   - Subquery optimization
   - JOIN order optimization

3. Materialized Views:
   - Pre-aggregated data for performance
   - Refresh strategies
   - Dependency management
   - Storage optimization

4. Partitioning:
   - Date-based partitioning
   - Automatic partition management
   - Constraint exclusion
   - Cross-partition queries

5. Caching Strategy:
   - Application-level caching
   - Database query caching
   - Materialized view caching
   - Cache invalidation

6. Monitoring:
   - Performance metrics collection
   - Slow query identification
   - Resource usage tracking
   - Automated alerting

Example Usage:
psql -d ecommerce -f 08_database_optimization.sql

This should demonstrate Copilot's ability to:
- Identify database performance bottlenecks
- Create optimal indexing strategies
- Rewrite queries for better performance
- Implement caching and archiving strategies
- Set up monitoring and maintenance procedures
*/
