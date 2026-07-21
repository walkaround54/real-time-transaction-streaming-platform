package com.transactionstreaming.flink;

import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class TransactionProcessorJob {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        env.setParallelism(1);

        env.fromData("Flink transaction processor scaffold working").print();

        env.execute("transaction-processor");

    }
}