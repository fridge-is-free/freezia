CONVERSATION_JSON_FORMAT = """
                이 때, 레시피는 전부 1인분 기준으로 재료 수량 정보를 제공해주도록 해.

                {
                    reply : "냉장고에 있는 스팸, 마요네즈, 김치를 사용해 레시피를 생성했습니다.",
                    recommendList : [
                        "가장 최근에 만든 요리와 비슷한 재료를 사용하는 레시피를 알려줘",
                        "간식으로 먹고 싶은데 칼로리를 절반으로 줄인 레시피를 알려줘",
                        "덮밥말고 볶음밥 레시피로 알려줘"
                    ],
                    recipeList : [
                        {
                            name : '스팸마요김치덮밥',
                            ingredientList : [
                                {
                                    name : '재료명',
                                    amounts : '재료의 양',
                                    unit : '단위 종류',
                                }
                            ],
                            seasoningList : [
                                {
                                    name : '조미료명',
                                    amounts : '조미료의 양',
                                    unit : '단위 종류',  // 조금, 약간 같은 애매한 단위를 제시하지 말고 명확한 단위를 제시해줘. ex) g, kg, 한줌, 1T, 1스푼
                                }
                            ],
                            cookTime : '총 요리에 필요한 시간',
                            carlorie : '요리의 칼로리 수치',
                            servings : '요리 제공량' // 몇 인분인지,
                            recipeType : '요리 유형', // 이 예시 내에서만 반환 - 한식, 양식, 중식, 일식, 밑반찬, 면요리, 볶음요리, 찜요리, 국물요리, 유통기한 임박 중 하나로 리턴해줘.
                            recipeSteps: [
                                {
                                    type: '단계 유형', // ex: '끓이기', '재료손질', '굽기', '볶기'
                                    description : '해당 단계 설명',
                                    name : '해당 단계 이름',
                                    duration : '해당 단계 진행 시간, 타이머에 사용할 것이므로 초 단위로 숫자만 제공', ex: 300
                                    tip : '해당 단계에 도움이 되는 요리 팁',
                                },
                            ]
                        },
                    ]
                }
            """

RECIPE_JSON_FORMAT = """
이 때, 레시피는 전부 1인분 기준으로 재료 수량 정보를 제공해주도록 해.
재료명은 명확하게 한가지 재료만 명시해.
조미료를 합쳐서 양념장을 만들어서 넣어야하는 경우에는 조리 단계에 양념장을 만드는 것과 양념장을 넣는다고 명시해주도록 해.

{
    reply : "냉장고에 있는 스팸, 마요네즈, 김치를 사용해 레시피를 생성했습니다.",
    recipeList : [
        {
            name : '스팸마요김치덮밥',
            ingredientList : [
                {
                    name : '재료명',
                    amounts : '재료의 양',
                    unit : '단위 종류',
                }
            ],
            seasoningList : [
                {
                    name : '조미료명',
                    amounts : '조미료의 양',
                    unit : '단위 종류', // 조금, 약간 같은 애매한 단위를 제시하지 말고 명확한 단위를 제시해줘. ex) g, kg, 한줌, 1T, 1스푼
                }
            ],
            cookTime : '총 요리에 필요한 시간',
            carlorie : '요리의 칼로리',
            servings : '요리 제공량' // 몇 인분인지,
            recipeType : '요리 유형', // 이 예시 내에서만 반환 - 한식, 양식, 중식, 일식, 밑반찬, 면요리, 볶음요리, 찜요리, 국물요리, 유통기한 임박 중 하나로 리턴해줘.
            recipeSteps: [
                {
                    type: '단계 유형', // ex: '끓이기', '재료손질', '굽기', '볶기'
                    description : '해당 단계 설명',
                    name : '해당 단계 이름',
                    duration : '해당 단계 진행 시간, 타이머에 사용',
                    tip : '해당 단계에 도움이 되는 요리 팁',
                    timer : '해당 단계에서 걸리는 시간'
                },
            ]
        },
    ]
}
"""

CHINA = """
대한민국에서 대중적으로 인기를 얻은 짜장면과 짬뽕 등 한국식 중국 요리는 화교들이 많이 살던 인천광역시에서 개발되었다.
이러한 과다한 경제 창출 때문에 결국 박정희 정부는 화폐개혁과 외국인 토지 소유 금지를 통해 화교의 경제력을 약화시켰는데 이 때문에 많은 화교들이 한국을 떠나거나 그 주업이 외식업으로 국한되었다. 
1960년대 ~ 1970년대 정부가 분식을 장려하고 비교적 짧은 조리시간이 산업화 시대의 요구와 맞아떨어지면서 짜장면 등 중국 요리는 대중적인 외식요리로 자리 잡았다.
대중적인 중국 음식점이 기하급수적으로 늘면서 현재의 중국 음식점은 화교보다는 한국인이 소유와 운영을 맡고 있는 경우가 대부분이다.
현재 신화교가 많이 들어서면서 다시 신화교 소유 음식점이 생기고 있는데, 그중 마라탕은 대표적인 신화교 음식이 되었다. 
이 영향으로 마라탕 매출이 급상승하여 마라 열풍이 생겨 지금까지 운영되고 있다.

"""

