from enum import Enum

class CustomerAction(Enum):

    CREATE_CUSTOMER = "create_customer" # 고객 생성
    DELETE_CUSTOMER = "delete_customer" # 고객 삭제

    GET_CUSTOMERS = "get_customers" # 모든 고객 조회
    GET_CUSTOMER_BY_ID = "get_customer_by_id" # 고객 아이디로 조회
    SEARCH_CUSTOMERS = "search_customers" # 조건 검색

    UPDATE_CUSTOMER = "update_customer" # 고객 정보 전체 수정
    PATCH_CUSTOMER = "patch_customer" # 고객 정보 일부 수정
    CHANGE_PASSWORD = "change_password" # 비밀번호 변경

   

