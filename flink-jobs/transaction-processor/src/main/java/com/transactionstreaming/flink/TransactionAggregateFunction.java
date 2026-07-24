package com.transactionstreaming.flink;

import org.apache.flink.api.common.functions.AggregateFunction;

public class TransactionAggregateFunction implements AggregateFunction<
    TransactionEvent, // in
    TransactionAggregateAccumulator, // accumulator
    TransactionAggregateAccumulator> { // output 
    
    @Override
    public TransactionAggregateAccumulator createAccumulator() {
        return new TransactionAggregateAccumulator();
    }

    @Override
    public TransactionAggregateAccumulator add(
        TransactionEvent event,
        TransactionAggregateAccumulator accumulator
    ) {
        double amount = event.amount();
        boolean failedStatus = "FAILED".equals(event.status());
        accumulator.addTransaction(amount, failedStatus);
        return accumulator;
    }

    @Override
    public TransactionAggregateAccumulator getResult(TransactionAggregateAccumulator accumulator) {
        // TODO: Return the accumulator as the intermediate window result.
        return accumulator;
    }

    @Override
    public TransactionAggregateAccumulator merge(
        TransactionAggregateAccumulator left,
        TransactionAggregateAccumulator right
    ) {
        TransactionAggregateAccumulator mergedAccumulator = left.merge(right);
        return mergedAccumulator;
    }
}