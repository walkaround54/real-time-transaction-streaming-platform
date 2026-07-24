package com.transactionstreaming.flink;

import org.apache.flink.streaming.api.functions.windowing.ProcessWindowFunction;
import org.apache.flink.streaming.api.windowing.windows.TimeWindow;
import org.apache.flink.util.Collector;

import java.time.Instant;

public class TransactionWindowFunction extends ProcessWindowFunction<
    TransactionAggregateAccumulator,
    TransactionProcessed,
    String,
    TimeWindow
> {
    @Override
    public void process(
        String customerId,
        Context context, // provided by Flink
        Iterable<TransactionAggregateAccumulator> elements,
        Collector<TransactionProcessed> out
    ) {
        TransactionAggregateAccumulator accumulator = elements.iterator().next();

        Instant windowStart = Instant.ofEpochMilli(context.window().getStart());
        Instant windowEnd = Instant.ofEpochMilli(context.window().getEnd());

        double averageAmount = accumulator.transactionCount() == 0
            ? 0.0
            : accumulator.totalAmount() / accumulator.transactionCount();

        TransactionProcessed transactionProcessed = new TransactionProcessed(
            customerId,
            windowStart,
            windowEnd,
            accumulator.transactionCount(),
            accumulator.totalAmount(),
            averageAmount,
            accumulator.failedTransactionCount(),
            accumulator.failedTransactionAmount()
        );

        out.collect(transactionProcessed);
    }
}