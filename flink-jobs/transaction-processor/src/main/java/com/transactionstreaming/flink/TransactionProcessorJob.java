package com.transactionstreaming.flink;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.connector.kafka.source.reader.deserializer.KafkaRecordDeserializationSchema;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import org.apache.flink.streaming.api.datastream.DataStream;

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

        // TODO: Parse each raw JSON string into a TransactionEvent.
        // Hint: Use map(...), and inside it call objectMapper.readValue(json, TransactionEvent.class).
        DataStream<TransactionEvent> transactions = rawTransactions
            ;

        // TODO: Print parsed TransactionEvent objects for verification.
        // Hint: This replaces printing the raw JSON strings.
        transactions.print();

        env.execute("transaction-processor");
    }
}
