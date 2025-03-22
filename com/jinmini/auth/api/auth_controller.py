from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from typing import Dict, Any, Optional
from com.jinmini.accoount.guest.customer.api.customer_controller import CustomerController

class AuthController:
    """인증 관련 비즈니스 로직을 처리하는 컨트롤러"""
    
    async def login(self, db: AsyncSession, user_id: str, password: str) -> Dict[str, Any]:
 
        # 임시로 기존 컨트롤러 사용
        customer_controller = CustomerController()
        
        try:
            # 사용자 조회
            user = await customer_controller.get_customer_by_id(db=db, user_id=user_id)
            if not user:
                return {
                    "success": False, 
                    "message": "등록되지 않은 사용자입니다.",
                    "user": None
                }
            
            # 비밀번호 검증 로직은 임시로 간단하게 구현
            # TODO: 비밀번호 해시 비교 로직으로 변경 필요
            from sqlalchemy import select
            from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
            
            query = select(CustomerEntity.password).where(CustomerEntity.user_id == user_id)
            result = await db.execute(query)
            stored_password = result.scalar_one_or_none()
            
            if not stored_password or password != stored_password:
                return {
                    "success": False,
                    "message": "비밀번호가 일치하지 않습니다.",
                    "user": None
                }
            
            # 로그인 성공
            return {
                "success": True,
                "message": "로그인 성공",
                "user": user
            }
            
        except Exception as e:
            print(f"로그인 처리 중 오류 발생: {e}")
            return {
                "success": False,
                "message": f"로그인 처리 중 오류가 발생했습니다: {str(e)}",
                "user": None
            }
    
    async def signup(self, db: AsyncSession, user_data: Dict[str, Any]) -> Dict[str, Any]:

        # 임시로 기존 컨트롤러 사용
        customer_controller = CustomerController()
        
        try:
            # 기존 회원가입 로직 호출
            from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
            
            # 요청 데이터를 CustomerSchema로 변환
            new_customer = CustomerSchema(
                user_id=user_data.get("user_id"),
                name=user_data.get("name"),
                email=user_data.get("email"),
                password=user_data.get("password")
            )
            
            # 회원가입 처리
            result = await customer_controller.create_customer(db=db, new_customer=new_customer)
            return result
        except Exception as e:
            print(f"회원가입 처리 중 오류 발생: {e}")
            raise HTTPException(status_code=500, detail=f"회원가입 처리 중 오류가 발생했습니다: {str(e)}") 