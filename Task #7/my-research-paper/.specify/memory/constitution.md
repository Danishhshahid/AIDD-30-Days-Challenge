<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- Modified principles:
  - Initialized all principles for a research-focused project.
- Added sections:
  - Core Principles
  - Artifact and Workflow Standards
  - Review Process
  - Governance
- Removed sections:
  - None
- Templates requiring updates:
  - ⚠ pending: .specify/templates/plan-template.md
  - ⚠ pending: .specify/templates/spec-template.md
  - ⚠ pending: .specify/templates/tasks-template.md
- Follow-up TODOs:
  - TODO(Consistency): Review and align all templates in `.specify/templates/` with the principles defined in this constitution.
-->
# My Research Paper Constitution

## Core Principles

### I. Reproducibility is Paramount
All code, data, and analysis steps MUST be fully documented and automated to allow for complete and independent reproduction of all results. All dependencies must be explicitly declared.

### II. Clarity and Rigor
The manuscript and all supporting materials MUST be written with clarity, precision, and scientific rigor. Methodologies must be transparently reported, and claims must be directly supported by evidence.

### III. Version Control is Mandatory
All project artifacts, including the manuscript, code, datasets, and figures, MUST be tracked using Git. The repository history should serve as a log of the research process.

### IV. Data and Code Integrity
Raw data is immutable. All data transformation, cleaning, and analysis MUST be performed via auditable scripts. Manual editing of raw or processed data is strictly forbidden.

### V. Open Science by Default
All research outputs (manuscript, code, data) SHOULD be made publicly available upon publication, following FAIR (Findable, Accessible, Interoperable, and Reusable) principles, unless restricted by privacy or ethical constraints.

### VI. Incremental and Atomic Commits
Commits should be small, focused, and represent a single logical change. Commit messages MUST be clear and descriptive, explaining the 'why' behind the change.

## Artifact and Workflow Standards

All research and analysis must be conducted in a structured and organized manner. The project will adhere to a standardized directory structure for data, code, and manuscripts. Notebooks (e.g., Jupyter) may be used for exploration but final analyses MUST be captured in scripts.

## Review Process

All changes to the manuscript, core analysis scripts, or figures must be submitted via pull requests. A review from at least one other project member is required before merging. The review should check for adherence to this constitution, correctness, and clarity.

## Governance

This constitution is the authoritative guide for the project. All contributions will be measured against its principles. Amendments require a pull request and approval from all active project members.

**Version**: 1.0.0 | **Ratified**: 2025-11-29 | **Last Amended**: 2025-11-29