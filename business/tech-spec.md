 # Tech-Spec.md

## Stack
- Language: Python 3.9 for its extensive libraries and community support for AI and data processing.
- Framework: Django 3.2 for building the web application with a focus on reusability and "pluggability" of components.
- Runtime: Gunicorn for managing the WSGI HTTP server.

## Hosting
- Free-tier-first: Heroku with a PostgreSQL add-on for the initial deployment.
- Specific platforms: AWS Elastic Beanstalk for scalability and integration with other AWS services.

## Data Model
- Tables/Collections:
  - `AI_USAGE_VERIFICATION`: Contains the verification records with fields like `verification_id`, `product_id`, `ai_provider_id`, `verification_status`, `verification_date`, and `verification_report`.
  - `AI_PROVIDERS`: Stores information about AI providers with fields like `provider_id`, `provider_name`, and `provider_contact_info`.
  - `PRODUCTS`: Contains product information with fields like `product_id`, `product_name`, and `product_url`.

## API Surface
- `/api/v1/verify`: POST endpoint to initiate the AI usage verification process.
- `/api/v1/verification/{verification_id}`: GET endpoint to retrieve the details of a specific verification request.
- `/api/v1/ai_providers`: GET endpoint to retrieve a list of AI providers.
- `/api/v1/products`: GET endpoint to retrieve a list of products.
- `/api/v1/verify_status`: GET endpoint to check the status of a verification request.
- `/api/v1/verification_report`: GET endpoint to retrieve the verification report of a specific verification request.

## Security Model
- Auth: JWT-based authentication for API access.
- Secrets: Environment variables for storing sensitive information like API keys.
- IAM: Roles and permissions for controlling access to resources within the application.

## Observability
- Logs: Logging using Django's built-in logging system, with integration with a third-party logging service like Sentry for error tracking and monitoring.
- Metrics: Integration with a monitoring service like Prometheus for tracking key performance indicators.
- Traces: Integration with a distributed tracing system like Jaeger for understanding the flow of requests through the application.

## Build/CI
- Continuous Integration: GitHub Actions for automated testing and deployment.
- Testing: Unit tests using Python's unittest framework and integration tests using Django's test client.
- Code quality: Static analysis using tools like PyLint and Black for maintaining code quality.