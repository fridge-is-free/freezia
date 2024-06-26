package com.s005.fif.controller;

import java.util.List;

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
import com.s005.fif.dto.request.ShoppingListRequestDto;
import com.s005.fif.dto.response.FridgeIngredientResponseDto;
import com.s005.fif.dto.response.ShoppingListResponseDto;
import com.s005.fif.service.ShoppingListService;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/shopping-list")
public class ShoppingListController {

	private final ShoppingListService shoppingListService;

	@GetMapping
	@Operation(summary = "쇼핑리스트 조회")
	@ApiResponse(
		content = {
			@Content(
				mediaType = "application/json",
				array = @ArraySchema(schema = @Schema(implementation = ShoppingListResponseDto.class))
			)
		}
	)
	public Response getShoppingList(@Parameter(hidden = true)MemberDto memberDto) {
		List<ShoppingListResponseDto> shoppingList = shoppingListService.getShoppingList(memberDto.getMemberId());
		return new Response("shoppingList", shoppingList);
	}

	@PostMapping
	@Operation(summary = "쇼핑리스트 아이템 등록")
	public Response postShoppingList(@Parameter(hidden = true)MemberDto member, @RequestBody ShoppingListRequestDto shoppingListRequestDto) {
		shoppingListService.addShoppingList(member.getMemberId(), shoppingListRequestDto);
		return new Response();
	}

	@PatchMapping("/{shoppingListId}")
	@Operation(summary = "쇼핑리스트 아이템 체크")
	@ApiResponse(
		content = {
			@Content(
				mediaType = "application/json",
				schema = @Schema(example = "{\"checkYn\": \"\"}")
			)
		}
	)
	public Response checkShoppingList(@Parameter(hidden = true) MemberDto memberDto, @PathVariable Integer shoppingListId) {
		Boolean checkYn = shoppingListService.checkShoppingList(memberDto.getMemberId(), shoppingListId);
		return new Response("checkYn", checkYn);
	}

	@DeleteMapping("/{shoppingListId}")
	@Operation(summary = "쇼핑리스트 아이템 삭제")
	public Response deleteShoppingList(@Parameter(hidden = true)MemberDto memberDto, @PathVariable Integer shoppingListId) {
		shoppingListService.deleteShoppingList(memberDto.getMemberId(), shoppingListId);
		return new Response();
	}
}
