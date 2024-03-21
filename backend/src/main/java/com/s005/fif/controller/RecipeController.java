package com.s005.fif.controller;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.s005.fif.common.auth.MemberDto;
import com.s005.fif.common.response.Response;
import com.s005.fif.dto.request.CompleteCookRequestDto;
import com.s005.fif.service.RecipeService;

import io.swagger.v3.oas.annotations.Operation;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/recipes")
@RequiredArgsConstructor
public class RecipeController {

    private final RecipeService recipeService;

    @GetMapping
    @Operation(summary = "레시피 목록 조회")
    public Response getRecipes(MemberDto memberDto) {
        return new Response("recipes", recipeService.getRecipes(memberDto.getMemberId()));
    }

    @GetMapping("/history/save")
    @Operation(summary = "저장한 레시피 목록 조회")
    public Response getSavedRecipes(MemberDto memberDto) {
        return new Response("recipes", recipeService.getSavedRecipes(memberDto.getMemberId()));
    }

    @GetMapping("/history/complete")
    @Operation(summary = "완료한 레시피 목록 조회")
    public Response getCompletedRecipes(MemberDto memberDto) {
        return new Response("recipes", recipeService.getCompletedRecipes(memberDto.getMemberId()));
    }

    @GetMapping("/recommendation")
    @Operation(summary = "추천 레시피 목록 조회")
    public Response getRecommendationRecipes(MemberDto memberDto) {
        return new Response("recipes", recipeService.getRecommendationRecipes(memberDto.getMemberId()));
    }

    @GetMapping("/{recipeId}")
    @Operation(summary = "레시피 상세 조회")
    public Response getRecipe(MemberDto memberDto, @PathVariable Integer recipeId) {
        return new Response("recipeInfo", recipeService.getRecipe(memberDto.getMemberId(), recipeId));
    }

    @GetMapping("/{recipeId}/steps")
    @Operation(summary = "레시피 단계 상세 조회")
    public Response getRecipeSteps(MemberDto memberDto, @PathVariable Integer recipeId) {
        return new Response("recipeSteps", recipeService.getRecipeSteps(memberDto.getMemberId(), recipeId));
    }

    @PatchMapping("/{recipeId}/save")
    @Operation(summary = "레시피 북마크 저장")
    public Response toggleSaveYn(MemberDto memberDto, @PathVariable Integer recipeId) {
        return new Response(Response.MESSAGE, recipeService.toggleSaveYn(memberDto.getMemberId(), recipeId));
    }

    @PostMapping("/{recipeId}/complete")
    public Response completeCook(MemberDto memberDto, @PathVariable Integer recipeId, @RequestBody @Valid CompleteCookRequestDto dto) {
        return new Response(Response.MESSAGE, recipeService.completeCook(memberDto.getMemberId(), recipeId, dto));
    }

    @GetMapping("/{recipeId}/complete")
    public Response getCompleteCook(MemberDto memberDto, @PathVariable Integer recipeId) {
        return new Response("completeCooks", recipeService.getCompleteCook(memberDto.getMemberId(), recipeId));
    }

    @DeleteMapping("/complete/{completeCookId}")
    public Response deleteCompleteCook(MemberDto memberDto, @PathVariable Integer completeCookId) {
        return new Response(Response.MESSAGE, recipeService.deleteCompleteCook(memberDto.getMemberId(), completeCookId));
    }
}
