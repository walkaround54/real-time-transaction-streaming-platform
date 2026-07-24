package com.transactionstreaming.flink;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.TumblingEventTimeWindows;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
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

        ObjectMapper objectMapper = new ObjectMapper()
            .registerModule(new JavaTimeModule());

        // ObjectValue methods:
        // readValue() parses JSON into a Java object
        // writeValue() write JSON to a file, stream
        // convertValue() convert one Java Object into another Java type
        DataStream<TransactionEvent> transactions = rawTransactions
            .map(eventString -> objectMapper.readValue(eventString,TransactionEvent.class));
        
        DataStream<TransactionEvent> transactionsWatermarked = transactions
            .assignTimestampsAndWatermarks(
                WatermarkStrategy.<TransactionEvent>forBoundedOutOfOrderness(Duration.ofSeconds(30))
            .withTimestampAssigner((transactionEvent, timestamp) -> transactionEvent.eventTime().toEpochMilli()));
        
        transactionsWatermarked.print();
        
        // KeyedStream<Original Stream Type, Key Type>
        KeyedStream<TransactionEvent, String> transactionsByCustomer = transactionsWatermarked
            .keyBy(transactionEvent -> transactionEvent.customerId());
        
        WindowedStream<TransactionEvent, String, TimeWindow> customerTransactionsByMinute = transactionsByCustomer
                .window(TumblingEventTimeWindows.of(Time.minutes(1)))
                .aggregate((event -> ))
        
        env.execute("transaction-processor");
    }
}
