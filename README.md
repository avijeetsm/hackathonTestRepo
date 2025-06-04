# Rule-Based Financial Transaction Processor

A modular Python system for processing financial transactions using customizable rules. Includes deep transitive dependencies and advanced test coverage.

## Modules
- `transaction.py`, `account.py`, `rule.py`, `rule_engine.py`, `logger.py`, `notification.py`, `audit.py`, `utils.py`
- 6+ test files for deep, realistic scenarios

## Running Tests
Install requirements and run:

```sh
pip install -r requirements.txt
pytest
```

No external DB or mocking—everything uses in-memory data.
