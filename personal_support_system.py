#!/usr/bin/env python3

import textwrap


LIFE_AREAS = {
    "1": {
        "name": "업무 / 공부",
        "examples": [
            "온라인 회의/수업 시작 전에 링크 열어두기",
            "반복적으로 쓰는 보고서/메일 양식 복붙해서 채우기",
            "매일 해야 하는 짧은 업무(출퇴근 기록, 이슈 상태 업데이트 등)",
            "주간 회의 전에 지난주 To-Do 정리해서 가져가기",
            "복붙 실수 나기 쉬운 엑셀/노션 정리 작업",
        ],
    },
    "2": {
        "name": "금융 / 행정",
        "examples": [
            "월세/관리비/대출 이자 납부일 챙기기",
            "각종 정기 구독(넷플릭스, 유튜브 프리미엄 등) 결제일 파악하기",
            "연말정산/세금 관련 서류 챙기기",
            "카드 사용 알림 보고 이상 결제 있는지 확인하기",
            "통장 잔액이 특정 금액 아래로 떨어지는 것 확인하기",
        ],
    },
    "3": {
        "name": "건강 / 루틴",
        "examples": [
            "매일 먹어야 하는 영양제/약 챙겨 먹기",
            "정기적으로 치과/검진 예약하기",
            "매일/격일로 하는 운동 루틴 기억하기",
            "잠들기 전 핸드폰 알람/수면 모드 설정하기",
            "수분 섭취량/걸음 수 같은 단순 트래킹 기록하기",
        ],
    },
    "4": {
        "name": "디지털 정리",
        "examples": [
            "다운로드 폴더/바탕화면에 쌓인 파일 정리하기",
            "중복 스크린샷/사진 지우기",
            "이메일 뉴스레터/스팸 구독 해지하기",
            "클라우드 저장공간 용량 확인하고 정리하기",
            "비밀번호/2단계 인증 백업 정보 정리하기",
        ],
    },
}


def print_header() -> None:
    title = "AI Helper – '실수만 있고 보상은 적은 일' 빠르게 떠올리기"
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()
    intro = (
        "이 도구는 창의성이 거의 필요 없고, 실수하면 스트레스만 생기는 루틴 작업을 "
        "빠르게 떠올리도록 도와주는 간단한 CLI 비서입니다.\n"
        "지금 당장 개선하고 싶은 삶의 영역을 하나 골라보세요."
    )
    print(textwrap.fill(intro, width=80))
    print()


def choose_area() -> str | None:
    print("어느 영역에서 이런 일을 줄이고 싶나요?")
    for key, info in LIFE_AREAS.items():
        print(f"  {key}. {info['name']}")
    print("  q. 종료")
    print()

    while True:
        choice = input("번호를 입력하세요 (예: 1) > ").strip()
        if choice.lower() in {"q", "quit", "exit"}:
            return None
        if choice in LIFE_AREAS:
            return choice
        print("유효한 번호가 아닙니다. 1~5 중 하나를 고르거나 q로 종료할 수 있습니다.")


def suggest_tasks(area_key: str) -> None:
    info = LIFE_AREAS[area_key]
    name = info["name"]
    examples = info["examples"]

    print()
    print(f"[선택한 영역] {name}")
    print("-" * (len(name) + 9))
    print()

    explanation = (
        "아래는 이 영역에서 흔하게 발생하는, 실수하면 스트레스만 생기고 "
        "창의성은 거의 필요 없는 루틴 작업들입니다.\n"
        "이 중에서 '나도 맨날 하는데 귀찮다/자주 까먹는다' 싶은 항목에 표시를 해보세요."
    )
    print(textwrap.fill(explanation, width=80))
    print()

    for idx, ex in enumerate(examples, start=1):
        print(f"  [{idx}] {ex}")
    print()

    follow_up = (
        "아이디어를 더 뽑고 싶다면, 번호 옆에 ✅ 를 mentally 붙여두고, "
        "이 항목들을\n"
        "- 체크리스트로 만들지,\n"
        "- 캘린더/리마인더에 넣을지,\n"
        "- 스크립트/자동화로 처리할 수 있을지\n"
        "같이 생각해보면 좋습니다."
    )
    print(textwrap.fill(follow_up, width=80))
    print()


def main() -> None:
    print_header()
    area = choose_area()
    if area is None:
        print("\n종료합니다. 오늘도 불필요한 스트레스는 조금 덜어보길 바라요.")
        return
    suggest_tasks(area)


if __name__ == "__main__":
    main()

