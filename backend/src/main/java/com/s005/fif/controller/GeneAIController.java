package com.s005.fif.controller;

import com.s005.fif.common.response.Response;
import com.s005.fif.dto.request.GeneAIPromptRequestDto;
import com.s005.fif.service.GeneAIService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

@RestController
@RequestMapping("/api/generate-AI")
@RequiredArgsConstructor
public class GeneAIController {

    private final GeneAIService geneAIService;

    @GetMapping("/websocket")
    public Response getThreadAndAssistant() {
        geneAIService.get();
        return new Response("fridgeIngredients", 1);
    }

    @GetMapping(produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> streamDataFromAI(GeneAIPromptRequestDto geneAIPromptRequestDto) {

        // FastAPI에서 SSE 스트림을 받는 로직
        Flux<String> fastApiStream = geneAIService.getStreamDataFromAI(geneAIPromptRequestDto);

        // 받아온 스트림을 그대로 클라이언트에 전송
        return fastApiStream;
    }

//    @GetMapping
//    public SseEmitter streamDataFromAI() throws IOException {
//        SseEmitter emitter = new SseEmitter();
//
//        // FastAPI에서 SSE 스트림을 받는 로직
//        Flux<String> fastApiStream = webClientService.getStreamDataFromAI();
//
//        fastApiStream.subscribe(
//                // 데이터를 받을 때마다 클라이언트에 데이터 전송
//                data -> {
//                    try {
//                        emitter.send(data);
//                    } catch (IOException e) {
//                        emitter.completeWithError(e);
//                    }
//                },
//                // 에러 처리
//                error -> emitter.completeWithError(error),
//                // 스트림 완료 처리
//                () -> emitter.complete()
//        );
//
//        return emitter;
//    }


}
