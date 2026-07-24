package com.transactionstreaming.flink;

public class TransactionAggregateAccumulator {
    private long transactionCount;
    private double totalAmount;
    private long failedTransactionCount;
    private double failedTransactionAmount;

    public TransactionAggregateAccumulator(
        long transactionCount,
        double totalAmount,
        long failedTransactionCount,
        double failedTransactionAmount
    ) {
        this.transactionCount = transactionCount;
        this.totalAmount = totalAmount;
        this.failedTransactionCount = failedTransactionCount;
        this.failedTransactionAmount = failedTransactionAmount;
    }

    public TransactionAggregateAccumulator() {
        this.transactionCount = 0;
        this.totalAmount = 0.0;
        this.failedTransactionCount = 0;
        this.failedTransactionAmount = 0.0;
    }

    public void addTransaction(double amount, boolean failed) {
        transactionCount++;
        totalAmount += amount;

        if (failed) {
            failedTransactionCount++;
            failedTransactionAmount += amount;
        }
    }

    public long transactionCount() {
        return transactionCount;
    }

    public double totalAmount() {
        return totalAmount;
    }

    public long failedTransactionCount() {
        return failedTransactionCount;
    }

    public double failedTransactionAmount() {
        return failedTransactionAmount;
    }

    public TransactionAggregateAccumulator merge(TransactionAggregateAccumulator other) {
        long mergedTransactionCount = this.transactionCount() + other.transactionCount();
        double mergedTotalAmount = this.totalAmount() + other.totalAmount();
        long mergedFailedTransactionCount = this.failedTransactionCount() + other.failedTransactionCount();
        double mergedFailedTransactionAmount = this.failedTransactionAmount() + other.failedTransactionAmount();
        
        return new TransactionAggregateAccumulator(
            mergedTransactionCount,
            mergedTotalAmount, 
            mergedFailedTransactionCount, 
            mergedFailedTransactionAmount
        );
    }
}