import pytest
from src.controllers.recipecontroller import RecipeController
from unittest.mock import MagicMock


@pytest.fixture
def recipe_controller():
    mock_controller = MagicMock()
    mock = RecipeController(mock_controller)
    return mock

@pytest.mark.unit
def test_get_recipe_true_readiness0point2(recipe_controller):
    pass

@pytest.mark.unit
def test_get_recipe_false_readiness0point2(recipe_controller):
    pass

@pytest.mark.unit
def test_get_recipe_readiness0(recipe_controller):
    pass

@pytest.mark.unit
def test_get_recipe_no_recipe_available(recipe_controller):
    result = recipe_controller.get_recipe(MagicMock(), True)

    assert result == None