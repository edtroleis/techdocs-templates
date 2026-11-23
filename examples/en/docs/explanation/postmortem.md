# Postmortem: duplicate charges on 2026-03-02

A blameless review. The goal is to learn, not to find who to blame.

## Summary

For 40 minutes, 312 customers were charged twice. All of them were refunded the same day.

## Impact

- 312 duplicate charges, 18,400 USD in total, refunded by 18:00
- 47 support tickets

## Timeline

| Time  | What happened                                        |
|-------|------------------------------------------------------|
| 14:05 | The provider starts answering in 20 s instead of 1 s |
| 14:06 | Checkout times out at 10 s and retries the payment   |
| 14:20 | Support reports customers charged twice              |
| 14:45 | Checkout retries turned off; duplicates stop         |
| 18:00 | Last refund done                                     |

## Root cause

Checkout retried payments after a timeout, and the Payments Service had no way to tell a retry from a new
payment.

## What went well and what did not

- Went well: refunds were scripted and finished the same day.
- Did not: no alert for duplicate charges; support found out first.

## Actions

| Action                                                | Owner    | Due        |
|-------------------------------------------------------|----------|------------|
| Idempotency keys ([ADR 0003](adr.md))                 | Payments | 2026-04-15 |
| Alert for two payments of the same order in 5 minutes | Payments | 2026-03-20 |