RESTAURANT = """
프랑스 ·영국 ·독일 ·이탈리아 및 미국의 요리가 혼성된 것, 그 일부가 가미된 것, 또는 한국식으로 변화된 것 등을 통틀어 서양요리라 하는데, 실제로 서양요리의 중심은 프랑스 요리이며, 국제적인 연회에서는 프랑스식의 조리법이 사용되고, 메뉴도 프랑스어로 적는 것이 관례이다. 서양요리에 공통되는 특징은, 한마디로 육류나 유지를 주재료로 쓰고 스파이스(바닐라·레몬·에센스·후추·고추 등의 향신료)를 많이 넣어 조리하는 것이다. 서양요리가 한국에 전래된 것은 정확하지는 않으나 개화와 더불어 들어온 것 같다.
서양에서는 식사양식이 끼니마다 다르고, 식사종류로는 아침·점심·저녁·정찬 등이 있다.

아침식사: 가족끼리 아침에 먹는 식사로서 가벼운 아침식사, 보통 아침식사, 여러 가지를 갖춘 아침식사 등 3가지가 있다. 첫번째 식단은 과일 또는 과일 주스·토스트·음료 등이고, 두번째 식단은 과일 또는 과일 주스·곡류음식·달걀·빵·음료 등이며, 세번째는 과일 또는 과일 주스·곡류음식·달걀과 베이컨·빵·음료 등이다.

점심식사: 아침보다는 약간 풍성하게 먹는 편인데, 샌드위치로 가볍게 먹는 경우와 일품요리 또는 육류요리와 채소요리까지 곁들이는 경우가 있다. 샌드위치를 먹을 때의 식단은 수프·샌드위치·샐러드·후식·음료 등이고 일품요리 식사의 식단은 일품요리·샐러드·빵·후식·음료 등이다.

저녁식사: 간소하게 먹는 저녁식사와 주된 요리에 수프 등을 갖춘 가족 디너가 있다. 가족 디너의 식단은 수프(또는 과일 칵테일)·주요리(생선 또는 고기요리)·샐러드·빵·후식·음료 등으로 구성된다.

정찬: 손님을 초대해서 대접할 때 또는 행사가 있을 때 차리는 성찬인데, 점심 때 차리는 것을 오찬, 저녁 때 차리는 것을 만찬이라 한다. 정찬의 풀 코스는 전채요리·콩소메(consommé:수프)·생선요리·앙트레(entrée:부드러운 닭 또는 양고기요리)·고기요리·샐러드·후식·드미타스 커피(demi-tasse coffee)로 이루어진다. 전채요리는 오르되브르(hors-d’œuvre) 또는 애피타이저라고도 한다. 정찬에 곁들이는 음료로는 식욕촉진을 위한 칵테일류 ·셰리 ·뒤포네(포도주의 일종) ·주스 등이 있으며, 전채요리에는 셰리, 생선요리에는 백포도주, 고기요리에는 적포도주를 쓰고, 축하연일 때는 샴페인을 쓴다. 탄산수 ·물은 식사 중 필요할 때마다 요구할 수 있고 식후에는 별실에서 리큐어 또는 브랜디 ·위스키 등으로 마무리를 한다.

"""

KOREA = """
한국의 요리이다. 한국에서 발달한 고유하고도 전통적인 음식을 흔히 한식(韓食)으로도 부른다. 
복잡한 궁중 요리에서부터 지방의 특색 요리와 현대의 맛있는 요리에 이르기까지 재료와 조리법이 매우 다양하다. 
현대 한국 요리는 남한 요리(남조선 요리)와 북한 요리(북조선 요리)로 나누기도 한다. 
전통적인 한국 정식은 밥, 국, 김치, 장 등과 함께 나오는 많은 반찬들로 이루어진다. 
한국 요리는 주로 쌀을 기반으로 일반적으로 사용되는 성분 포함 참기름, 들기름, 고추장, 된장, 간장, 소금, 마늘, 생강, 고춧가루, 다시마 국물 등으로 맛을 낸다. 
김치는 거의 항상 모든 음식에서 제공된다.
"""

