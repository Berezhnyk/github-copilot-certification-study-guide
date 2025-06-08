# Exercise 2: Design Pattern Implementation
# Task: Implement the Observer pattern for a notification system

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Set
from enum import Enum
from datetime import datetime

class EventType(Enum):
    """Enumeration of supported event types."""
    USER_CREATED = "user_created"
    USER_UPDATED = "user_updated"
    USER_DELETED = "user_deleted"
    ORDER_PLACED = "order_placed"
    ORDER_CANCELLED = "order_cancelled"
    PAYMENT_PROCESSED = "payment_processed"

class Observer(ABC):
    """Observer interface that all subscribers must implement."""
    
    @abstractmethod
    def update(self, event_type: EventType, data: Dict[str, Any]) -> None:
        """
        Called when an event occurs.
        
        Args:
            event_type: Type of event that occurred
            data: Event-specific data
        """
        # TODO: Let Copilot define the observer interface
        pass

class NotificationPublisher:
    """
    Subject/Publisher that manages observers and sends notifications.
    Supports multiple event types and selective subscription.
    """
    
    def __init__(self):
        """Initialize observer management system."""
        # TODO: Initialize observer management system
        # Should support multiple event types
        pass
    
    def subscribe(self, observer: Observer, event_types: List[EventType]) -> None:
        """
        Subscribe observer to specific event types.
        
        Args:
            observer: Observer to subscribe
            event_types: List of event types to subscribe to
        """
        # TODO: Let Copilot implement subscription logic
        pass
    
    def unsubscribe(self, observer: Observer, event_types: List[EventType] = None) -> None:
        """
        Unsubscribe observer from events.
        
        Args:
            observer: Observer to unsubscribe
            event_types: Specific event types to unsubscribe from, or None for all
        """
        # TODO: Let Copilot implement unsubscription logic
        pass
    
    def notify(self, event_type: EventType, data: Dict[str, Any]) -> None:
        """
        Notify all subscribers of an event.
        
        Args:
            event_type: Type of event
            data: Event data to send to observers
        """
        # TODO: Let Copilot implement notification logic
        pass
    
    def get_subscriber_count(self, event_type: EventType) -> int:
        """
        Get number of subscribers for an event type.
        
        Args:
            event_type: Event type to check
        
        Returns:
            int: Number of subscribers
        """
        # TODO: Let Copilot implement subscriber counting
        pass

# Example Observer implementations
class EmailNotificationObserver(Observer):
    """Observer that sends email notifications."""
    
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.notifications_sent = 0
    
    def update(self, event_type: EventType, data: Dict[str, Any]) -> None:
        """Send email notification for the event."""
        # TODO: Let Copilot implement email notification logic
        pass

class SMSNotificationObserver(Observer):
    """Observer that sends SMS notifications."""
    
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.notifications_sent = 0
    
    def update(self, event_type: EventType, data: Dict[str, Any]) -> None:
        """Send SMS notification for the event."""
        # TODO: Let Copilot implement SMS notification logic
        pass

class AuditLogObserver(Observer):
    """Observer that logs events for audit purposes."""
    
    def __init__(self):
        self.logged_events = []
    
    def update(self, event_type: EventType, data: Dict[str, Any]) -> None:
        """Log event for audit trail."""
        # TODO: Let Copilot implement audit logging logic
        pass

if __name__ == "__main__":
    # Test the observer pattern implementation
    publisher = NotificationPublisher()
    
    # Create observers
    email_observer = EmailNotificationObserver("admin@example.com")
    sms_observer = SMSNotificationObserver("+1234567890")
    audit_observer = AuditLogObserver()
    
    # Subscribe to events
    publisher.subscribe(email_observer, [EventType.USER_CREATED, EventType.ORDER_PLACED])
    publisher.subscribe(sms_observer, [EventType.ORDER_PLACED, EventType.PAYMENT_PROCESSED])
    publisher.subscribe(audit_observer, list(EventType))  # Subscribe to all events
    
    # Simulate events
    print("Simulating events...")
    
    # User created event
    publisher.notify(EventType.USER_CREATED, {
        "user_id": 123,
        "username": "johndoe",
        "email": "john@example.com",
        "timestamp": datetime.now().isoformat()
    })
    
    # Order placed event
    publisher.notify(EventType.ORDER_PLACED, {
        "order_id": 456,
        "user_id": 123,
        "total": 99.99,
        "items": ["Product A", "Product B"],
        "timestamp": datetime.now().isoformat()
    })
    
    # Check notification counts
    print(f"Email notifications sent: {email_observer.notifications_sent}")
    print(f"SMS notifications sent: {sms_observer.notifications_sent}")
    print(f"Events logged: {len(audit_observer.logged_events)}")
    
    # Check subscriber counts
    print(f"USER_CREATED subscribers: {publisher.get_subscriber_count(EventType.USER_CREATED)}")
    print(f"ORDER_PLACED subscribers: {publisher.get_subscriber_count(EventType.ORDER_PLACED)}")
