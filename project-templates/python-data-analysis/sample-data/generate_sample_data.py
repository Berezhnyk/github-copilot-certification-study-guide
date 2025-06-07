# Sample E-commerce Dataset Generator
# Generated data for GitHub Copilot certification practice exercises

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker

# Initialize Faker for realistic data generation
fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

def generate_customers(n=1000):
    """Generate sample customer data"""
    customers = []
    
    for i in range(n):
        customer = {
            'customer_id': f'CUST_{i+1:06d}',
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'registration_date': fake.date_between(start_date='-2y', end_date='today'),
            'age': random.randint(18, 80),
            'gender': random.choice(['M', 'F', 'Other']),
            'location': fake.city(),
            'country': fake.country(),
            'customer_segment': random.choice(['Bronze', 'Silver', 'Gold', 'Platinum']),
            'preferred_category': random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'])
        }
        customers.append(customer)
    
    return pd.DataFrame(customers)

def generate_products(n=500):
    """Generate sample product data"""
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
    products = []
    
    for i in range(n):
        category = random.choice(categories)
        product = {
            'product_id': f'PROD_{i+1:06d}',
            'name': fake.catch_phrase(),
            'category': category,
            'brand': fake.company(),
            'price': round(random.uniform(9.99, 999.99), 2),
            'cost': round(random.uniform(5.0, 500.0), 2),
            'description': fake.text(max_nb_chars=200),
            'rating': round(random.uniform(1.0, 5.0), 1),
            'review_count': random.randint(0, 1000),
            'in_stock': random.choice([True, False]),
            'stock_quantity': random.randint(0, 100) if random.random() > 0.1 else 0,
            'launch_date': fake.date_between(start_date='-3y', end_date='today')
        }
        products.append(product)
    
    return pd.DataFrame(products)

def generate_orders(customers_df, products_df, n=5000):
    """Generate sample order data"""
    orders = []
    
    for i in range(n):
        customer_id = random.choice(customers_df['customer_id'].tolist())
        order_date = fake.date_between(start_date='-1y', end_date='today')
        
        order = {
            'order_id': f'ORD_{i+1:08d}',
            'customer_id': customer_id,
            'order_date': order_date,
            'order_status': random.choice(['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']),
            'payment_method': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer']),
            'shipping_address': fake.address(),
            'total_amount': 0  # Will be calculated based on order items
        }
        orders.append(order)
    
    return pd.DataFrame(orders)

def generate_order_items(orders_df, products_df, avg_items_per_order=2.5):
    """Generate sample order items data"""
    order_items = []
    item_id = 1
    
    for _, order in orders_df.iterrows():
        num_items = max(1, int(np.random.poisson(avg_items_per_order)))
        selected_products = products_df.sample(n=min(num_items, len(products_df)))
        
        order_total = 0
        
        for _, product in selected_products.iterrows():
            quantity = random.randint(1, 5)
            unit_price = product['price']
            line_total = quantity * unit_price
            order_total += line_total
            
            item = {
                'item_id': f'ITEM_{item_id:08d}',
                'order_id': order['order_id'],
                'product_id': product['product_id'],
                'quantity': quantity,
                'unit_price': unit_price,
                'line_total': line_total,
                'discount_amount': round(random.uniform(0, line_total * 0.2), 2)
            }
            order_items.append(item)
            item_id += 1
        
        # Update order total
        orders_df.loc[orders_df['order_id'] == order['order_id'], 'total_amount'] = float(round(order_total, 2))
    
    return pd.DataFrame(order_items)

def generate_website_analytics(n=10000):
    """Generate sample website analytics data"""
    analytics = []
    
    for i in range(n):
        session_date = fake.date_time_between(start_date='-6m', end_date='now')
        
        record = {
            'session_id': f'SESS_{i+1:08d}',
            'user_id': f'USER_{random.randint(1, 2000):06d}',
            'session_date': session_date,
            'page_views': random.randint(1, 20),
            'session_duration_minutes': random.randint(1, 120),
            'bounce_rate': random.choice([True, False]),
            'device_type': random.choice(['Desktop', 'Mobile', 'Tablet']),
            'browser': random.choice(['Chrome', 'Firefox', 'Safari', 'Edge']),
            'traffic_source': random.choice(['Direct', 'Google', 'Facebook', 'Email', 'Referral']),
            'conversion': random.choice([True, False]),
            'revenue': round(random.uniform(0, 500), 2) if random.random() > 0.7 else 0
        }
        analytics.append(record)
    
    return pd.DataFrame(analytics)

def generate_customer_support_tickets(customers_df, n=1500):
    """Generate sample customer support data"""
    tickets = []
    
    for i in range(n):
        customer_id = random.choice(customers_df['customer_id'].tolist())
        created_date = fake.date_time_between(start_date='-1y', end_date='now')
        
        ticket = {
            'ticket_id': f'TICK_{i+1:06d}',
            'customer_id': customer_id,
            'subject': fake.sentence(nb_words=6),
            'category': random.choice(['Billing', 'Technical', 'Shipping', 'Product', 'Account']),
            'priority': random.choice(['Low', 'Medium', 'High', 'Critical']),
            'status': random.choice(['Open', 'In Progress', 'Resolved', 'Closed']),
            'created_date': created_date,
            'resolved_date': created_date + timedelta(days=random.randint(0, 30)) if random.random() > 0.3 else None,
            'satisfaction_score': random.randint(1, 5) if random.random() > 0.4 else None,
            'description': fake.text(max_nb_chars=500)
        }
        tickets.append(ticket)
    
    return pd.DataFrame(tickets)

def main():
    """Main function to generate all datasets"""
    print("Generating sample datasets...")
    
    # Generate data
    customers = generate_customers(1000)
    products = generate_products(500)
    orders = generate_orders(customers, products, 5000)
    order_items = generate_order_items(orders, products)
    analytics = generate_website_analytics(10000)
    support_tickets = generate_customer_support_tickets(customers, 1500)
    
    # Save to CSV files
    customers.to_csv('customers.csv', index=False)
    products.to_csv('products.csv', index=False)
    orders.to_csv('orders.csv', index=False)
    order_items.to_csv('order_items.csv', index=False)
    analytics.to_csv('website_analytics.csv', index=False)
    support_tickets.to_csv('support_tickets.csv', index=False)
    
    print("Sample datasets generated successfully!")
    print(f"- Customers: {len(customers)} records")
    print(f"- Products: {len(products)} records")
    print(f"- Orders: {len(orders)} records")
    print(f"- Order Items: {len(order_items)} records")
    print(f"- Analytics: {len(analytics)} records")
    print(f"- Support Tickets: {len(support_tickets)} records")
    
    print("\nDatasets saved as CSV files:")
    print("- customers.csv")
    print("- products.csv")
    print("- orders.csv")
    print("- order_items.csv")
    print("- website_analytics.csv")
    print("- support_tickets.csv")

if __name__ == "__main__":
    main()