JAPAN = """
주요 특징으로는 섬나라 임을 근간으로 하는 해산물이 주류라는 것과 '생식(生食)', '(재료 본연의 맛을 중시하는) 담백한 양념류', '섬세한 담는 방식' 이상의 세 가지가 주로 꼽힌다. 다만 이는 상술한 가이세키 같은 일본 전통 요리나 회 같은 순수 100% 생식에서나 주로 찾아볼 수 있고, 실제로는 야키소바, 라멘, 나베, 초밥 등 간이 진한 음식들도 많다. 초밥은 의외일 수도 있지만 제조과정에서 식초와 설탕을 기본적으로 상당히 넣고, 시식자 취향에 따라서 간장과 와사비까지 들어간다.
- 차가운 요리가 많다
- 재료가 중요하다
- 해산물 등 날 것으로 먹는 음식이 많다
- 장식이 많다
- 육식 메뉴의 부족
- 근대 이후의 육식 문화
- 조미(調味) 방식
- 적은 향신료 사용
- 과도한 소금 사용
- 느끼하고 기름지다
- 설탕의 사용에 관하여
- 차(茶) 등 음료 섭취
"""

SIDE_DISH = """
마른 찬이라고도 불리는 밑반찬은 대부분의 상차림에 한두 가지가 오를 정도로 종류와 쓰임새가 다양한 가정 상비 음식이다. 식품 저장법이 발달하지 못한 시절에 상하기 쉬운 식품을 장기간 보존하기 위해 염장을 했다. 이를 자반이라 하고, 한자어로는 좌반佐飯이라 한다. 조선무쌍신식요리제법에 “자반이라는 것은 밥을 먹도록 도와준다 하여 좌반이라 하고 어느 집이든지 젓갈이나 자반은 저축하여야 하는데 두 가지가 모두 소금에만 만든 물건이라 여러 찬수에 없어서는 안 되는 것이다.”라고 되어 있다. 자반은 그 말의 어원이 좌반에서 비롯되었듯이 넓은 뜻으로는 밥에 곁들이는 음식의 총칭이며, 좁은 뜻으로는 생선을 소금에 절인 반찬감이다. 자반은 또 생선을 소금에 절인 것 이외에 채소나 해산물을 고추장이나 찹쌀풀을 발라 말려서 튀기거나 짭짤하게 조리거나 무친 것, 볶은 것 등 종류가 다양하다. 자반에는 매듭자반이나 미역자반처럼 기름에 튀겨서 간을 한 것도 있고 호두튀각, 다시마튀각처럼 식용유에 튀긴 후 설탕을 뿌리는 것도 있다. 가장 널리 쓰이는 생선자반은 고등어자반, 준치자반, 조기자반, 비웃(청어자반), 갈치자반, 뱅어자반, 밴댕이자반, 전어자반 등 종류가 매우 많다.
부각과 튀각은 제철에 나는 재료를 그때그때 갈무리해 두는 방법으로 널리 이용되었다. 감자부각, 김부각, 참죽부각, 아카시아꽃부각, 동백잎부각, 깻잎부각, 들깨송이부각, 메뚜기부각, 국화잎부각, 풋고추부각, 두릅부각 등 다양하다.
더덕·무·오이·마늘·생선 등을 간장이나 된장·고추장·막장·식초 속에 넣어 삭힌 다음 그냥 또는 양념하여 먹는 것으로, 상차림에 대비하여 준비해 두는 밑반찬(묵혀 두고 먹는 반찬)이다. 감장아찌, 두부장아찌, 가지장아찌, 달래장아찌, 깻잎장아찌, 천초장아찌, 산초장아찌, 굴비장아찌, 전복장아찌 등 많은 종류가 있다. 이것은 초기 김치의 한 원형에서 비롯된 것으로, 채소류 대부분이 다양하게 장아찌로 쓰이고 있으며 보수성 강하게 전해 내려오는 전통음식이다. 그 밖에 장산적, 장똑똑이, 섭산적, 전복쌈, 어란魚卵, 북어무침(북어보푸라기), 멸치볶음, 코다리조림, 콩자반, 오징어채무침, 암치, 건대구, 고추장볶음(약고추장) 등도 있다. 이렇게 다양한 종류의 포, 자반, 부각, 튀각, 조림, 볶음, 장아찌 등 밑반찬은 보존성이 뛰어나고 깊은 맛이 있어 상차림에 두루 쓰였다. 특히 생선자반은 교통이 발달하지 못했고 냉동·냉장 시설이 없던 시절에 장꾼들이 산간오지까지 생선을 공급할 수 있어 자반 중 으뜸으로 취급받았다. 우리 조상들은 사계절이 뚜렷한 자연환경 속에서 먹거리가 부족한 겨울에 포나 자반, 부각, 장아찌 등을 이용하여 제철이 아닌 때와 비상시에도 요긴하게 먹을 수 있도록 저장식품을 미리 장만해두곤 하였다.
밑반찬은 소금·간장 등으로 간을 짙게 한 음식이어서 부패와 변질이 잘되지 않아 저장성이 뛰어나다. 또 보관 기간에 품질의 변화가 거의 없고, 재가열 등 조리 조작이 필요하지 않는 장점이 있다.
"""


