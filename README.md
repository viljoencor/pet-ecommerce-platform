# pet-ecommerce-platform
pet-ecommerce-platform

## **Project Structure**
```plaintext
ecommerce-platform/
├── .github/
│   └── workflows/          # CI/CD GitHub Actions
├── cdk/                    # AWS Infrastructure (CDK Python)
│   └── app.py, stacks/
├── backend/
│   ├── dotnet/             # C# .NET Core APIs (Order, Product, etc.)
│   │   └── Ecommerce.Api/
│   └── python/             # Python Lambdas (PayFast IPN, glue logic)
│       └── payfast_ipn/
├── frontend/
│   └── react/              # React.js (Amplify frontend)
├── openapi/
│   └── order-api.yaml      # OpenAPI docs for C# Order API
├── README.md
└── .gitignore
```
