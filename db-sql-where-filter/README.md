# WHERE Filtering

Beginner | db

For compliance reasons the dashboard may only show adult users (age 18 or older). The `users` table holds people of all ages.

Write a query that returns all columns of `users`, but only the rows where `age` is greater than or equal to 18.

### Constraints

- Return all columns (id, name, email, age)
- Only rows where `age >= 18` (someone who is exactly 18 counts)
- No sorting required

### Hints

<details>
<summary>Hint 1</summary>

`WHERE` goes after `FROM` and holds a condition each row must satisfy.

</details>

<details>
<summary>Hint 2</summary>

Be careful with the boundary: `>` and `>=` treat 18 differently.

</details>