CHINA_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 레시피 30개 중 중식 요리일 확률이 80 이상인 레시피만 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int 값으로 반환)
}


ex) {
    짜장면 : 100,
    크림파스타 : 0,
    김치찌개 : 0 
}

"""

RESTAURANT_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 레시피 20개 중 양식 요리일 확률이 80 이상인 레시피만 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int 값으로 반환)
}


ex) {
    짜장면 : 0,
    크림파스타 : 100,
    스테이크 : 100
    김치찌개 : 0 
}

"""

KOREA_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 레시피 20개 중 한식 요리일 확률이 80 이상인 레시피만 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int 값으로 반환)
}


ex) {
    짜장면 : 0,
    크림파스타 : 0,
    스테이크 : 20,
    김치찌개 : 100, 
    된장찌개 : 100
}

"""

JAPAN_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 레시피 20개 중 일식 요리일 확률이 80 이상인 레시피만 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int 값으로 반환)
}


ex) {
    광어초밥 : 100,
    일본카레 : 100,
    라멘 : 100,
    짜장면 : 0,
    김치찌개 : 0
}

"""

FRY_ANSWER_JSON= """
튀길때는 메인 식재료를 단 하나만 사용해서 튀기도록 해.
김치 튀김이나 마늘 튀김, 짜장 튀김같은건 추천하지마. 대중적인 튀김요리만 추천하도록 해.
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 튀김 요리 레시피 20개를 튀김요리일 확률과 함께 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int값으로 반환)
}

ex) {
    감자튀김 : 100,
    가지튀김 : 100,
    돈까스 : 100,
    야끼소바 : 0,
    김치찌개 : 0,
    스프 : 0
}

"""

STIR_FRY_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 볶음 요리 레시피 20개를 볶음 요리일 확률과 함께 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int값으로 반환)
}

ex) {
    야끼소바 : 100,
    김치볶음밥 : 100,
    김치찜 : 10,
    김치찌개 : 0,
    돼지고기 구이 : 40
}
"""

NOODLE_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 면 요리 레시피 20개를 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int값으로 반환)
}

ex) {
    야끼소바 : 100,
    라멘 : 100
    파스타 : 100,
    김치찌개 : 0
}

"""

SOUP_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 국물, 스프 요리 레시피 20개를 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int값으로 반환)
}

ex) {
    양송이 스프 : 100,
    김치찌개 : 100,
    김치나베 : 100,
    돈까스 : 0,
    김치찜 : 70
}
"""

STEAM_ANSWER_JSON= """
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 찜 요리 레시피 20개를 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:
{
     레시피 제목 : 확률(int값으로 반환)
}

ex) {
    생선찜 : 100,
    찐만두 : 100,
    돼지고기 김치찜 : 100
    김치찌개 : 30,
    야끼소바 : 10
}
"""

SIDE_ANSWER_JSON= """
사이드 메뉴를 추천할 땐 단 하나의 식재료만 사용한 채식주의자 레시피로 추천해줘.
현재 냉장고 재고 정보를 활용하여 즉시 만들 수 있는 사이드 메뉴 채식주의자 레시피 15개를 해당 레시피가 채식주의자가 먹는 사이드 메뉴일 확률과 함께 명시해줘.
무조건 아래와 같은 JSON 형식으로 반환해주고 이외의 말은 하지마:

{
     레시피 제목 : 확률(int값으로 반환)
}

ex) { 
    배추 겉절이 : 100,
    콩나물무침: 100,
    마늘 쫑 장아찌: 100,
    김치 장아찌: 40,
    목살: 0,
    베이컨: 0,
    생선: 0,
    마라: 0
}
"""


define = {
    "중식" : CHINA,
    "양식" : RESTAURANT,
    "한식" : KOREA,
    "일식" : JAPAN,
    "밑반찬" : SIDE_DISH
}

answer = {
    "중식" : CHINA_ANSWER_JSON,
    "양식" : RESTAURANT_ANSWER_JSON,
    "한식" : KOREA_ANSWER_JSON,
    "일식" : JAPAN_ANSWER_JSON,
    "면요리" : NOODLE_ANSWER_JSON,
    "국물 요리": SOUP_ANSWER_JSON,
    "찜 요리": STEAM_ANSWER_JSON,
    "볶음 요리": STIR_FRY_ANSWER_JSON,
    "튀김 요리": FRY_ANSWER_JSON,
    "밑반찬": SIDE_ANSWER_JSON
}