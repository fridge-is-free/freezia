export default function FilterList({
  recipeTypeList,
  selectedList,
  setSelectedList,
  recipeListRef,
}) {
  const selectItem = (idx) => {
    if (selectedList.includes(idx)) {
      setSelectedList(selectedList.filter((item) => item !== idx));
    } else setSelectedList([...selectedList, idx]);
    recipeListRef.current.scrollTop = 0;
  };

  return (
    <div className="filter-list-container">
      {recipeTypeList.map((filter) => (
        <div
          className={`filter-item f-0 box-shadow ${selectedList.includes(filter) ? 'filter-item-selected' : ''}`}
          key={filter}
          onClick={() => {
            selectItem(filter);
          }}
        >
          {filter}
        </div>
      ))}
    </div>
  );
}
