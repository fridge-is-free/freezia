package com.s005.fif.service;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

import javax.swing.text.html.Option;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.s005.fif.common.exception.CustomException;
import com.s005.fif.common.exception.ExceptionType;
import com.s005.fif.dto.FcmSendDto;
import com.s005.fif.dto.response.CautionIngredientResponseDto;
import com.s005.fif.dto.response.FridgeIngredientResponseDto;
import com.s005.fif.entity.CautionIngredientRel;
import com.s005.fif.entity.Fridge;
import com.s005.fif.entity.FridgeIngredient;
import com.s005.fif.entity.Ingredient;
import com.s005.fif.entity.Member;
import com.s005.fif.repository.CautionIngredientRelRepository;
import com.s005.fif.repository.FridgeIngredientRepository;
import com.s005.fif.repository.FridgeRepository;
import com.s005.fif.repository.IngredientRepository;
import com.s005.fif.repository.MemberRepository;

@Service
@Transactional
@RequiredArgsConstructor
public class FridgeIngredientService {

	private final FridgeIngredientRepository fridgeIngredientRepository;
	private final IngredientRepository ingredientRepository;
	private final FridgeRepository fridgeRepository;
	private final CautionIngredientRelRepository cautionIngredientRelRepository;
	private final FirebaseCloudMessageService fcmService;
	private final MemberRepository memberRepository;

	/**
	 * 냉장고에 있는 모든 식재료를 조회한다.
	 * @param fridgeId : 냉장고 ID
	 * @return 냉장고 식재료 목록
	 */
	public List<FridgeIngredientResponseDto> getAllGredients(Integer fridgeId) {
		List<FridgeIngredient> fridgeIngredients = fridgeIngredientRepository.findAllByFridgeFridgeId(fridgeId);
		return fridgeIngredients.stream().map(FridgeIngredientResponseDto::fromEntity).toList();
	}

	/**
	 * 냉장고에 식재료를 추가한다.
	 * @param fridgeId : 냉장고 ID
	 * @param name : 식재료명
	 */
	@Transactional
	public void addIngredients(Integer fridgeId, String name) {
		Fridge fridge = fridgeRepository.findById(fridgeId)
			.orElseThrow(() -> new CustomException(ExceptionType.FRIDGE_NOT_FOUND));
		Ingredient ingredient = ingredientRepository.findByName(name)
			.orElseThrow(() -> new CustomException(ExceptionType.INGREDIENTS_NOT_FOUND));

		FridgeIngredient fridgeIngredient = FridgeIngredient.builder()
			.fridge(fridge)
			.ingredient(ingredient)
			.expirationDate(LocalDate.now().plusDays(ingredient.getExpirationPeriod()))
			.build();
		fridgeIngredientRepository.save(fridgeIngredient);
	}

	/**
	 * 냉장고 속 식재료를 삭제하고, 사용자의 위험식재료일 경우 메시지를 전송한다.
	 * @param memberId
	 * @param fridgeIngredientId
	 */
	@Transactional
	public void removeIngredients(Integer memberId, Integer fridgeIngredientId) {
		// 식재료 제거
		FridgeIngredient fridgeIngredient = fridgeIngredientRepository.findById(fridgeIngredientId)
			.orElseThrow(() -> new CustomException(ExceptionType.FRIDGE_INGREDIENT_NOT_FOUND));
		// fridgeIngredientRepository.delete(fridgeIngredient);

		// 위험식재료 판단
		Optional<CautionIngredientRel> cautionIngredient = cautionIngredientRelRepository.findByMemberIdAndIngredientId(
			memberId, fridgeIngredient.getIngredient().getIngredientId());
		if(cautionIngredient.isPresent()) {
			Member member = memberRepository.findById(memberId)
				.orElseThrow(() -> new CustomException(ExceptionType.MEMBER_NOT_FOUND));
			// 모바일 앱 푸시
			Ingredient ingredient = cautionIngredient.get().getIngredient();
			FcmSendDto fcmSendDto = FcmSendDto.builder()
				.token(member.getMobileToken())
				.title("위험 식재료 알림")
				.body("방금 꺼내신 "+ingredient.getName()+"는 지병에 좋지 않아요.")
				.data(CautionIngredientResponseDto.builder()
					.name(ingredient.getName())
					.description(cautionIngredient.get().getDescription())
					.imgUrl(ingredient.getImgUrl())
					.build())
				.build();
			fcmService.sendMessageTo(fcmSendDto);
		}
	}
}
