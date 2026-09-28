# Tree of Thoughts (ToT) Beam Search Reasoner Skill

High-efficiency, zero-dependency Python implementation of **Tree of Thoughts (ToT)** for deliberate problem solving via lookahead search.

## Features
- **Breadth-First Beam Search Exploration**: Prunes low-confidence branches while maintaining multiple promising hypothesis paths.
- **Evaluation Heuristics**: Dynamically guides agent decision making via state-value estimators.
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    Root["Initial Thought State"] --> B1["Candidate 1"]
    Root --> B2["Candidate 2"]
    Root --> B3["Candidate 3 (Pruned)"]
    B1 --> B11["Thought 1.1"]
    B1 --> B12["Thought 1.2"]
    B2 --> B21["Thought 2.1 (Optimal)"]
    B2 --> B22["Thought 2.2"]
```
