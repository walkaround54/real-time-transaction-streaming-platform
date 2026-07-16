# Fraud Engine

## Objective

Detect suspicious financial behaviour in real time using Flink's stateful processing.

## Fraud Rules

1. Spend > SGD10,000 within 5 minutes
2. More than 5 transactions within 60 seconds
3. More than 3 failed transactions within 5 minutes
4. Multiple countries within a short period
5. Transaction significantly above customer's historical average

These rules should combine short-term velocity checks with longer-term customer history. A one-minute aggregation is useful for validating the first Flink job, but realistic fraud detection needs baselines over longer horizons such as 1 day, 7 days, or 30 days.

## Customer Profile

Maintain a customer profile so the fraud engine can compare current behaviour against normal behaviour.

Potential profile fields:

- Usual countries
- Usual channels
- Usual merchant categories
- Average transaction amount
- Median transaction amount
- Daily average spend
- Weekly average spend
- Failed transaction rate
- Previous transaction country
- Last transaction timestamp

## RocksDB State

Maintain:

- Running spend
- Transaction counter
- Failed transaction counter
- Previous country
- Last transaction timestamp
- Historical average spend

RocksDB will later store this customer-level state so Flink can update the profile continuously as new transactions arrive.

## Anomalous Transaction Generation

The producer should eventually generate explicit suspicious scenarios so the fraud rules can be tested intentionally.

Candidate scenarios:

- High-value transaction
- Rapid repeated transactions for the same customer
- Repeated failed transactions
- Transaction from an unusual country
- Transaction in an unusual merchant category
- Sudden spend spike compared with the customer's historical profile

The first version can keep these scenarios simple and probabilistic, such as mostly normal transactions with a small percentage of suspicious transactions.

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
