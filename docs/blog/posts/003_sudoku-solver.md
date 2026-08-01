---
date:
  created: 2022-02-07T08:00:00+08:00
slug: sudoku-solver
archive: true
---

# Video: Solving sudokus using depth first search

I've never been much of a sudoku fan, but ever since I've started coding I've wanted to create a program that is able to solve them. I found out it was a bit of a tall ask for a newbie programmer a few years ago, but stumbling across my failed attempt, I decided to give it another go.

<!-- more -->

This time the goal not only to make a program to solve sudokus, but also to give consideration to the style of the code. By structuring my code using object oriented programming, it allows the code to be expanded upon down the line without refactoring everything. The separation between the view and logic of the application would allow views to be used, and even allows the logic to be switched out in a way that also enables sudoku variants.

In the algorithmic portion of the code, I used a backtracking/depth first search algorithm in order to solve the sudokus. Although not the most efficient way to solve a sudoku, it still works to solve the grid in a fraction of a second!

<iframe width="560" height="315" src="https://www.youtube.com/embed/RlJN6F4copU?si=aSfJoi-heaxxXtHX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
