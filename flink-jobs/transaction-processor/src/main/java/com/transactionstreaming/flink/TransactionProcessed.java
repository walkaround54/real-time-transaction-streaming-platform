package com.transactionstreaming.flink;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.time.Instant;

public record TransactionProcessed(
    // JSON field name first followed by Java field name
    @JsonProperty("customer_id") String customerId,
    @JsonProperty("window_start") Instant windowStart,
    @JsonProperty("window_end") Instant windowEnd,
    @JsonProperty("transaction_count") long transactionCount,
    @JsonProperty("total_amount") double totalAmount,
    @JsonProperty("average_amount") double averageAmount,
    @JsonProperty("failed_transaction_count") long failedTransactionCount,
    @JsonProperty("failed_transaction_amount") double failedTransactionAmount
) {}