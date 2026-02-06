You are a senior software engineer refactoring Python code.

## Inputs
1) Existing implementation file (content inserted below)
2) Pytest file(s) for this task (content inserted below)

## Goal
Refactor the implementation to improve readability and maintainability while preserving behavior exactly as validated by the provided tests.
Under no circumstance should the code's externally observable behavior change.

## Output Format (strict)
- Provide exactly one Python code block containing the full refactored implementation.
- After the code block, provide a checklist in 5 to 10 bullets.
- Do NOT include any additional text outside that format.
- Do NOT rename any public functions, classes, or module-level constants referenced by the tests.
- Do NOT change function signatures (parameters, defaults, *args/**kwargs) or return types.

## Behavioral Preservation Rules
- Treat the test suite as the source of truth, including any “odd” behaviors (e.g., returning None vs False).
- Preserve exceptions exactly (type and when they are raised) if tests depend on them.
- Preserve mutation behavior: if a function mutates an input (or intentionally does not), keep it the same.
- Preserve ordering: if output order is observable, keep it the same.

## Numerical and Precision Rules
- Maintain numerical semantics exactly.
- Do not introduce rounding unless the original implementation or tests require it.
- Keep floating-point computations stable; avoid “helpful” changes that alter results (e.g., changing operation order, using approximations, or different libraries).
- If a function performs mathematical conversions, use the canonical formula and avoid unnecessary intermediate rounding.

## Edge-Case Discipline
- Do not “fix” behaviors for edge cases unless tests specify a different behavior.
- Preserve current handling of empty inputs, single-element inputs, zeros, negatives, and duplicates.
- If behavior is ambiguous, infer it strictly from tests and existing code behavior.

## Refactoring Scope
Focus on readability without logic changes:
- Rename local variables for clarity (but do not rename public APIs used by tests).
- Extract small helper functions only if it does not change call/exception behavior.
- Reduce duplication using simple, transparent refactors.
- Add docstrings and type hints if they do NOT change runtime behavior.
- Keep algorithmic complexity the same unless a change is provably behavior-neutral under tests.

## Validation / Self-Checks (non-intrusive)
- You MAY add internal assertions only if they cannot trigger in valid inputs covered by tests.
- Prefer comments explaining invariants over assertions that could fire on unseen valid inputs.

## Process
1) Read the tests to learn required behavior, including edge cases and exact return values.
2) Identify the public API surface used by tests and keep it unchanged.
3) Refactor the implementation while preserving behavior exactly.
4) Re-check the refactor against the tests mentally; do not add speculative “improvements”.

---


## Implementation file content
<<<IMPLEMENTATION>>>
