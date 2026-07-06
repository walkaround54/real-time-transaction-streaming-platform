# Fraud Engine

## Objective

Detect suspicious financial behaviour in real time using Flink's stateful processing.

## Fraud Rules

1. Spend > SGD10,000 within 5 minutes
2. More than 5 transactions within 60 seconds
3. More than 3 failed transactions within 5 minutes
4. Multiple countries within a short period
5. Transaction significantly above customer's historical average

## RocksDB State

Maintain:

- Running spend
- Transaction counter
- Failed transaction counter
- Previous country
- Last transaction timestamp
- Historical average spend

## Alert Topic

`transactions_alerts`

Example payload:

```json
{
  "alert_id":"ALERT100001",
  "customer_id":"CUST001",
  "severity":"HIGH",
  "alert_type":"HIGH_VELOCITY_SPEND"
}
```

## Future Ideas

- Machine learning anomaly detection
- Device fingerprinting
- Velocity scoring
- Risk score aggregation
- Explainable fraud decisions