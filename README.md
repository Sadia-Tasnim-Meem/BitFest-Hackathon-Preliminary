## API Documentation

### Ingredient Management

#### Retrieve All Ingredients
- **Route**: `/ingredients`  
- **Method**: GET  
- **Description**: Retrieve all available ingredients.  
- **Sample Response**:
  ```json
  [
      {
          "id": 1,
          "name": "Sugar",
          "quantity": 500,
          "unit": "grams",
          "updated_at": "2024-12-21T12:00:00Z"
      },
      {
          "id": 2,
          "name": "Eggs",
          "quantity": 6,
          "unit": "pieces",
          "updated_at": "2024-12-20T10:30:00Z"
      }
  ]
  ```

#### Add a New Ingredient
- **Route**: `/ingredients`  
- **Method**: POST  
- **Description**: Add a new ingredient.  
- **Sample Payload**:
  ```json
  {
      "name": "Milk",
      "quantity": 2,
      "unit": "liters"
  }
  ```  
- **Sample Response**:
  ```json
  {
      "message": "Ingredient added successfully",
      "id": 3
  }
  ```

#### Update an Ingredient
- **Route**: `/ingredients/{id}`  
- **Method**: PUT  
- **Description**: Update an ingredient's quantity or unit.  
- **Sample Payload**:
  ```json
  {
      "quantity": 1.5,
      "unit": "liters"
  }
  ```  
- **Sample Response**:
  ```json
  {
      "message": "Ingredient updated successfully"
  }
  ```

---

### Recipe Management

#### Retrieve All Recipes
- **Route**: `/recipes`  
- **Method**: GET  
- **Description**: Retrieve all stored recipes.  
- **Sample Response**:
  ```json
  [
      {
          "id": 1,
          "title": "Pancakes",
          "ingredients": {
              "Flour": "2 cups",
              "Milk": "1 cup",
              "Eggs": "2"
          },
          "instructions": "Mix all ingredients and cook on a skillet.",
          "category": "Breakfast",
          "added_at": "2024-12-15T09:00:00Z"
      }
  ]
  ```

#### Add a New Recipe (Text)
- **Route**: `/recipes`  
- **Method**: POST  
- **Description**: Add a new recipe from text.  
- **Sample Payload**:
  ```json
  {
      "title": "Chocolate Cake",
      "ingredients": {
          "Flour": "2 cups",
          "Sugar": "1.5 cups",
          "Cocoa Powder": "0.5 cups"
      },
      "instructions": "Mix ingredients, bake at 180°C for 30 minutes.",
      "category": "Dessert"
  }
  ```  
- **Sample Response**:
  ```json
  {
      "message": "Recipe added successfully",
      "id": 2
  }
  ```

#### Add a New Recipe (Image)
- **Route**: `/recipes/image`  
- **Method**: POST  
- **Description**: Add a new recipe from an image.  
- **Sample Payload**:
  ```json
  {
      "image_path": "/uploads/recipe_image.jpg"
  }
  ```  
- **Sample Response**:
  ```json
  {
      "message": "Recipe parsed and added successfully",
      "id": 3
  }
  ```

---

### Chatbot Integration

#### Chatbot Interaction
- **Route**: `/chat`  
- **Method**: POST  
- **Description**: Interact with the chatbot for recipe recommendations based on available ingredients and user preferences.  
- **Sample Payload**:
  ```json
  {
      "user_input": "I want something sweet today."
  }
  ```  
- **Sample Response**:
  ```json
  {
      "message": "Based on your preferences, here are some suggestions:",
      "recipes": [
          {
              "title": "Chocolate Cake",
              "ingredients": {
                  "Flour": "2 cups",
                  "Sugar": "1.5 cups",
                  "Cocoa Powder": "0.5 cups"
              },
              "instructions": "Mix ingredients, bake at 180°C for 30 minutes."
          },
          {
              "title": "Brownies",
              "ingredients": {
                  "Butter": "1 cup",
                  "Sugar": "1 cup",
                  "Cocoa Powder": "0.5 cups"
              },
              "instructions": "Combine ingredients, bake for 25 minutes."
          }
      ]
  }
  
