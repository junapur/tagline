[windows]
set shell := ["powershell.exe", "-NoLogo", "-Command"]

[private]
default:
    @just --list --unsorted

# Run the CLI
run *args:
    cargo run -- {{args}}

# Format code
fmt:
    cargo fmt

# Lint code
lint:
    cargo clippy --all-targets -- -D warnings

# Run tests
test:
    cargo test

# Check code
check:
    cargo fmt --check
    cargo clippy --all-targets -- -D warnings
    cargo test
