package com.transactionstreaming.flink;
import java.time.Instant;
import com.fasterxml.jackson.annotation.JsonProperty;

public record TransactionEvent( 
    // automatically generates methods like constructor, field accessors, toString()
    @JsonProperty("transaction_id") String transactionId,
    @JsonProperty("customer_id") String customerId,
    @JsonProperty("account_id") String accountId,
    @JsonProperty("merchant_id") String merchantId,
    @JsonProperty("merchant_category") String merchantCategory,
    @JsonProperty("amount") double amount,
    @JsonProperty("currency") String currency,
    @JsonProperty("country") String country,
    @JsonProperty("channel") String channel,
    @JsonProperty("status") String status,
    @JsonProperty("event_time") Instant eventTime
) {}

