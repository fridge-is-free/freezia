export default function ReplyMessage({ chat }) {
  const { profile } = sessionStorage;
  const { name } = JSON.parse(profile);
  return (
    <div className="reply-chat-message">
      <span>👋 안녕하세요! </span>
      <div />
      <span className="bold">{name}</span>
      <span>
        님의 냉장고 속 식재료, 기피 식재료, 지병 정보를 바탕으로 다양한 레시피를
        제공해드리는 대화형 서비스입니다.
      </span>
    </div>
  );
}
