# cqhyxk SDK

Python SDK for the 身份中台V2.0 OpenAPI (Identity Management Platform V2.0 OpenAPI)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/pypi/pyversions/cqhyxk)](https://pypi.org/project/cqhyxk/)

## Overview

This SDK provides a Python interface to interact with the Identity Management Platform V2.0 API, allowing you to manage personnel, organizations, tags, and event subscriptions programmatically.

The SDK provides:

- **Type Safety**: All requests and responses are validated with Pydantic models
- **Environment Configuration**: Load credentials from environment variables
- **Complete API Coverage**: All endpoints from the OpenAPI specification
- **Error Handling**: Comprehensive error handling with custom exceptions
- **Documentation**: Detailed documentation for all methods

## Installation

Install the package using pip:

```bash
pip install cqhyxk
```

Or using uv:

```bash
uv pip install cqhyxk
```

## Quick Start

1. **Set up environment variables** by creating a `.env` file (see `.env.example`):

    ```env
    CQHYXK_BASEURL=https://your-domain/backend/school-platform/openapi
    CQHYXK_APP_KEY=your_app_key_here
    CQHYXK_APP_SECRET=your_app_secret_here
    ```

2. **Initialize the client and make API calls**:

    ```python
    from cqhyxk import CqhyxkClient
    from cqhyxk.models import IdentityPageRequest

    # Initialize the client (credentials loaded from environment variables)
    client = CqhyxkClient()

    # Example: Get first 10 identities
    request = IdentityPageRequest(current=0, size=10)
    response = client.get_identity_list(request)
    
    print(f"Retrieved {len(response.data.content)} identities")
    for identity in response.data.content:
        print(f"- {identity.name} ({identity.sourceUserId})")
    ```

## Configuration

The SDK supports configuration via environment variables:

- `CQHYXK_BASEURL`: The base URL for the API (default: `https://your-domain/backend/school-platform/openapi`)
- `CQHYXK_APP_KEY`: Your application key for API authentication
- `CQHYXK_APP_SECRET`: Your application secret for API authentication

You can also pass these values directly to the constructor:

```python
client = CqhyxkClient(
    app_key="your_app_key",
    app_secret="your_app_secret", 
    base_url="https://your-api-domain.com"
)
```

## Available Methods

### Personnel Methods

- `get_identity_list(request)`: Get paginated list of personnel identity information
- `get_face_photos(source_user_id)`: Get face photos by student ID

### Organization Methods

- `get_org_list(physical, internal, org_id)`: Get list of organizations

### Tag Methods

- `get_tag_list(tag_id)`: Get list of tags
- `get_member_tags_page(request)`: Get paginated list of personnel tag relationships

### Event Subscription Methods

- `add_subscription(request)`: Subscribe to events
- `cancel_subscription(event_type)`: Cancel event subscription

For detailed documentation of each method, including parameters and response formats, check the docstrings in the source code.

## Examples

Run the example script to see the SDK in action:

```bash
python example.py
```

Make sure your environment variables are properly configured before running the example.

## Development

To install the package in development mode:

```bash
git clone https://github.com/liudonghua123/cqhyxk.git
cd cqhyxk
pip install -e .
```

Or with uv:

```bash
uv pip install -e .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues, please file a bug report in the GitHub repository or contact the maintainers.

## API Documentation

For detailed API documentation, refer to the [original OpenAPI specification](docs/cqhyxk_OpenAPI_v2.4.md).