package com.s005.fif.dto.request;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
public class RecipeImageRequestDto {
	private Integer recipeId;
	private String recipeName;
	private String ingredient;
}
