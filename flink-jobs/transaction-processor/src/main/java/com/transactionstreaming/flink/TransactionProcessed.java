package com.transactionstreaming.flink;
import java.time.Instant;

public record TransactionProcessed(
    String customerId,
    Instant windowStart,
    Instant windowEnd,
    long transactionCount,
    double totalAmount,
    double averageAmount,
    long failedTransactionCount,
    double failedTransactionAmount
)

{}
