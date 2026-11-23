# {{site_name}}

What to do when an alert fires. Each alert points to one runbook; start here
during an incident.

## Alert index

| Alert           | Severity | Runbook         |
| --------------- | -------- | --------------- |
| High error rate | Critical | Example runbook |
| Queue growing   | Warning  | (to write)      |

## During an incident

1. Acknowledge the alert, so nobody else starts the same work.
2. Open the runbook for the alert and follow it.
3. If the runbook does not solve it, escalate (see Escalation).
4. After the incident, write a postmortem.

## Keeping the runbooks useful

- A runbook that did not work is fixed right after the incident
- An alert without a runbook is either given one or removed

## Who looks after it

These runbooks are maintained by {{owner}}.
