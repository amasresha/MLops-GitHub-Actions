# MLops-GitHub-Actions

[![MLops CI/CD Pipeline](https://github.com/amasresha/MLops-GitHub-Actions/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/amasresha/MLops-GitHub-Actions/actions/workflows/ci-cd.yml)

```markdown
A project demonstrating an MLOps pipeline using GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD).
```
## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/amasresha/MLops-GitHub-Actions.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest tests/
   ```

4. Train the model:
   ```bash
   python src/train.py
   ```

5. Make predictions:
   ```bash
   python src/predict.py
   ```

### GitHub Actions CI/CD Pipeline
The CI/CD pipeline is defined in .github/workflows/ci-cd.yml. It automates testing and ensures code quality on every push or pull request to the main branch.


### Workflow Steps
1. **Checkout Code**: Fetches the latest code from the repository.
2. **Set Up Python**: Configures the Python environment (e.g., Python 3.12).
3. **Install Dependencies**: Installs the required Python packages from `requirements.txt`.
4. **Run Tests**: Executes unit tests using `pytest`.

### How to Trigger the Pipeline
- Push changes to the `main` branch.
- Open a pull request targeting the `main` branch.

## License

MIT License. See [LICENSE](LICENSE) for details.
