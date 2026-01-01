# Contributing to Quantum Simulation Scheduling

Thank you for considering contributing to this project! 

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, Qiskit version)
- Error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:
- Clear description of the enhancement
- Use cases and benefits
- Possible implementation approach

### Pull Requests

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Add** tests for new functionality
5. **Ensure** all tests pass (`pytest tests/`)
6. **Update** documentation if needed
7. **Commit** with clear messages (`git commit -m 'Add amazing feature'`)
8. **Push** to your fork (`git push origin feature/amazing-feature`)
9. **Open** a Pull Request

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Include type hints where appropriate
- Keep functions focused and modular

### Testing

- Write tests for new features
- Ensure existing tests pass
- Run: `pytest tests/ -v`

### Documentation

- Update README.md if adding new features
- Add inline comments for complex logic
- Update CHANGELOG.md

### Commit Messages

Use clear, descriptive commit messages:
```
Add circuit cutting optimization

- Implement new cutting algorithm
- Improve overhead calculation
- Add tests for edge cases
```

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Quantum_Simulation_Scheduling_ver1.git
cd Quantum_Simulation_Scheduling

# Create environment
conda create -n squan python=3.10
conda activate squan

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/
```

## Code Review Process

- All PRs require review before merging
- Address review comments promptly
- Keep PRs focused on single features/fixes

## Questions?

Open an issue or contact the maintainers.

Thank you for contributing! 🙏
