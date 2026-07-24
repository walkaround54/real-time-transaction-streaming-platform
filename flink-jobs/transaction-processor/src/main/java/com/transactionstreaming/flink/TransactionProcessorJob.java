package com.transactionstreaming.flink;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.TumblingEventTimeWindows;
import org.apache.flink.streaming.api.windowing.windows.TimeWindow;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.KeyedStream;
import org.apache.flink.streaming.api.datastream.WindowedStream;
import java.time.Duration;

public class TransactionProcessorJob {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        env.setParallelism(1);

        KafkaSource<String> source = KafkaSource.<String>builder()
            .setBootstrapServers("broker:29092")
            .setTopics("transactions_raw")
            .setGroupId("flink-transactions-processor")
            .setValueOnlyDeserializer(new SimpleStringSchema())
            .setStartingOffsets(OffsetsInitializer.earliest())
            .build();

        DataStream<String> rawTransactions = env
            .fromSource(source, WatermarkStrategy.noWatermarks(), "transactions-raw-source");

        DataStream<TransactionEvent> transactions = rawTransactions
            .map(new TransactionEventParser());
        
        DataStream<TransactionEvent> transactionsWatermarked = transactions
            .assignTimestampsAndWatermarks(
                WatermarkStrategy.<TransactionEvent>forBoundedOutOfOrderness(Duration.ofSeconds(30))
            .withTimestampAssigner((transactionEvent, timestamp) -> transactionEvent.eventTime().toEpochMilli()));
        
        // KeyedStream<Original Stream Type, Key Type>
        KeyedStream<TransactionEvent, String> transactionsByCustomer = transactionsWatermarked
            .keyBy(transactionEvent -> transactionEvent.customerId());
        
        WindowedStream<TransactionEvent, String, TimeWindow> customerTransactionsByMinute = transactionsByCustomer
                .window(TumblingEventTimeWindows.of(Duration.ofMinutes(1)));
        
        DataStream<TransactionProcessed> processedTransactions = customerTransactionsByMinute
                .aggregate(
                    new TransactionAggregateFunction(),
                    new TransactionWindowFunction()
                );
        
        processedTransactions.print();
        // by default, a DataStream prints as it processes, and not all at once

        env.execute("transaction-processor");
    }
}
