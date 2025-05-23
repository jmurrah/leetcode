"""
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. 
The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
"""


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes = {recipe: ingredients[i] for i, recipe in enumerate(recipes)}
        supplies = set(supplies)
        impossible = set()

        def dfs(recipe, seen):
            if recipe in supplies:
                return True
            if recipe in impossible or recipe not in recipes or recipe in seen:
                return False
            
            seen.add(recipe)
            if all([dfs(ingredient, seen) for ingredient in recipes[recipe]]):
                supplies.add(recipe)
                return True
            
            impossible.add(recipe)
            return False
        
        output = []
        for recipe in recipes.keys():
            if dfs(recipe, set()):
                output.append(recipe)

        return output
