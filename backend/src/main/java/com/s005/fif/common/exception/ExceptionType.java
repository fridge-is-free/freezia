package com.s005.fif.common.exception;

import lombok.Getter;

@Getter
public enum ExceptionType {

    // test
    TEST_400(400, "400 에러"),
    TEST_500(500, "500 에러"),

    // member
    MEMBER_NOT_FOUND(404, "사용자를 찾을 수 없습니다."),

    // recipe
    RECIPE_NOT_FOUND(404, "레시피를 찾을 수 없습니다."),
    RECIPE_NOT_ACCESSIBLE(403, "본인의 레시피가 아닙니다."),
    ;

    private final int code;
    private final String msg;

    ExceptionType(int code, String msg) {
        this.code = code;
        this.msg = msg;
    }
}