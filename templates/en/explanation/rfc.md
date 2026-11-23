---
template:
  version: 1
  name: RFC / design doc
  description: A proposal before the decision (the ADR records the result)
  category: explanation
  example: explanation/rfc.md
  folder: rfcs
  numbered: true
  fields:
    status:
      prompt: Status
      default: "Draft"
---

# {{title}}

Status: {{status}}

Author: {{owner}} · Date: {{date}}

## Summary

The proposal in two or three sentences.

## Problem

What is wrong today, and who it affects. Numbers help: errors, time, cost.

## Proposal

How it would work. A diagram, the main flows and what changes for each team.

## Alternatives

| Option       | Pros | Cons |
|--------------|------|------|
| The proposal |      |      |
| Do nothing   |      |      |

## Risks and open questions

- What could go wrong, and how we would notice
- What still needs an answer, and who can answer it

## Rollout

The steps to get there, and how to go back.
