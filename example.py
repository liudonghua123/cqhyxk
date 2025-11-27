"""
Example usage of the cqhyxk SDK
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Replace 'SAMPLE_USER_ID' with an actual user ID to test this function
sample_user_id = os.getenv('SAMPLE_USER_ID', 'SAMPLE_USER_ID')

from cqhyxk import CqhyxkClient
from cqhyxk.models import IdentityPageRequest, SubscriptionRequest, MemberTagPageRequest

def main():
    """
    Example demonstrating how to use the cqhyxk SDK
    """
    # Initialize the client - credentials will be loaded from environment variables
    # Make sure to set CQHYXK_BASEURL, CQHYXK_APP_KEY, and CQHYXK_APP_SECRET in your .env file
    client = CqhyxkClient()
    
    print("cqhyxk SDK Example")
    print("=" * 30)
    
    # Example 1: Get identity list (first 10 records)
    print("\n1. Getting identity list...")
    try:
        request = IdentityPageRequest(current=0, size=10, sourceUserId=sample_user_id)
        response = client.get_identity_list(request)
        print(f"Retrieved {len(response.data.content) if response.data and response.data.content else 0} identities")
        print(f"Content: {response.data.content if response.data and response.data.content else 'N/A'}")
    except Exception as e:
        print(f"Error getting identity list: {str(e).encode('utf-8', errors='ignore').decode('utf-8')}")
    
    # Example 2: Get organization list
    print("\n2. Getting organization list...")
    try:
        response = client.get_org_list()
        print(f"Retrieved {len(response.data.content) if response.data and response.data.content else 0} organizations")
        print(f"Content: {response.data.content if response.data and response.data.content else 'N/A'}")
    except Exception as e:
        print(f"Error getting organization list: {str(e).encode('utf-8', errors='ignore').decode('utf-8')}")
    
    # Example 3: Get tag list
    print("\n3. Getting tag list...")
    try:
        response = client.get_tag_list()
        print(f"Retrieved {len(response.data.content) if response.data and response.data.content else 0} tags")
        print(f"Content: {response.data.content if response.data and response.data.content else 'N/A'}")
    except Exception as e:
        print(f"Error getting tag list: {str(e).encode('utf-8', errors='ignore').decode('utf-8')}")
    
    # Example 4: Get face photos (using a sample ID)
    print("\n4. Getting face photos...")
    try:
        response = client.get_face_photos(sample_user_id)
        print(f"Retrieved {len(response.data.content) if response.data and response.data.content else 0} face photos for user {sample_user_id}")
        print(f"Content: {response.data.content if response.data and response.data.content else 'N/A'}")
    except Exception as e:
        print(f"Error getting face photos: {str(e).encode('utf-8', errors='ignore').decode('utf-8')}")
    
    # Example 5: Subscribe to an event (use with caution in production)
    print("\n5. Subscribing to an event (example)...")
    try:
        # Replace with your actual callback URL in a real scenario
        callback_url = os.getenv('CALLBACK_URL', 'https://your-callback-url.com/webhook')
        subscription_request = SubscriptionRequest(
            event_type=1,  # Personnel event
            callback_url=callback_url
        )
        response = client.add_subscription(subscription_request)
        print(f"Event subscription response: {response.data.result if response.data and response.data.result else 'N/A'}")
    except Exception as e:
        print(f"Error subscribing to event: {str(e).encode('utf-8', errors='ignore').decode('utf-8')}")
    
    # Example 6: Get member tags page
    print("\n6. Getting member tags page...")
    try:
        request = MemberTagPageRequest(current=0, size=10, sourceUserId=sample_user_id)
        print(f"Requesting member tags with: {request.dict(exclude_none=True)}")
        response = client.get_member_tags_page(request)
        print(f"Retrieved {len(response.data.content) if response.data and response.data.content else 0} member tag relationships")
        print(f"Content: {response.data.content if response.data and response.data.content else 'N/A'}")
    except Exception as e:
        print(f"Error getting member tags page: {str(e).encode('utf-8', errors='ignore').decode('utf-8')}")
    
    print("\n" + "=" * 30)
    print("Example completed!")

if __name__ == "__main__":
    main()