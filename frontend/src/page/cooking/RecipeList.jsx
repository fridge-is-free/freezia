import { Link } from 'react-router-dom';
import '../../assets/styles/cooking/recipelist.css';
import FilterList from '../../components/cooking/FilterList';
import Header from '../../components/cooking/Header';

export default function RecipeList() {
  const recipeList = JSON.parse(sessionStorage.recipeList);

  return (
    <div className="cooking-recipe-list-container">
      <Header isHome />
      <FilterList />
      <div className="cooking-recipe-list">
        <Link
          to="/Cooking/recipe/create"
          className="recipe-create-button box-shadow link "
        >
          <div className="recipe-create-button-text bold f-2">
            레시피 생성하기
          </div>
        </Link>
        {recipeList.map(({ name, imgUrl, recipeId, cookTime }) => (
          <Link
            to={`/Cooking/recipe/${recipeId}`}
            key={recipeId}
            style={{ backgroundImage: `url(${imgUrl})` }}
            className="recipe-item-container box-shadow link"
          >
            <div className="recipe-item-description">
              <div className="recipe-item-background-filter" />
              <div className="recipe-item-description-wrapper">
                <div className="recipe-item-description-duration f-0 o-5">
                  <img
                    src="/images/cooking/time.svg"
                    alt="아이콘"
                    className="recipe-item-description-duration-icon"
                  />
                  {`${cookTime}min`}
                </div>
                <div className="recipe-item-description-name">{name}</div>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
