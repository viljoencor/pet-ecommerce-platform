# 📦 pet-ecommerce-platform (by @viljoencor)

This monorepo contains the full source code and infrastructure as code (IaC) for the Pet E-Commerce Platform.

## 🔧 Structure

```
petecommerce-platform/
├── .github/workflows/       # GitHub Actions CI/CD
├── cdk/                     # AWS CDK infra (Python)
├── backend/
│   ├── dotnet/              # C# .NET Core APIs
│   └── python/              # Python Lambdas
├── frontend/react/          # React frontend (AWS Amplify)
├── openapi/                 # Swagger/OpenAPI definitions
├── README.md
└── .gitignore
```

---

## ✅ Stack Summary
- **Infrastructure:** AWS CDK (Python)
- **Backend:** C# .NET Core (REST APIs), Python (Lambdas)
- **Frontend:** React.js (Hosted via AWS Amplify)
- **Auth:** AWS Cognito
- **Database:** Aurora PostgreSQL, DynamoDB
- **CI/CD:** GitHub Actions

---

## 🚀 Quick Start

```bash
git clone git@github.com:viljoencor/pet-ecommerce-platform.git
cd pet-ecommerce-platform
```

---

## 🗂️ .gitignore
```
# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/

# .NET
bin/
obj/
*.user
*.suo
*.pdb
*.cache

# Node / React
node_modules/
build/
dist/
.env
.DS_Store

# CDK
cdk.out/
```

---

## 🤖 GitHub Actions Workflows

### 📄 `.github/workflows/deploy-cdk.yml`
```yaml
name: Deploy CDK Infrastructure
on:
  push:
    paths:
      - 'cdk/**'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.11
      - run: pip install -r cdk/requirements.txt
      - run: cdk synth
      - run: cdk deploy --require-approval never
```

### 📄 `.github/workflows/build-dotnet.yml`
```yaml
name: Build and Deploy .NET Core API
on:
  push:
    paths:
      - 'backend/dotnet/**'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-dotnet@v3
        with:
          dotnet-version: '8.x'
      - run: dotnet restore ./backend/dotnet/Ecommerce.Api
      - run: dotnet build --configuration Release ./backend/dotnet/Ecommerce.Api
```

### 📄 `.github/workflows/deploy-python-lambda.yml`
```yaml
name: Deploy Python Lambda
on:
  push:
    paths:
      - 'backend/python/**'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: aws-actions/configure-aws-credentials@v3
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: af-south-1
      - run: |
          zip -r lambda.zip backend/python/payfast_ipn
          aws lambda update-function-code \
            --function-name PayFastIPNLambda \
            --zip-file fileb://lambda.zip
```
