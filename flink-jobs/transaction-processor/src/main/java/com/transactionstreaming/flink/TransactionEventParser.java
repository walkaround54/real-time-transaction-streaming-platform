package com.transactionstreaming.flink;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import org.apache.flink.api.common.functions.OpenContext;
import org.apache.flink.api.common.functions.RichMapFunction;

public class TransactionEventParser extends RichMapFunction<String, TransactionEvent> {
    private transient ObjectMapper objectMapper;

    @Override
    public void open(OpenContext openContext) {
        objectMapper = new ObjectMapper()
            .registerModule(new JavaTimeModule());
    }

    @Override
    public TransactionEvent map(String eventString) throws Exception {
        return objectMapper.readValue(eventString, TransactionEvent.class);
    }
}
